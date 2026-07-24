# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_about.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)
import resources_rc

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(350, 260)
        AboutWindow.setMinimumSize(QSize(350, 260))
        AboutWindow.setMaximumSize(QSize(350, 260))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(7)
        AboutWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/media/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setStyleSheet(u"font-family: Inter;")
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 332, 242))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.ffstudio = QLabel(self.frame)
        self.ffstudio.setObjectName(u"ffstudio")
        self.ffstudio.setGeometry(QRect(40, 11, 251, 81))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.ffstudio.setFont(font1)
        self.ffstudio.setPixmap(QPixmap(u":/media/logo.png"))
        self.ffstudio.setScaledContents(True)
        self.description = QLabel(self.frame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(20, 110, 301, 16))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(10)
        self.description.setFont(font2)
        self.used = QLabel(self.frame)
        self.used.setObjectName(u"used")
        self.used.setGeometry(QRect(20, 130, 301, 16))
        self.used.setFont(font2)
        self.copyright = QLabel(self.frame)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setGeometry(QRect(20, 160, 171, 16))
        self.copyright.setFont(font2)
        self.copyright.setScaledContents(False)
        self.pp1 = QLabel(self.frame)
        self.pp1.setObjectName(u"pp1")
        self.pp1.setGeometry(QRect(20, 190, 81, 16))
        self.pp1.setFont(font2)
        self.pp1.setOpenExternalLinks(True)
        self.pp2 = QLabel(self.frame)
        self.pp2.setObjectName(u"pp2")
        self.pp2.setGeometry(QRect(105, 190, 211, 16))
        self.pp2.setFont(font2)
        self.pp2.setOpenExternalLinks(True)
        self.pp2_2 = QLabel(self.frame)
        self.pp2_2.setObjectName(u"pp2_2")
        self.pp2_2.setGeometry(QRect(105, 210, 181, 16))
        self.pp2_2.setFont(font2)
        self.pp2_2.setOpenExternalLinks(True)
        self.pp1_2 = QLabel(self.frame)
        self.pp1_2.setObjectName(u"pp1_2")
        self.pp1_2.setGeometry(QRect(20, 210, 81, 16))
        self.pp1_2.setFont(font2)
        self.pp1_2.setOpenExternalLinks(True)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About FFmpeg Studio", None))
        self.ffstudio.setText("")
        self.description.setText(QCoreApplication.translate("AboutWindow", u"Simple FFmpeg tool for working with media files.", None))
        self.used.setText(QCoreApplication.translate("AboutWindow", u"Made using Python, QtDesigner and FFmpeg.", None))
        self.copyright.setText(QCoreApplication.translate("AboutWindow", u"Copyright \u00a9 2026 pythoncbk", None))
        self.pp1.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>Project page:</p></body></html>", None))
        self.pp2.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><a href=\"https://github.com/pythonCBK/ffmpegstudio\"><span style=\" text-decoration: underline; color:#99ebff;\">github.com/pythonCBK/ffmpegstudio</span></a></p></body></html>", None))
        self.pp2_2.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><a href=\"https://github.com/pythonCBK\"><span style=\" text-decoration: underline; color:#99ebff;\">github.com/pythonCBK</span></a></p></body></html>", None))
        self.pp1_2.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>Author:</p></body></html>", None))
    # retranslateUi

