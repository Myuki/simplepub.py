from ebooklib import epub

from enum import Enum
from typing import Dict, List, Set
import os


# Identify book text type for parsing
class RawTextType(Enum):
  tsdm: int = 0
  lk: int = 0


# Index chapter
class Chapter:
  string: str = ""
  index: int = 0
  level: int = 0
  illustration: bool = False


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
  textPath: str = ""
  textDirPath: str = ""
  rawText: str = ""
  rawTextType: RawTextType
  rawLines: tuple

  # Book data
  contentsIndex: int = 0
  afterContentsIndex: int = 0
  contents: List[Chapter] = []

  # illustrationPath: index
  illustrations: Dict[str, int] = {}

  def __init__(self, filePath: str):
    with open(filePath, "rt", encoding="utf-8") as file:
      self.textPath = filePath
      self.textDirPath = os.path.dirname(self.textPath)
      # Get the raw text and strip BOM
      self.rawText = file.read(-1).lstrip(u'\ufeff')
      self.rawLines = tuple(self.rawText.splitlines())

    # Parse the raw text type in first 20 lines
    for line in self.rawLines[0:20]:
      if "tsdm" in line:
        self.rawTextType = RawTextType.tsdm
        break
      if "lightnovel" in line:
        self.rawTextType = RawTextType.lk
        break

  # Get metadata in different raw text type
  def getMetadata(self):
    # TSDM/LK
    if self.rawTextType == RawTextType.tsdm or self.rawTextType == RawTextType.lk:
      self.title = self.rawLines[0].strip()
      self.source = "天使動漫" if self.rawTextType == RawTextType.tsdm else "輕之國度"
      self.language = "zh-Hant"
      self.subject = "輕小説"

      # Get metadata in first 20 lines
      for line in self.rawLines[0:20]:
        if self.author == "" and ("作者" in line or "作者" in line):
          self.author = line.split("：")[1].strip()
        if self.illustrator == "" and ("插畫" in line or "插画" in line):
          self.illustrator = line.split("：")[1].strip()
        if self.translator == "" and ("譯者" in line or "译者" in line):
          self.translator = line.split("：")[1].strip()

  # Get book contents
  def getContents(self):
    # Find contents in first 100 lines
    index: int = 0
    for line in self.rawLines[0:100]:
      index += 1
      if "CONTENTS" in line:
        self.contentsIndex = index
        break
    # Get contents in following lines
    while (not self.rawLines[index].isspace()):
      chapter = Chapter()
      chapter.string = self.rawLines[index].strip()
      self.contents.append(chapter)
      index += 1
    self.afterContentsIndex = index

  # Find all chapters location
  def getChaptersIndex(self):
    for chapter in self.contents:
      chapter.index = self.findFirstLine(self.afterContentsIndex, chapter.string)
      # TSDM/LK chapter may has title illustration
      if self.rawTextType == RawTextType.tsdm or self.rawTextType == RawTextType.lk:
        if not self.rawLines[chapter.index - 1].isspace():
          chapter.illustration = True

  # Get all image in text directory
  def getIllustrationsPath(self):
    subFilePaths: List[str] = os.listdir(self.textDirPath)
    for filePath in subFilePaths:
      if filePath.endswith(".png") or filePath.endswith(".webp") or filePath.endswith(".jpg"):
        self.illustrations[self.textDirPath + "/" + filePath] = -1

  # Find all image location
  def findIllustrationsIndex(self, beginning: str = "", ending: str = ""):
    for illustration in self.illustrations:
      illustrationName = os.path.basename(os.path.splitext(illustration)[0])
      self.illustrations[illustration] = self.findFirstLine(0, illustrationName, beginning, ending)

  # Find fist line in all lines
  def findFirstLine(self, startIndex: int, substring: str, beginning: str = "", ending: str = "") -> int:
    index = startIndex
    for line in self.rawLines[startIndex:]:
      if substring in line and line.startswith(beginning) and line.endswith(ending):
        return index
      index += 1
    return -1

  # Find lines in all lines
  def findLines(self, startIndex: int, substring: str, beginning: str = "", ending: str = "") -> Set[int]:
    result: Set[int] = set()
    index = startIndex
    for line in self.rawLines[startIndex:]:
      if substring in line and line.startswith(beginning) and line.endswith(ending):
        result.add(index)
      index += 1
    return result

  # Find lines in certain lines
  def findLinesInLines(self, indexSet: Set[int], substring: str, beginning: str = "", ending: str = "") -> Set[int]:
    result: Set[int] = set()
    for index in indexSet:
      line = self.rawLines[index]
      if substring in line and line.startswith(beginning) and line.endswith(ending):
        result.add(index)
    return result
