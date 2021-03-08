# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.verticalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_1, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileLineEdit = QLineEdit(self.centralwidget)
        self.fileLineEdit.setObjectName(u"fileLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLineEdit.sizePolicy().hasHeightForWidth())
        self.fileLineEdit.setSizePolicy(sizePolicy)
        self.fileLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fileLineEdit)

        self.openFileButton = QPushButton(self.centralwidget)
        self.openFileButton.setObjectName(u"openFileButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.openFileButton.sizePolicy().hasHeightForWidth())
        self.openFileButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.openFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contentsLabel = QLabel(self.centralwidget)
        self.contentsLabel.setObjectName(u"contentsLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentsLabel.sizePolicy().hasHeightForWidth())
        self.contentsLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.contentsLabel)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy3)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_3.addWidget(self.plainTextEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.IllustrationsLabel = QLabel(self.centralwidget)
        self.IllustrationsLabel.setObjectName(u"IllustrationsLabel")
        sizePolicy2.setHeightForWidth(self.IllustrationsLabel.sizePolicy().hasHeightForWidth())
        self.IllustrationsLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.IllustrationsLabel)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.IllustrationBeginlabel = QLabel(self.centralwidget)
        self.IllustrationBeginlabel.setObjectName(u"IllustrationBeginlabel")
        sizePolicy2.setHeightForWidth(self.IllustrationBeginlabel.sizePolicy().hasHeightForWidth())
        self.IllustrationBeginlabel.setSizePolicy(sizePolicy2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.IllustrationBeginlabel)

        self.IllustrationBeginLineEdit = QLineEdit(self.centralwidget)
        self.IllustrationBeginLineEdit.setObjectName(u"IllustrationBeginLineEdit")
        sizePolicy.setHeightForWidth(self.IllustrationBeginLineEdit.sizePolicy().hasHeightForWidth())
        self.IllustrationBeginLineEdit.setSizePolicy(sizePolicy)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.IllustrationBeginLineEdit)

        self.IllustrationEndlabel = QLabel(self.centralwidget)
        self.IllustrationEndlabel.setObjectName(u"IllustrationEndlabel")
        sizePolicy2.setHeightForWidth(self.IllustrationEndlabel.sizePolicy().hasHeightForWidth())
        self.IllustrationEndlabel.setSizePolicy(sizePolicy2)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.IllustrationEndlabel)

        self.IllustrationEndLineEdit = QLineEdit(self.centralwidget)
        self.IllustrationEndLineEdit.setObjectName(u"IllustrationEndLineEdit")
        sizePolicy.setHeightForWidth(self.IllustrationEndLineEdit.sizePolicy().hasHeightForWidth())
        self.IllustrationEndLineEdit.setSizePolicy(sizePolicy)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.IllustrationEndLineEdit)


        self.verticalLayout_6.addLayout(self.formLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.metadataLabel = QLabel(self.centralwidget)
        self.metadataLabel.setObjectName(u"metadataLabel")
        sizePolicy2.setHeightForWidth(self.metadataLabel.sizePolicy().hasHeightForWidth())
        self.metadataLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.metadataLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy2.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.titleLineEdit = QLineEdit(self.centralwidget)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        sizePolicy.setHeightForWidth(self.titleLineEdit.sizePolicy().hasHeightForWidth())
        self.titleLineEdit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleLineEdit)

        self.authorLabel = QLabel(self.centralwidget)
        self.authorLabel.setObjectName(u"authorLabel")
        sizePolicy2.setHeightForWidth(self.authorLabel.sizePolicy().hasHeightForWidth())
        self.authorLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLabel)

        self.authorLineEdit = QLineEdit(self.centralwidget)
        self.authorLineEdit.setObjectName(u"authorLineEdit")
        sizePolicy.setHeightForWidth(self.authorLineEdit.sizePolicy().hasHeightForWidth())
        self.authorLineEdit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorLineEdit)

        self.illustratorLabel = QLabel(self.centralwidget)
        self.illustratorLabel.setObjectName(u"illustratorLabel")
        sizePolicy2.setHeightForWidth(self.illustratorLabel.sizePolicy().hasHeightForWidth())
        self.illustratorLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.illustratorLabel)

        self.illustratorLineEdit = QLineEdit(self.centralwidget)
        self.illustratorLineEdit.setObjectName(u"illustratorLineEdit")
        sizePolicy.setHeightForWidth(self.illustratorLineEdit.sizePolicy().hasHeightForWidth())
        self.illustratorLineEdit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.illustratorLineEdit)

        self.translatorLabel = QLabel(self.centralwidget)
        self.translatorLabel.setObjectName(u"translatorLabel")
        sizePolicy2.setHeightForWidth(self.translatorLabel.sizePolicy().hasHeightForWidth())
        self.translatorLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.translatorLabel)

        self.translatorLineEdit = QLineEdit(self.centralwidget)
        self.translatorLineEdit.setObjectName(u"translatorLineEdit")
        sizePolicy.setHeightForWidth(self.translatorLineEdit.sizePolicy().hasHeightForWidth())
        self.translatorLineEdit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.translatorLineEdit)


        self.verticalLayout_6.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        sizePolicy2.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.okButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"simplepub.py", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.contentsLabel.setText(QCoreApplication.translate("MainWindow", u"Contents:", None))
        self.IllustrationsLabel.setText(QCoreApplication.translate("MainWindow", u"Illustrations:", None))
        self.IllustrationBeginlabel.setText(QCoreApplication.translate("MainWindow", u"Begin Identity:", None))
        self.IllustrationEndlabel.setText(QCoreApplication.translate("MainWindow", u"End Identity:", None))
        self.metadataLabel.setText(QCoreApplication.translate("MainWindow", u"Metadata:", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.illustratorLabel.setText(QCoreApplication.translate("MainWindow", u"Illustrator:", None))
        self.translatorLabel.setText(QCoreApplication.translate("MainWindow", u"Translator:", None))
        self.okButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

