# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataFitting.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 692)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 640))
        MainWindow.setStyleSheet("#MainWindow{\n"
"}\n"
"\n"
"#centralWidget{\n"
"    background: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QCheckBox{\n"
"        color:rgb(186, 184, 172);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color:rgb(186, 184, 172);\n"
"    background:rgb(80, 80, 80);\n"
"    border: 1px black;\n"
"    selection-background-color:rgb(208, 146, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:rgb(186, 184, 172);\n"
"    background:rgb(40, 40, 40);\n"
"    border-color:rgb(0, 0, 0);\n"
"    selection-background-color:rgb(208, 146, 0);\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color:rgb(186, 184, 172);\n"
"    background:rgb(40, 40, 40);\n"
"    border-color:rgb(0, 0, 0);\n"
"    selection-background-color:rgb(208, 146, 0);\n"
"}\n"
"\n"
"QComboBox{\n"
"    color:rgb(186, 184, 172);\n"
"    background:rgb(80, 80, 80);\n"
"    selection-background-color: rgb(208, 146, 0);\n"
"}\n"
"\n"
"#CB_D2{\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border:0px;\n"
"    color:rgb(186, 184, 172);\n"
"    background:rgb(80, 80, 80);\n"
"    selection-background-color: rgb(208, 146, 0);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    color:rgb(208, 146, 0);\n"
"}\n"
"\n"
"#LBL_ApplicationSlogan{\n"
"    color:rgb(186, 184, 172);\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"]\n"
"{\n"
"\n"
"    color:rgb(208, 146, 0);\n"
"}\n"
"\n"
"Line{\n"
"    color:rgb(208, 146, 0);\n"
"    background-color: rgb(100, 0, 0);\n"
"    alternate-background-color: rgb(0, 100, 0);\n"
"    border-color: rgb(0, 0,100);\n"
"    gridline-color: rgb(0, 200, 0);\n"
"    selection-color: rgb(200, 0, 0);\n"
"    selection-background-color: rgb(0, 0, 200);\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(104, 80))
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PB_Dir = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Dir.sizePolicy().hasHeightForWidth())
        self.PB_Dir.setSizePolicy(sizePolicy)
        self.PB_Dir.setObjectName("PB_Dir")
        self.horizontalLayout_3.addWidget(self.PB_Dir)
        self.LE_Dir = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_Dir.sizePolicy().hasHeightForWidth())
        self.LE_Dir.setSizePolicy(sizePolicy)
        self.LE_Dir.setMinimumSize(QtCore.QSize(200, 0))
        self.LE_Dir.setObjectName("LE_Dir")
        self.horizontalLayout_3.addWidget(self.LE_Dir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.PB_Dir_Load = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Dir_Load.sizePolicy().hasHeightForWidth())
        self.PB_Dir_Load.setSizePolicy(sizePolicy)
        self.PB_Dir_Load.setObjectName("PB_Dir_Load")
        self.verticalLayout_2.addWidget(self.PB_Dir_Load)
        self.CB_Files = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CB_Files.sizePolicy().hasHeightForWidth())
        self.CB_Files.setSizePolicy(sizePolicy)
        self.CB_Files.setObjectName("CB_Files")
        self.verticalLayout_2.addWidget(self.CB_Files)
        self.PB_File = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_File.sizePolicy().hasHeightForWidth())
        self.PB_File.setSizePolicy(sizePolicy)
        self.PB_File.setObjectName("PB_File")
        self.verticalLayout_2.addWidget(self.PB_File)
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LBL_Mode = QtWidgets.QLabel(self.centralWidget)
        self.LBL_Mode.setObjectName("LBL_Mode")
        self.horizontalLayout_4.addWidget(self.LBL_Mode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.RB_Mode_MDC = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Mode_MDC.setObjectName("RB_Mode_MDC")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.RB_Mode_MDC)
        self.horizontalLayout_4.addWidget(self.RB_Mode_MDC)
        self.RB_Mode_EDC = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Mode_EDC.setObjectName("RB_Mode_EDC")
        self.buttonGroup.addButton(self.RB_Mode_EDC)
        self.horizontalLayout_4.addWidget(self.RB_Mode_EDC)
        self.RB_Mode_Free = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Mode_Free.setObjectName("RB_Mode_Free")
        self.buttonGroup.addButton(self.RB_Mode_Free)
        self.horizontalLayout_4.addWidget(self.RB_Mode_Free)
        self.PB_DC_Editing = QtWidgets.QPushButton(self.centralWidget)
        self.PB_DC_Editing.setObjectName("PB_DC_Editing")
        self.horizontalLayout_4.addWidget(self.PB_DC_Editing)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LBL_Fit = QtWidgets.QLabel(self.centralWidget)
        self.LBL_Fit.setObjectName("LBL_Fit")
        self.horizontalLayout_5.addWidget(self.LBL_Fit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.RB_Fit_Linear = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Fit_Linear.setObjectName("RB_Fit_Linear")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.RB_Fit_Linear)
        self.horizontalLayout_5.addWidget(self.RB_Fit_Linear)
        self.RB_Fit_Quadratic = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Fit_Quadratic.setObjectName("RB_Fit_Quadratic")
        self.buttonGroup_2.addButton(self.RB_Fit_Quadratic)
        self.horizontalLayout_5.addWidget(self.RB_Fit_Quadratic)
        self.RB_Fit_Mexican = QtWidgets.QRadioButton(self.centralWidget)
        self.RB_Fit_Mexican.setObjectName("RB_Fit_Mexican")
        self.buttonGroup_2.addButton(self.RB_Fit_Mexican)
        self.horizontalLayout_5.addWidget(self.RB_Fit_Mexican)
        self.PB_Fit_ARPES = QtWidgets.QPushButton(self.centralWidget)
        self.PB_Fit_ARPES.setObjectName("PB_Fit_ARPES")
        self.horizontalLayout_5.addWidget(self.PB_Fit_ARPES)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.LE_Update_Bandfit = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_Update_Bandfit.sizePolicy().hasHeightForWidth())
        self.LE_Update_Bandfit.setSizePolicy(sizePolicy)
        self.LE_Update_Bandfit.setObjectName("LE_Update_Bandfit")
        self.horizontalLayout_6.addWidget(self.LE_Update_Bandfit)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.PB_Update_Bandfit = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Update_Bandfit.sizePolicy().hasHeightForWidth())
        self.PB_Update_Bandfit.setSizePolicy(sizePolicy)
        self.PB_Update_Bandfit.setObjectName("PB_Update_Bandfit")
        self.horizontalLayout_7.addWidget(self.PB_Update_Bandfit)
        self.LBL_Fitfunc = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_Fitfunc.sizePolicy().hasHeightForWidth())
        self.LBL_Fitfunc.setSizePolicy(sizePolicy)
        self.LBL_Fitfunc.setObjectName("LBL_Fitfunc")
        self.horizontalLayout_7.addWidget(self.LBL_Fitfunc)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.LBL_ARPES_Output = QtWidgets.QLabel(self.centralWidget)
        self.LBL_ARPES_Output.setObjectName("LBL_ARPES_Output")
        self.verticalLayout_2.addWidget(self.LBL_ARPES_Output)
        self.TE_ARPES_output = QtWidgets.QTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TE_ARPES_output.sizePolicy().hasHeightForWidth())
        self.TE_ARPES_output.setSizePolicy(sizePolicy)
        self.TE_ARPES_output.setReadOnly(True)
        self.TE_ARPES_output.setObjectName("TE_ARPES_output")
        self.verticalLayout_2.addWidget(self.TE_ARPES_output)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.WDGT_ARPES = MPL_WIDGET(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WDGT_ARPES.sizePolicy().hasHeightForWidth())
        self.WDGT_ARPES.setSizePolicy(sizePolicy)
        self.WDGT_ARPES.setMinimumSize(QtCore.QSize(500, 300))
        self.WDGT_ARPES.setObjectName("WDGT_ARPES")
        self.horizontalLayout.addWidget(self.WDGT_ARPES)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LBL_ProfFit = QtWidgets.QLabel(self.centralWidget)
        self.LBL_ProfFit.setObjectName("LBL_ProfFit")
        self.verticalLayout_3.addWidget(self.LBL_ProfFit)
        self.CB_DCFitfunction = QtWidgets.QComboBox(self.centralWidget)
        self.CB_DCFitfunction.setObjectName("CB_DCFitfunction")
        self.verticalLayout_3.addWidget(self.CB_DCFitfunction)
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.LE_Parameters = QtWidgets.QLineEdit(self.centralWidget)
        self.LE_Parameters.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_Parameters.sizePolicy().hasHeightForWidth())
        self.LE_Parameters.setSizePolicy(sizePolicy)
        self.LE_Parameters.setMinimumSize(QtCore.QSize(150, 0))
        self.LE_Parameters.setObjectName("LE_Parameters")
        self.verticalLayout_3.addWidget(self.LE_Parameters)
        self.LBL_Parameters = QtWidgets.QLabel(self.centralWidget)
        self.LBL_Parameters.setObjectName("LBL_Parameters")
        self.verticalLayout_3.addWidget(self.LBL_Parameters)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.PB_Update = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Update.sizePolicy().hasHeightForWidth())
        self.PB_Update.setSizePolicy(sizePolicy)
        self.PB_Update.setObjectName("PB_Update")
        self.horizontalLayout_9.addWidget(self.PB_Update)
        self.ChB_Estimate_Params_Profile = QtWidgets.QCheckBox(self.centralWidget)
        self.ChB_Estimate_Params_Profile.setObjectName("ChB_Estimate_Params_Profile")
        self.horizontalLayout_9.addWidget(self.ChB_Estimate_Params_Profile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.PB_FitProf = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_FitProf.sizePolicy().hasHeightForWidth())
        self.PB_FitProf.setSizePolicy(sizePolicy)
        self.PB_FitProf.setObjectName("PB_FitProf")
        self.horizontalLayout_8.addWidget(self.PB_FitProf)
        self.PB_Profile_Editing = QtWidgets.QPushButton(self.centralWidget)
        self.PB_Profile_Editing.setObjectName("PB_Profile_Editing")
        self.horizontalLayout_8.addWidget(self.PB_Profile_Editing)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.PB_P2A = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_P2A.sizePolicy().hasHeightForWidth())
        self.PB_P2A.setSizePolicy(sizePolicy)
        self.PB_P2A.setObjectName("PB_P2A")
        self.verticalLayout_3.addWidget(self.PB_P2A)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.WDGT_Profile = MPL_WIDGET(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WDGT_Profile.sizePolicy().hasHeightForWidth())
        self.WDGT_Profile.setSizePolicy(sizePolicy)
        self.WDGT_Profile.setMinimumSize(QtCore.QSize(500, 250))
        self.WDGT_Profile.setMaximumSize(QtCore.QSize(16777215, 200))
        self.WDGT_Profile.setObjectName("WDGT_Profile")
        self.horizontalLayout_2.addWidget(self.WDGT_Profile)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Calibration = QtWidgets.QAction(MainWindow)
        self.actionLoad_Calibration.setObjectName("actionLoad_Calibration")
        self.actionSet_Standard_Calibration = QtWidgets.QAction(MainWindow)
        self.actionSet_Standard_Calibration.setObjectName("actionSet_Standard_Calibration")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyMass"))
        self.PB_Dir.setText(_translate("MainWindow", "Directory"))
        self.LE_Dir.setText(_translate("MainWindow", "Filelocation"))
        self.PB_Dir_Load.setText(_translate("MainWindow", "Load Files"))
        self.PB_File.setText(_translate("MainWindow", "Load"))
        self.LBL_Mode.setText(_translate("MainWindow", "Mode"))
        self.RB_Mode_MDC.setText(_translate("MainWindow", "MDC"))
        self.RB_Mode_EDC.setText(_translate("MainWindow", "EDC"))
        self.RB_Mode_Free.setText(_translate("MainWindow", "Free"))
        self.PB_DC_Editing.setText(_translate("MainWindow", "Enable Editing"))
        self.LBL_Fit.setText(_translate("MainWindow", "Fittype (Band)"))
        self.RB_Fit_Linear.setText(_translate("MainWindow", "Linear"))
        self.RB_Fit_Quadratic.setText(_translate("MainWindow", "Quadratic"))
        self.RB_Fit_Mexican.setText(_translate("MainWindow", "Mexican"))
        self.PB_Fit_ARPES.setText(_translate("MainWindow", "Fit"))
        self.label_2.setText(_translate("MainWindow", "Start Parameters"))
        self.LE_Update_Bandfit.setText(_translate("MainWindow", "Enter Parameters"))
        self.PB_Update_Bandfit.setText(_translate("MainWindow", "Update"))
        self.LBL_Fitfunc.setText(_translate("MainWindow", "TextLabel"))
        self.LBL_ARPES_Output.setText(_translate("MainWindow", "Output"))
        self.LBL_ProfFit.setText(_translate("MainWindow", "Fit function"))
        self.label.setText(_translate("MainWindow", "Start Parameters"))
        self.LE_Parameters.setText(_translate("MainWindow", "Enter Parameters"))
        self.LBL_Parameters.setText(_translate("MainWindow", "TextLabel"))
        self.PB_Update.setText(_translate("MainWindow", "Update"))
        self.ChB_Estimate_Params_Profile.setToolTip(_translate("MainWindow", "Estimate the Fit parameters between left and right border"))
        self.ChB_Estimate_Params_Profile.setText(_translate("MainWindow", "Estimate"))
        self.PB_FitProf.setText(_translate("MainWindow", "Fit Profile"))
        self.PB_Profile_Editing.setText(_translate("MainWindow", "Enable Editing"))
        self.PB_P2A.setText(_translate("MainWindow", "Peak 2 ARPES"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Calibration"))
        self.actionLoad_Calibration.setText(_translate("MainWindow", "Load Calibration"))
        self.actionSet_Standard_Calibration.setText(_translate("MainWindow", "Set Standard Calibration"))


from mplwidget import MPL_WIDGET


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
