# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1363, 569)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	/*background-image: url(:/images/images/images/PyDracula.png);*/\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rg"
                        "b(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: "
                        "rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	bo"
                        "rder-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border"
                        "-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color:"
                        " rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	backgroun"
                        "d-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backgrou"
                        "nd-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
""
                        "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	"
                        "subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QComm"
                        "andLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(60, 68, 83);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(55, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Facial_Button = QPushButton(self.topMenu)
        self.Facial_Button.setObjectName(u"Facial_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Facial_Button.sizePolicy().hasHeightForWidth())
        self.Facial_Button.setSizePolicy(sizePolicy)
        self.Facial_Button.setMinimumSize(QSize(0, 40))
        self.Facial_Button.setFont(font)
        self.Facial_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Facial_Button.setLayoutDirection(Qt.LeftToRight)
        self.Facial_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png)")

        self.verticalLayout_8.addWidget(self.Facial_Button)

        self.Location_Button = QPushButton(self.topMenu)
        self.Location_Button.setObjectName(u"Location_Button")
        sizePolicy.setHeightForWidth(self.Location_Button.sizePolicy().hasHeightForWidth())
        self.Location_Button.setSizePolicy(sizePolicy)
        self.Location_Button.setMinimumSize(QSize(0, 40))
        self.Location_Button.setFont(font)
        self.Location_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Location_Button.setLayoutDirection(Qt.LeftToRight)
        self.Location_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-location-pin.png)")

        self.verticalLayout_8.addWidget(self.Location_Button)

        self.Connection_Button = QPushButton(self.topMenu)
        self.Connection_Button.setObjectName(u"Connection_Button")
        sizePolicy.setHeightForWidth(self.Connection_Button.sizePolicy().hasHeightForWidth())
        self.Connection_Button.setSizePolicy(sizePolicy)
        self.Connection_Button.setMinimumSize(QSize(0, 40))
        self.Connection_Button.setFont(font)
        self.Connection_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Connection_Button.setLayoutDirection(Qt.LeftToRight)
        self.Connection_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-wifi-signal-2.png)")

        self.verticalLayout_8.addWidget(self.Connection_Button)

        self.Exit_Button = QPushButton(self.topMenu)
        self.Exit_Button.setObjectName(u"Exit_Button")
        sizePolicy.setHeightForWidth(self.Exit_Button.sizePolicy().hasHeightForWidth())
        self.Exit_Button.setSizePolicy(sizePolicy)
        self.Exit_Button.setMinimumSize(QSize(0, 40))
        self.Exit_Button.setFont(font)
        self.Exit_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Exit_Button.setLayoutDirection(Qt.LeftToRight)
        self.Exit_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.Exit_Button)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Facial_Recognition_Widget = QWidget()
        self.Facial_Recognition_Widget.setObjectName(u"Facial_Recognition_Widget")
        self.Facial_Recognition_Widget.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;")
        self.horizontalLayout_2 = QHBoxLayout(self.Facial_Recognition_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Display_Frame = QFrame(self.Facial_Recognition_Widget)
        self.Display_Frame.setObjectName(u"Display_Frame")
        self.Display_Frame.setFrameShape(QFrame.StyledPanel)
        self.Display_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Display_Frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Display_Tittle = QLabel(self.Display_Frame)
        self.Display_Tittle.setObjectName(u"Display_Tittle")
        self.Display_Tittle.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout_4.addWidget(self.Display_Tittle)

        self.Video_Frame = QFrame(self.Display_Frame)
        self.Video_Frame.setObjectName(u"Video_Frame")
        self.Video_Frame.setMinimumSize(QSize(0, 0))
        self.Video_Frame.setFrameShape(QFrame.StyledPanel)
        self.Video_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Video_Frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Video_Label = QLabel(self.Video_Frame)
        self.Video_Label.setObjectName(u"Video_Label")
        self.Video_Label.setMinimumSize(QSize(500, 500))

        self.verticalLayout_16.addWidget(self.Video_Label)


        self.verticalLayout_4.addWidget(self.Video_Frame)


        self.horizontalLayout_2.addWidget(self.Display_Frame)

        self.Attendance_Frame = QFrame(self.Facial_Recognition_Widget)
        self.Attendance_Frame.setObjectName(u"Attendance_Frame")
        self.Attendance_Frame.setFrameShape(QFrame.StyledPanel)
        self.Attendance_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Attendance_Frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Attendance_title = QLabel(self.Attendance_Frame)
        self.Attendance_title.setObjectName(u"Attendance_title")
        self.Attendance_title.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout_5.addWidget(self.Attendance_title)

        self.Attendance_Content = QFrame(self.Attendance_Frame)
        self.Attendance_Content.setObjectName(u"Attendance_Content")
        self.Attendance_Content.setFrameShape(QFrame.StyledPanel)
        self.Attendance_Content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Attendance_Content)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.Attendance_Content)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem21)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(22, 22, 22, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet(u"background-color: rgb(22, 22, 22);")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.Attendance_Content)


        self.horizontalLayout_2.addWidget(self.Attendance_Frame)

        self.stackedWidget.addWidget(self.Facial_Recognition_Widget)
        self.Proximity_Detection_Widget = QWidget()
        self.Proximity_Detection_Widget.setObjectName(u"Proximity_Detection_Widget")
        self.Proximity_Detection_Widget.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.Proximity_Detection_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PROXIMITY_LABEL_2 = QLabel(self.Proximity_Detection_Widget)
        self.PROXIMITY_LABEL_2.setObjectName(u"PROXIMITY_LABEL_2")
        self.PROXIMITY_LABEL_2.setMinimumSize(QSize(0, 20))
        self.PROXIMITY_LABEL_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.PROXIMITY_LABEL_2)

        self.LIVE_LOCATION = QFrame(self.Proximity_Detection_Widget)
        self.LIVE_LOCATION.setObjectName(u"LIVE_LOCATION")
        self.LIVE_LOCATION.setFrameShape(QFrame.StyledPanel)
        self.LIVE_LOCATION.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.LIVE_LOCATION)

        self.stackedWidget.addWidget(self.Proximity_Detection_Widget)
        self.Connection_Widget = QWidget()
        self.Connection_Widget.setObjectName(u"Connection_Widget")
        self.horizontalLayout_7 = QHBoxLayout(self.Connection_Widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LEFT_CONNECTION = QFrame(self.Connection_Widget)
        self.LEFT_CONNECTION.setObjectName(u"LEFT_CONNECTION")
        sizePolicy1.setHeightForWidth(self.LEFT_CONNECTION.sizePolicy().hasHeightForWidth())
        self.LEFT_CONNECTION.setSizePolicy(sizePolicy1)
        self.LEFT_CONNECTION.setFrameShape(QFrame.StyledPanel)
        self.LEFT_CONNECTION.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.LEFT_CONNECTION)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.LEFT_TOP_2 = QFrame(self.LEFT_CONNECTION)
        self.LEFT_TOP_2.setObjectName(u"LEFT_TOP_2")
        self.LEFT_TOP_2.setFrameShape(QFrame.StyledPanel)
        self.LEFT_TOP_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.LEFT_TOP_2)
        self.formLayout.setObjectName(u"formLayout")
        self.connectIP = QPushButton(self.LEFT_TOP_2)
        self.connectIP.setObjectName(u"connectIP")
        self.connectIP.setMinimumSize(QSize(200, 30))
        self.connectIP.setMaximumSize(QSize(150, 16777215))
        self.connectIP.setFont(font)
        self.connectIP.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectIP.setContextMenuPolicy(Qt.PreventContextMenu)
        self.connectIP.setToolTipDuration(-8)
        self.connectIP.setLayoutDirection(Qt.LeftToRight)
        self.connectIP.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-wifi-signal-4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connectIP.setIcon(icon)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.connectIP)

        self.disconnectIP = QPushButton(self.LEFT_TOP_2)
        self.disconnectIP.setObjectName(u"disconnectIP")
        self.disconnectIP.setMinimumSize(QSize(200, 30))
        self.disconnectIP.setMaximumSize(QSize(150, 16777215))
        self.disconnectIP.setFont(font)
        self.disconnectIP.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnectIP.setContextMenuPolicy(Qt.PreventContextMenu)
        self.disconnectIP.setToolTipDuration(-8)
        self.disconnectIP.setLayoutDirection(Qt.LeftToRight)
        self.disconnectIP.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-wifi-signal-off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnectIP.setIcon(icon1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.disconnectIP)

        self.IP_ENTER = QLineEdit(self.LEFT_TOP_2)
        self.IP_ENTER.setObjectName(u"IP_ENTER")
        self.IP_ENTER.setMinimumSize(QSize(0, 30))
        self.IP_ENTER.setMaximumSize(QSize(350, 16777215))
        self.IP_ENTER.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.IP_ENTER)

        self.LEFT_TOP_TITLE = QLabel(self.LEFT_TOP_2)
        self.LEFT_TOP_TITLE.setObjectName(u"LEFT_TOP_TITLE")
        self.LEFT_TOP_TITLE.setMaximumSize(QSize(16777215, 20))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.LEFT_TOP_TITLE)


        self.verticalLayout_9.addWidget(self.LEFT_TOP_2)

        self.TERMINAL = QFrame(self.LEFT_CONNECTION)
        self.TERMINAL.setObjectName(u"TERMINAL")
        self.TERMINAL.setFrameShape(QFrame.StyledPanel)
        self.TERMINAL.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.TERMINAL)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.TERMINAL_LABEL = QLabel(self.TERMINAL)
        self.TERMINAL_LABEL.setObjectName(u"TERMINAL_LABEL")

        self.verticalLayout_11.addWidget(self.TERMINAL_LABEL)

        self.TERMINAL_PLAINTEXTEDIT = QPlainTextEdit(self.TERMINAL)
        self.TERMINAL_PLAINTEXTEDIT.setObjectName(u"TERMINAL_PLAINTEXTEDIT")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.TERMINAL_PLAINTEXTEDIT.sizePolicy().hasHeightForWidth())
        self.TERMINAL_PLAINTEXTEDIT.setSizePolicy(sizePolicy5)
        self.TERMINAL_PLAINTEXTEDIT.setMinimumSize(QSize(100, 200))
        self.TERMINAL_PLAINTEXTEDIT.setMaximumSize(QSize(500, 16777214))
        self.TERMINAL_PLAINTEXTEDIT.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.TERMINAL_PLAINTEXTEDIT.setFocusPolicy(Qt.NoFocus)
        self.TERMINAL_PLAINTEXTEDIT.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.TERMINAL_PLAINTEXTEDIT.setToolTipDuration(-3)
        self.TERMINAL_PLAINTEXTEDIT.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.TERMINAL_PLAINTEXTEDIT.setReadOnly(True)
        self.TERMINAL_PLAINTEXTEDIT.setBackgroundVisible(False)

        self.verticalLayout_11.addWidget(self.TERMINAL_PLAINTEXTEDIT)


        self.verticalLayout_9.addWidget(self.TERMINAL)


        self.horizontalLayout_7.addWidget(self.LEFT_CONNECTION)

        self.RIGHT_CONNECTION = QFrame(self.Connection_Widget)
        self.RIGHT_CONNECTION.setObjectName(u"RIGHT_CONNECTION")
        sizePolicy1.setHeightForWidth(self.RIGHT_CONNECTION.sizePolicy().hasHeightForWidth())
        self.RIGHT_CONNECTION.setSizePolicy(sizePolicy1)
        self.RIGHT_CONNECTION.setFocusPolicy(Qt.WheelFocus)
        self.RIGHT_CONNECTION.setFrameShape(QFrame.StyledPanel)
        self.RIGHT_CONNECTION.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.RIGHT_CONNECTION)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.RIGHT_CONNECTION_TITTLE = QLabel(self.RIGHT_CONNECTION)
        self.RIGHT_CONNECTION_TITTLE.setObjectName(u"RIGHT_CONNECTION_TITTLE")

        self.verticalLayout_12.addWidget(self.RIGHT_CONNECTION_TITTLE)

        self.IP = QFrame(self.RIGHT_CONNECTION)
        self.IP.setObjectName(u"IP")
        self.IP.setFrameShape(QFrame.StyledPanel)
        self.IP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.IP)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.IP_LABEL = QLabel(self.IP)
        self.IP_LABEL.setObjectName(u"IP_LABEL")
        self.IP_LABEL.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_10.addWidget(self.IP_LABEL)

        self.IP_Lcd = QLabel(self.IP)
        self.IP_Lcd.setObjectName(u"IP_Lcd")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.IP_Lcd.sizePolicy().hasHeightForWidth())
        self.IP_Lcd.setSizePolicy(sizePolicy6)
        self.IP_Lcd.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_10.addWidget(self.IP_Lcd)


        self.verticalLayout_12.addWidget(self.IP)

        self.TEMPERATURE = QFrame(self.RIGHT_CONNECTION)
        self.TEMPERATURE.setObjectName(u"TEMPERATURE")
        self.TEMPERATURE.setFrameShape(QFrame.StyledPanel)
        self.TEMPERATURE.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.TEMPERATURE)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TEMPEARTURE_LABEL = QLabel(self.TEMPERATURE)
        self.TEMPEARTURE_LABEL.setObjectName(u"TEMPEARTURE_LABEL")
        self.TEMPEARTURE_LABEL.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.TEMPEARTURE_LABEL)

        self.Temperature_Lcd = QLabel(self.TEMPERATURE)
        self.Temperature_Lcd.setObjectName(u"Temperature_Lcd")
        self.Temperature_Lcd.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.Temperature_Lcd)


        self.verticalLayout_12.addWidget(self.TEMPERATURE)

        self.MEMORY = QFrame(self.RIGHT_CONNECTION)
        self.MEMORY.setObjectName(u"MEMORY")
        self.MEMORY.setFrameShape(QFrame.StyledPanel)
        self.MEMORY.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.MEMORY)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.MEMORY_LABEL = QLabel(self.MEMORY)
        self.MEMORY_LABEL.setObjectName(u"MEMORY_LABEL")
        self.MEMORY_LABEL.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.MEMORY_LABEL)

        self.Memory_Lcd = QLabel(self.MEMORY)
        self.Memory_Lcd.setObjectName(u"Memory_Lcd")
        self.Memory_Lcd.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.Memory_Lcd)


        self.verticalLayout_12.addWidget(self.MEMORY)

        self.CPU = QFrame(self.RIGHT_CONNECTION)
        self.CPU.setObjectName(u"CPU")
        self.CPU.setMinimumSize(QSize(100, 0))
        self.CPU.setFrameShape(QFrame.StyledPanel)
        self.CPU.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.CPU)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.CPU_LABEL = QLabel(self.CPU)
        self.CPU_LABEL.setObjectName(u"CPU_LABEL")
        self.CPU_LABEL.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.CPU_LABEL)

        self.Cpu_Lcd = QLabel(self.CPU)
        self.Cpu_Lcd.setObjectName(u"Cpu_Lcd")
        self.Cpu_Lcd.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_9.addWidget(self.Cpu_Lcd)


        self.verticalLayout_12.addWidget(self.CPU)

        self.DISK = QFrame(self.RIGHT_CONNECTION)
        self.DISK.setObjectName(u"DISK")
        self.DISK.setFrameShape(QFrame.StyledPanel)
        self.DISK.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.DISK)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.DISK_LABEL = QLabel(self.DISK)
        self.DISK_LABEL.setObjectName(u"DISK_LABEL")
        self.DISK_LABEL.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_11.addWidget(self.DISK_LABEL)

        self.Disk_Lcd = QLabel(self.DISK)
        self.Disk_Lcd.setObjectName(u"Disk_Lcd")
        self.Disk_Lcd.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_11.addWidget(self.Disk_Lcd)


        self.verticalLayout_12.addWidget(self.DISK)


        self.horizontalLayout_7.addWidget(self.RIGHT_CONNECTION, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.Connection_Widget)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.Facial_Button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Location_Button.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.Connection_Button.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Bus Unit Monitoring System (TIE PROJECT DEMO)", None))
        self.Display_Tittle.setText(QCoreApplication.translate("MainWindow", u"Live Video", None))
        self.Video_Label.setText(QCoreApplication.translate("MainWindow", u"                                                 WAITING FOR VIDEO", None))
        self.Attendance_title.setText(QCoreApplication.translate("MainWindow", u"Attendance", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Arrival Time", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.PROXIMITY_LABEL_2.setText(QCoreApplication.translate("MainWindow", u"Live Location", None))
        self.connectIP.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.disconnectIP.setText(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
        self.IP_ENTER.setText("")
        self.IP_ENTER.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter IP address here: Example 192.168.0.20", None))
        self.LEFT_TOP_TITLE.setText(QCoreApplication.translate("MainWindow", u"Connect Bus Unit", None))
        self.TERMINAL_LABEL.setText(QCoreApplication.translate("MainWindow", u"TERMINAL", None))
        self.RIGHT_CONNECTION_TITTLE.setText(QCoreApplication.translate("MainWindow", u"Bus Unit Status", None))
        self.IP_LABEL.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.IP_Lcd.setText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.TEMPEARTURE_LABEL.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.Temperature_Lcd.setText(QCoreApplication.translate("MainWindow", u"temp", None))
        self.MEMORY_LABEL.setText(QCoreApplication.translate("MainWindow", u"Memory Usage", None))
        self.Memory_Lcd.setText(QCoreApplication.translate("MainWindow", u"memory", None))
        self.CPU_LABEL.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.Cpu_Lcd.setText(QCoreApplication.translate("MainWindow", u"cpu", None))
        self.DISK_LABEL.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.Disk_Lcd.setText(QCoreApplication.translate("MainWindow", u"disk", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By John Lbalunye and Emmanuel Achinga ", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.1", None))
    # retranslateUi

