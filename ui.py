from book import *
from layout import *

from PySide6 import QtCore, QtGui, QtWidgets
import os


class UI(QMainWindow):
  book: RawBook

  def __init__(self):
    super(UI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

  @QtCore.Slot()
  def on_openFileButton_clicked(self):
    # Open text file
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "Text Files(*.txt);;All Files(*)")

    if filePath != "":
      self.ui.filePathLineEdit.setText(filePath)
      self.book = RawBook(filePath)

      # Display metadata
      self.book.getMetadata()
      self.ui.titleLineEdit.setText(self.book.title)
      self.ui.authorLineEdit.setText(self.book.author)
      self.ui.illustratorLineEdit.setText(self.book.illustrator)
      self.ui.translatorLineEdit.setText(self.book.translator)
      self.ui.sourceLineEdit.setText(self.book.source)
      self.ui.languageLineEdit.setText(self.book.language)
      self.ui.subjectLineEdit.setText(self.book.subject)

      # Display contents
      self.book.getContents()
      contents = ""
      for chapter in self.book.contents:
        contents = contents + chapter.string + "\n"
      self.ui.contentsTextEdit.setPlainText(contents.strip())

      # Get other data
      self.book.getChaptersIndex()
      self.book.getIllustrationsPath()
      self.book.findIllustrationsIndex()

  @QtCore.Slot()
  def on_okButton_clicked(self):
    pass
