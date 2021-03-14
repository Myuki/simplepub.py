from ebooklib import epub

from enum import Enum
from typing import Dict, List, Set
import os


# Identify book text type for parsing
class RawTextType(Enum):
  default: int = 0
  tsdm: int = 1
  lk: int = 1


# Index chapter
class Chapter:
  string: str = ""
  level: int = 0
  index: int = 0
  illustration: bool = False

  def __init__(self, string: str, level: int = 0, index: int = 0):
    self.string = string
    self.level = level
    self.index = index


class RawBook:
  # Metadata
  title: str = ""
  author: str = ""
  illustrator: str = ""
  translator: str = ""
  source: str = ""
  language: str = ""
  subject: str = ""

  # Raw data
  rawTextType: RawTextType = RawTextType.default
  __textPath: str = ""
  __textDirPath: str = ""
  __rawText: str = ""
  __rawLines: tuple

  # Book data
  contentsIndex: int = 0
  afterContentsIndex: int = 0
  contents: List[Chapter] = []

  # Illustration data
  # illustrationPath: index
  illustrations: Dict[str, int] = {}
  illustrationPrefix: str = ""
  illustrationSuffix: str = ""

  def __init__(self, filePath: str):
    with open(filePath, "rt", encoding="utf-8") as file:
      self.__textPath = filePath
      self.__textDirPath = os.path.dirname(self.__textPath)
      # Get the raw text and strip BOM
      self.__rawText = file.read(-1).lstrip(u'\ufeff')
      self.__rawLines = tuple(self.__rawText.splitlines())
      self.initIllustrationsPath()

    # Parse the raw text type in first 20 lines
    for line in self.__rawLines[0:20]:
      if "tsdm" in line:
        self.rawTextType = RawTextType.tsdm
        break
      if "lightnovel" in line:
        self.rawTextType = RawTextType.lk
        break

    # Init in different raw text type
    if self.rawTextType == RawTextType.tsdm or self.rawTextType == RawTextType.lk:
      self.initMetadata()
      self.illustrationPrefix = "　　（"
      self.illustrationSuffix = "）"

  # Get metadata in different raw text type
  def initMetadata(self):
    # TSDM/LK
    if self.rawTextType == RawTextType.tsdm or self.rawTextType == RawTextType.lk:
      for line in self.__rawLines:
        if not line.isspace():
          self.title = self.__rawLines[0].strip()
      self.source = "天使動漫" if self.rawTextType == RawTextType.tsdm else "輕之國度"
      self.language = "zh-Hant"
      self.subject = "輕小説"

      # Get metadata in first 20 lines
      for line in self.__rawLines[0:20]:
        if self.author == "" and ("作者" in line or "作者" in line):
          self.author = line.split("：")[1].strip()
        if self.illustrator == "" and ("插畫" in line or "插画" in line):
          self.illustrator = line.split("：")[1].strip()
        if self.translator == "" and ("譯者" in line or "译者" in line):
          self.translator = line.split("：")[1].strip()

  # Get book contents
  def initContents(self):
    # Find contents in first 100 lines
    index: int = 0
    for line in self.__rawLines[0:100]:
      index += 1
      if "CONTENTS" in line:
        self.contentsIndex = index
        break
    # Get contents in following lines
    while (not self.__rawLines[index].isspace()):
      line: str = self.__rawLines[index]
      level: int = 0
      # Set chapter level by count prefixed \t
      if line.startswith("\t"):
        for char in line:
          if char == "\t":
            level += 1
      chapter = Chapter(line.strip(), level)
      self.contents.append(chapter)
      index += 1
    self.afterContentsIndex = index

  # Find all chapters location
  def initChaptersIndex(self):
    for chapter in self.contents:
      chapter.index = self.findLine(self.afterContentsIndex, chapter.string)
      # TSDM/LK chapter may has title illustration
      if self.rawTextType == RawTextType.tsdm or self.rawTextType == RawTextType.lk:
        if not self.__rawLines[chapter.index - 1].isspace():
          chapter.illustration = True

  # Get all image in text directory
  def initIllustrationsPath(self):
    subFilePaths: List[str] = os.listdir(self.__textDirPath)
    for filePath in subFilePaths:
      if filePath.endswith(".png") or filePath.endswith(".webp") or filePath.endswith(".jpg"):
        self.illustrations[self.__textDirPath + "/" + filePath] = -1

  # Set contents by string
  def setContents(self, string: str):
    rawContens: List[str] = string.splitlines()
    contents: List[Chapter] = []
    # Set chapter level by count prefixed \t
    for line in rawContens:
      level: int = 0
      if line.startswith("\t"):
        for char in line:
          if char == "\t":
            level += 1
      chapter = Chapter(line.strip(), level)
      contents.append(chapter)
    self.contents = contents

  # Find all image location
  def findIllustrationsIndex(self, prefix: str = "", suffix: str = ""):
    for illustration in self.illustrations:
      illustrationName = os.path.basename(os.path.splitext(illustration)[0])
      self.illustrations[illustration] = self.findLine(0, illustrationName, prefix, suffix)

  # Find fist line in all lines
  def findLine(self, startIndex: int, substring: str, prefix: str = "", suffix: str = "") -> int:
    index = startIndex
    for line in self.__rawLines[startIndex:]:
      if substring in line and line.startswith(prefix) and line.endswith(suffix):
        return index
      index += 1
    return -1
