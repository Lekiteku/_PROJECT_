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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"background-color: rgb(15, 15, 15);")
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
"	background-image: url(:/images/images/images/PyDracula.png);\n"
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
"	background-color: rgb(18"
                        "9, 147, 249);\n"
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
"	background-color: rgb("
                        "189, 147, 249);\n"
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
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
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
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
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
"	color: rgb"
                        "(255, 255, 255);\n"
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
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
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
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
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
"}\n"
""
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
"     su"
                        "bcontrol-origin: margin;\n"
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
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
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
"	subco"
                        "ntrol-position: top right;\n"
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
"    h"
                        "eight: 10px;\n"
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
"QCommandLi"
                        "nkButton {	\n"
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
"	background-color: rgb(57, 65, 80);\n"
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
        self.Big_App = QFrame(self.styleSheet)
        self.Big_App.setObjectName(u"Big_App")
        self.Big_App.setStyleSheet(u"")
        self.Big_App.setFrameShape(QFrame.NoFrame)
        self.Big_App.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.Big_App)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_Menu_Box = QFrame(self.Big_App)
        self.Left_Menu_Box.setObjectName(u"Left_Menu_Box")
        self.Left_Menu_Box.setMinimumSize(QSize(60, 0))
        self.Left_Menu_Box.setMaximumSize(QSize(60, 16777215))
        self.Left_Menu_Box.setStyleSheet(u"QPushButton{\n"
"                background-repeat: no-repeat;\n"
"                background-position: center center;\n"
"            }")
        self.Left_Menu_Box.setFrameShape(QFrame.NoFrame)
        self.Left_Menu_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Left_Menu_Box)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Logo = QFrame(self.Left_Menu_Box)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(0, 50))
        self.Logo.setMaximumSize(QSize(16777215, 50))
        self.Logo.setStyleSheet(u"")
        self.Logo.setFrameShape(QFrame.NoFrame)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.Logo_Icon = QFrame(self.Logo)
        self.Logo_Icon.setObjectName(u"Logo_Icon")
        self.Logo_Icon.setGeometry(QRect(10, 5, 42, 42))
        self.Logo_Icon.setMinimumSize(QSize(42, 42))
        self.Logo_Icon.setMaximumSize(QSize(42, 42))
        self.Logo_Icon.setFrameShape(QFrame.NoFrame)
        self.Logo_Icon.setFrameShadow(QFrame.Raised)
        self.Title_Left_Name_Label = QLabel(self.Logo)
        self.Title_Left_Name_Label.setObjectName(u"Title_Left_Name_Label")
        self.Title_Left_Name_Label.setGeometry(QRect(70, 8, 160, 20))
        self.Title_Left_Name_Label.setFont(font)
        self.Title_Left_Name_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Title_Left_Description_Label = QLabel(self.Logo)
        self.Title_Left_Description_Label.setObjectName(u"Title_Left_Description_Label")
        self.Title_Left_Description_Label.setGeometry(QRect(70, 27, 160, 16))
        self.Title_Left_Description_Label.setMaximumSize(QSize(16777215, 16))
        self.Title_Left_Description_Label.setFont(font)
        self.Title_Left_Description_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.Logo)

        self.Menu = QFrame(self.Left_Menu_Box)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"")
        self.Menu.setFrameShape(QFrame.NoFrame)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.Menu)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Menu = QFrame(self.Menu)
        self.Top_Menu.setObjectName(u"Top_Menu")
        self.Top_Menu.setMaximumSize(QSize(16777215, 45))
        self.Top_Menu.setFrameShape(QFrame.NoFrame)
        self.Top_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Top_Menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Toggle_Top_Menu_Button = QPushButton(self.Top_Menu)
        self.Toggle_Top_Menu_Button.setObjectName(u"Toggle_Top_Menu_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Toggle_Top_Menu_Button.sizePolicy().hasHeightForWidth())
        self.Toggle_Top_Menu_Button.setSizePolicy(sizePolicy)
        self.Toggle_Top_Menu_Button.setMinimumSize(QSize(0, 45))
        self.Toggle_Top_Menu_Button.setFont(font)
        self.Toggle_Top_Menu_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Toggle_Top_Menu_Button.setLayoutDirection(Qt.LeftToRight)
        self.Toggle_Top_Menu_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.Toggle_Top_Menu_Button)


        self.verticalMenuLayout.addWidget(self.Top_Menu)

        self.Middle_Menu = QFrame(self.Menu)
        self.Middle_Menu.setObjectName(u"Middle_Menu")
        self.Middle_Menu.setFrameShape(QFrame.NoFrame)
        self.Middle_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Middle_Menu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Facial_Button = QPushButton(self.Middle_Menu)
        self.Facial_Button.setObjectName(u"Facial_Button")
        sizePolicy.setHeightForWidth(self.Facial_Button.sizePolicy().hasHeightForWidth())
        self.Facial_Button.setSizePolicy(sizePolicy)
        self.Facial_Button.setMinimumSize(QSize(0, 45))
        self.Facial_Button.setFont(font)
        self.Facial_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Facial_Button.setLayoutDirection(Qt.LeftToRight)
        self.Facial_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);\n"
"")

        self.verticalLayout_8.addWidget(self.Facial_Button)

        self.Location_Button = QPushButton(self.Middle_Menu)
        self.Location_Button.setObjectName(u"Location_Button")
        sizePolicy.setHeightForWidth(self.Location_Button.sizePolicy().hasHeightForWidth())
        self.Location_Button.setSizePolicy(sizePolicy)
        self.Location_Button.setMinimumSize(QSize(0, 45))
        self.Location_Button.setFont(font)
        self.Location_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Location_Button.setLayoutDirection(Qt.LeftToRight)
        self.Location_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.Location_Button)

        self.Connection_Button = QPushButton(self.Middle_Menu)
        self.Connection_Button.setObjectName(u"Connection_Button")
        sizePolicy.setHeightForWidth(self.Connection_Button.sizePolicy().hasHeightForWidth())
        self.Connection_Button.setSizePolicy(sizePolicy)
        self.Connection_Button.setMinimumSize(QSize(0, 45))
        self.Connection_Button.setFont(font)
        self.Connection_Button.setCursor(QCursor(Qt.ArrowCursor))
        self.Connection_Button.setLayoutDirection(Qt.LeftToRight)
        self.Connection_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.Connection_Button)

        self.Registration_Button = QPushButton(self.Middle_Menu)
        self.Registration_Button.setObjectName(u"Registration_Button")
        sizePolicy.setHeightForWidth(self.Registration_Button.sizePolicy().hasHeightForWidth())
        self.Registration_Button.setSizePolicy(sizePolicy)
        self.Registration_Button.setMinimumSize(QSize(0, 45))
        self.Registration_Button.setFont(font)
        self.Registration_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Registration_Button.setLayoutDirection(Qt.LeftToRight)
        self.Registration_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.Registration_Button)

        self.Exit_Button = QPushButton(self.Middle_Menu)
        self.Exit_Button.setObjectName(u"Exit_Button")
        sizePolicy.setHeightForWidth(self.Exit_Button.sizePolicy().hasHeightForWidth())
        self.Exit_Button.setSizePolicy(sizePolicy)
        self.Exit_Button.setMinimumSize(QSize(0, 45))
        self.Exit_Button.setFont(font)
        self.Exit_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Exit_Button.setLayoutDirection(Qt.LeftToRight)
        self.Exit_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.Exit_Button)


        self.verticalMenuLayout.addWidget(self.Middle_Menu, 0, Qt.AlignTop)

        self.Bottom_Menu = QFrame(self.Menu)
        self.Bottom_Menu.setObjectName(u"Bottom_Menu")
        self.Bottom_Menu.setFrameShape(QFrame.NoFrame)
        self.Bottom_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Bottom_Menu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Toggle_Bottom_Menu_Button = QPushButton(self.Bottom_Menu)
        self.Toggle_Bottom_Menu_Button.setObjectName(u"Toggle_Bottom_Menu_Button")
        sizePolicy.setHeightForWidth(self.Toggle_Bottom_Menu_Button.sizePolicy().hasHeightForWidth())
        self.Toggle_Bottom_Menu_Button.setSizePolicy(sizePolicy)
        self.Toggle_Bottom_Menu_Button.setMinimumSize(QSize(0, 45))
        self.Toggle_Bottom_Menu_Button.setFont(font)
        self.Toggle_Bottom_Menu_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Toggle_Bottom_Menu_Button.setLayoutDirection(Qt.LeftToRight)
        self.Toggle_Bottom_Menu_Button.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.Toggle_Bottom_Menu_Button)


        self.verticalMenuLayout.addWidget(self.Bottom_Menu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.Menu)


        self.appLayout.addWidget(self.Left_Menu_Box)

        self.Extra_Left_Menu_Box = QFrame(self.Big_App)
        self.Extra_Left_Menu_Box.setObjectName(u"Extra_Left_Menu_Box")
        self.Extra_Left_Menu_Box.setMinimumSize(QSize(0, 0))
        self.Extra_Left_Menu_Box.setMaximumSize(QSize(0, 16777215))
        self.Extra_Left_Menu_Box.setFrameShape(QFrame.NoFrame)
        self.Extra_Left_Menu_Box.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.Extra_Left_Menu_Box)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.Extra_Top_Box = QFrame(self.Extra_Left_Menu_Box)
        self.Extra_Top_Box.setObjectName(u"Extra_Top_Box")
        self.Extra_Top_Box.setMinimumSize(QSize(0, 50))
        self.Extra_Top_Box.setMaximumSize(QSize(16777215, 50))
        self.Extra_Top_Box.setFrameShape(QFrame.NoFrame)
        self.Extra_Top_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Extra_Top_Box)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.extraColumLayout.addWidget(self.Extra_Top_Box)

        self.Extra_Buttom_Content_Box = QFrame(self.Extra_Left_Menu_Box)
        self.Extra_Buttom_Content_Box.setObjectName(u"Extra_Buttom_Content_Box")
        self.Extra_Buttom_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Extra_Buttom_Content_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Extra_Buttom_Content_Box)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.extraColumLayout.addWidget(self.Extra_Buttom_Content_Box)


        self.appLayout.addWidget(self.Extra_Left_Menu_Box)

        self.Content_Box = QFrame(self.Big_App)
        self.Content_Box.setObjectName(u"Content_Box")
        self.Content_Box.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.Content_Box.setFrameShape(QFrame.NoFrame)
        self.Content_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Content_Box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Top_Content_Box = QFrame(self.Content_Box)
        self.Top_Content_Box.setObjectName(u"Top_Content_Box")
        self.Top_Content_Box.setMinimumSize(QSize(0, 50))
        self.Top_Content_Box.setMaximumSize(QSize(16777215, 50))
        self.Top_Content_Box.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Top_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Top_Content_Box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Content_Box)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.Title_Top_Content_Box = QFrame(self.Top_Content_Box)
        self.Title_Top_Content_Box.setObjectName(u"Title_Top_Content_Box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Title_Top_Content_Box.sizePolicy().hasHeightForWidth())
        self.Title_Top_Content_Box.setSizePolicy(sizePolicy1)
        self.Title_Top_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Title_Top_Content_Box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Title_Top_Content_Box)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Title_Top_Content_Box_Label = QLabel(self.Title_Top_Content_Box)
        self.Title_Top_Content_Box_Label.setObjectName(u"Title_Top_Content_Box_Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Title_Top_Content_Box_Label.sizePolicy().hasHeightForWidth())
        self.Title_Top_Content_Box_Label.setSizePolicy(sizePolicy2)
        self.Title_Top_Content_Box_Label.setMaximumSize(QSize(16777215, 45))
        self.Title_Top_Content_Box_Label.setFont(font)
        self.Title_Top_Content_Box_Label.setStyleSheet(u"")
        self.Title_Top_Content_Box_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Title_Top_Content_Box_Label)


        self.horizontalLayout.addWidget(self.Title_Top_Content_Box)


        self.verticalLayout_2.addWidget(self.Top_Content_Box)

        self.Buttom_Content_Box = QFrame(self.Content_Box)
        self.Buttom_Content_Box.setObjectName(u"Buttom_Content_Box")
        self.Buttom_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Buttom_Content_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Buttom_Content_Box)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Content = QFrame(self.Buttom_Content_Box)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Main_Content_Box = QFrame(self.Content)
        self.Main_Content_Box.setObjectName(u"Main_Content_Box")
        self.Main_Content_Box.setStyleSheet(u"")
        self.Main_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Main_Content_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Main_Content_Box)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.Stacked_Widget = QStackedWidget(self.Main_Content_Box)
        self.Stacked_Widget.setObjectName(u"Stacked_Widget")
        self.Stacked_Widget.setMaximumSize(QSize(16777215, 16777215))
        self.Stacked_Widget.setCursor(QCursor(Qt.ArrowCursor))
        self.Stacked_Widget.setTabletTracking(True)
        self.Stacked_Widget.setStyleSheet(u"background: transparent;")
        self.Facial_Recognition_Stacked_Widget = QWidget()
        self.Facial_Recognition_Stacked_Widget.setObjectName(u"Facial_Recognition_Stacked_Widget")
        self.Facial_Recognition_Stacked_Widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.Facial_Recognition_Stacked_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Facial_FR_Box = QFrame(self.Facial_Recognition_Stacked_Widget)
        self.Facial_FR_Box.setObjectName(u"Facial_FR_Box")
        self.Facial_FR_Box.setFrameShape(QFrame.StyledPanel)
        self.Facial_FR_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Facial_FR_Box)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Facial_Title_lable = QLabel(self.Facial_FR_Box)
        self.Facial_Title_lable.setObjectName(u"Facial_Title_lable")
        self.Facial_Title_lable.setMaximumSize(QSize(16777215, 20))
        self.Facial_Title_lable.setFont(font)
        self.Facial_Title_lable.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.Facial_Title_lable)

        self.Dispay_Facial_Box = QFrame(self.Facial_FR_Box)
        self.Dispay_Facial_Box.setObjectName(u"Dispay_Facial_Box")
        self.Dispay_Facial_Box.setMinimumSize(QSize(0, 0))
        self.Dispay_Facial_Box.setMaximumSize(QSize(16777215, 16777215))
        self.Dispay_Facial_Box.setCursor(QCursor(Qt.UpArrowCursor))
        self.Dispay_Facial_Box.setFrameShape(QFrame.StyledPanel)
        self.Dispay_Facial_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Dispay_Facial_Box)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Display = QLabel(self.Dispay_Facial_Box)
        self.Display.setObjectName(u"Display")
        self.Display.setMinimumSize(QSize(640, 480))

        self.verticalLayout_13.addWidget(self.Display)


        self.verticalLayout_10.addWidget(self.Dispay_Facial_Box)

        self.Extra_Infor_Facial_Box = QFrame(self.Facial_FR_Box)
        self.Extra_Infor_Facial_Box.setObjectName(u"Extra_Infor_Facial_Box")
        self.Extra_Infor_Facial_Box.setFrameShape(QFrame.StyledPanel)
        self.Extra_Infor_Facial_Box.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.Extra_Infor_Facial_Box)


        self.horizontalLayout_2.addWidget(self.Facial_FR_Box)

        self.Attendance_FR_Box = QFrame(self.Facial_Recognition_Stacked_Widget)
        self.Attendance_FR_Box.setObjectName(u"Attendance_FR_Box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Attendance_FR_Box.sizePolicy().hasHeightForWidth())
        self.Attendance_FR_Box.setSizePolicy(sizePolicy3)
        self.Attendance_FR_Box.setMaximumSize(QSize(1134, 16777215))
        self.Attendance_FR_Box.setFrameShape(QFrame.StyledPanel)
        self.Attendance_FR_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Attendance_FR_Box)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Attendance_Label = QLabel(self.Attendance_FR_Box)
        self.Attendance_Label.setObjectName(u"Attendance_Label")
        self.Attendance_Label.setFont(font)
        self.Attendance_Label.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.Attendance_Label)

        self.Attendance_Table = QTableWidget(self.Attendance_FR_Box)
        if (self.Attendance_Table.columnCount() < 3):
            self.Attendance_Table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Attendance_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Attendance_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Attendance_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.Attendance_Table.rowCount() < 16):
            self.Attendance_Table.setRowCount(16)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.Attendance_Table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Attendance_Table.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Attendance_Table.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Attendance_Table.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Attendance_Table.setItem(0, 2, __qtablewidgetitem21)
        self.Attendance_Table.setObjectName(u"Attendance_Table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Attendance_Table.sizePolicy().hasHeightForWidth())
        self.Attendance_Table.setSizePolicy(sizePolicy4)
        self.Attendance_Table.setMaximumSize(QSize(16777215, 706))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(38, 38, 38, 255))
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
        self.Attendance_Table.setPalette(palette)
        self.Attendance_Table.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.Attendance_Table.setContextMenuPolicy(Qt.PreventContextMenu)
        self.Attendance_Table.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.Attendance_Table.setFrameShape(QFrame.NoFrame)
        self.Attendance_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Attendance_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Attendance_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Attendance_Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Attendance_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Attendance_Table.setShowGrid(True)
        self.Attendance_Table.setGridStyle(Qt.SolidLine)
        self.Attendance_Table.setSortingEnabled(False)
        self.Attendance_Table.horizontalHeader().setVisible(False)
        self.Attendance_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Attendance_Table.horizontalHeader().setDefaultSectionSize(200)
        self.Attendance_Table.horizontalHeader().setStretchLastSection(True)
        self.Attendance_Table.verticalHeader().setVisible(False)
        self.Attendance_Table.verticalHeader().setCascadingSectionResizes(False)
        self.Attendance_Table.verticalHeader().setHighlightSections(False)
        self.Attendance_Table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.Attendance_Table)


        self.horizontalLayout_2.addWidget(self.Attendance_FR_Box)

        self.Stacked_Widget.addWidget(self.Facial_Recognition_Stacked_Widget)
        self.Proximity_Detection_Stacked_Widget = QWidget()
        self.Proximity_Detection_Stacked_Widget.setObjectName(u"Proximity_Detection_Stacked_Widget")
        self.Proximity_Detection_Stacked_Widget.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.Proximity_Detection_Stacked_Widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.Proximity_Detection_Stacked_Widget)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.Proximity_Detection_Stacked_Widget)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 364, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.Proximity_Detection_Stacked_Widget)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font1);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem43)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy5)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 0))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette1)
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

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.Stacked_Widget.addWidget(self.Proximity_Detection_Stacked_Widget)
        self.Connection_Stacked_Widget = QWidget()
        self.Connection_Stacked_Widget.setObjectName(u"Connection_Stacked_Widget")
        self.verticalLayout_20 = QVBoxLayout(self.Connection_Stacked_Widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.Connection_Stacked_Widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.Stacked_Widget.addWidget(self.Connection_Stacked_Widget)

        self.verticalLayout_15.addWidget(self.Stacked_Widget)


        self.horizontalLayout_4.addWidget(self.Main_Content_Box)

        self.Extra_Right_Content_Box = QFrame(self.Content)
        self.Extra_Right_Content_Box.setObjectName(u"Extra_Right_Content_Box")
        self.Extra_Right_Content_Box.setMinimumSize(QSize(0, 0))
        self.Extra_Right_Content_Box.setMaximumSize(QSize(0, 16777215))
        self.Extra_Right_Content_Box.setFrameShape(QFrame.NoFrame)
        self.Extra_Right_Content_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Extra_Right_Content_Box)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.Extra_Right_Content_Box)


        self.verticalLayout_6.addWidget(self.Content)

        self.Buttom_Content = QFrame(self.Buttom_Content_Box)
        self.Buttom_Content.setObjectName(u"Buttom_Content")
        self.Buttom_Content.setMinimumSize(QSize(0, 22))
        self.Buttom_Content.setMaximumSize(QSize(16777215, 22))
        self.Buttom_Content.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.Buttom_Content.setFrameShape(QFrame.NoFrame)
        self.Buttom_Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Buttom_Content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Credits_Label = QLabel(self.Buttom_Content)
        self.Credits_Label.setObjectName(u"Credits_Label")
        self.Credits_Label.setMaximumSize(QSize(16777215, 16))
        self.Credits_Label.setFont(font)
        self.Credits_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.Credits_Label)

        self.Version = QLabel(self.Buttom_Content)
        self.Version.setObjectName(u"Version")
        self.Version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.Version)

        self.Frame_Size_Grip = QFrame(self.Buttom_Content)
        self.Frame_Size_Grip.setObjectName(u"Frame_Size_Grip")
        self.Frame_Size_Grip.setMinimumSize(QSize(20, 0))
        self.Frame_Size_Grip.setMaximumSize(QSize(20, 16777215))
        self.Frame_Size_Grip.setFrameShape(QFrame.NoFrame)
        self.Frame_Size_Grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Frame_Size_Grip)


        self.verticalLayout_6.addWidget(self.Buttom_Content)


        self.verticalLayout_2.addWidget(self.Buttom_Content_Box)


        self.appLayout.addWidget(self.Content_Box)


        self.appMargins.addWidget(self.Big_App)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.Stacked_Widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title_Left_Name_Label.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.Title_Left_Description_Label.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.Toggle_Top_Menu_Button.setText("")
        self.Facial_Button.setText("")
        self.Location_Button.setText("")
        self.Connection_Button.setText("")
        self.Registration_Button.setText("")
        self.Exit_Button.setText("")
        self.Toggle_Bottom_Menu_Button.setText("")
        self.Title_Top_Content_Box_Label.setText(QCoreApplication.translate("MainWindow", u"   School Bus Monitiring System (TIE PROJECT DEMO) ", None))
        self.Facial_Title_lable.setText(QCoreApplication.translate("MainWindow", u"RASPERRY PI LIVE FEED", None))
        self.Display.setText(QCoreApplication.translate("MainWindow", u"                                                                       Video Display", None))
        self.Attendance_Label.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        ___qtablewidgetitem = self.Attendance_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.Attendance_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.Attendance_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.Attendance_Table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.Attendance_Table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.Attendance_Table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.Attendance_Table.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.Attendance_Table.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.Attendance_Table.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.Attendance_Table.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.Attendance_Table.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.Attendance_Table.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.Attendance_Table.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.Attendance_Table.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.Attendance_Table.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.Attendance_Table.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.Attendance_Table.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.Attendance_Table.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.Attendance_Table.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.Attendance_Table.isSortingEnabled()
        self.Attendance_Table.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.Attendance_Table.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem20 = self.Attendance_Table.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem21 = self.Attendance_Table.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Arrival Name", None));
        self.Attendance_Table.setSortingEnabled(__sortingEnabled)

        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem41 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem42 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem43 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.Credits_Label.setText(QCoreApplication.translate("MainWindow", u"By : Emmanuel Achinga and John Lbalunye", None))
        self.Version.setText(QCoreApplication.translate("MainWindow", u"v1.0.1", None))
    # retranslateUi

