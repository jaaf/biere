# Form implementation generated from reading ui file 'designer/phadjusterwidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Adjuster(object):
    def setupUi(self, Adjuster):
        Adjuster.setObjectName("Adjuster")
        Adjuster.resize(1103, 799)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Adjuster)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(Adjuster)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Adjuster)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupboxMaltsDiph = QtWidgets.QScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupboxMaltsDiph.sizePolicy().hasHeightForWidth())
        self.groupboxMaltsDiph.setSizePolicy(sizePolicy)
        self.groupboxMaltsDiph.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.groupboxMaltsDiph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.groupboxMaltsDiph.setWidgetResizable(True)
        self.groupboxMaltsDiph.setObjectName("groupboxMaltsDiph")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 735))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupboxMaltsDiph.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.groupboxMaltsDiph)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.groupBoxPhAdjust = QtWidgets.QGroupBox(Adjuster)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPhAdjust.sizePolicy().hasHeightForWidth())
        self.groupBoxPhAdjust.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBoxPhAdjust.setFont(font)
        self.groupBoxPhAdjust.setStyleSheet("")
        self.groupBoxPhAdjust.setTitle("")
        self.groupBoxPhAdjust.setObjectName("groupBoxPhAdjust")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxPhAdjust)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainCheckBox = QtWidgets.QCheckBox(self.groupBoxPhAdjust)
        self.mainCheckBox.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.mainCheckBox.setFont(font)
        self.mainCheckBox.setObjectName("mainCheckBox")
        self.verticalLayout_3.addWidget(self.mainCheckBox)
        self.controlGroupbox = QtWidgets.QGroupBox(self.groupBoxPhAdjust)
        self.controlGroupbox.setStyleSheet("")
        self.controlGroupbox.setTitle("")
        self.controlGroupbox.setObjectName("controlGroupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.controlGroupbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.controlGroupbox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelPhBefore = QtWidgets.QLabel(self.controlGroupbox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.labelPhBefore.setFont(font)
        self.labelPhBefore.setObjectName("labelPhBefore")
        self.horizontalLayout_6.addWidget(self.labelPhBefore)
        self.phBeforeEdit = QtWidgets.QLineEdit(self.controlGroupbox)
        self.phBeforeEdit.setMaximumSize(QtCore.QSize(48, 24))
        self.phBeforeEdit.setObjectName("phBeforeEdit")
        self.horizontalLayout_6.addWidget(self.phBeforeEdit)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.phTargetLabel = QtWidgets.QLabel(self.controlGroupbox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.phTargetLabel.setFont(font)
        self.phTargetLabel.setObjectName("phTargetLabel")
        self.horizontalLayout_7.addWidget(self.phTargetLabel)
        self.spinBox = QtWidgets.QDoubleSpinBox(self.controlGroupbox)
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.spinBox.setFont(font)
        self.spinBox.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.spinBox.setPrefix("")
        self.spinBox.setSuffix("")
        self.spinBox.setSingleStep(0.05)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_7.addWidget(self.spinBox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.acidAgentLabel = QtWidgets.QLabel(self.controlGroupbox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.acidAgentLabel.setFont(font)
        self.acidAgentLabel.setObjectName("acidAgentLabel")
        self.horizontalLayout_9.addWidget(self.acidAgentLabel)
        self.acidAgentCombo = QtWidgets.QComboBox(self.controlGroupbox)
        self.acidAgentCombo.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.acidAgentCombo.setFont(font)
        self.acidAgentCombo.setObjectName("acidAgentCombo")
        self.horizontalLayout_9.addWidget(self.acidAgentCombo)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout_11)
        self.line_2 = QtWidgets.QFrame(self.controlGroupbox)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.phAdjustMessageLabel = QtWidgets.QTextEdit(self.controlGroupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phAdjustMessageLabel.sizePolicy().hasHeightForWidth())
        self.phAdjustMessageLabel.setSizePolicy(sizePolicy)
        self.phAdjustMessageLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.phAdjustMessageLabel.setStyleSheet("color: red;")
        self.phAdjustMessageLabel.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.phAdjustMessageLabel.setReadOnly(True)
        self.phAdjustMessageLabel.setObjectName("phAdjustMessageLabel")
        self.verticalLayout_2.addWidget(self.phAdjustMessageLabel)
        self.line_3 = QtWidgets.QFrame(self.controlGroupbox)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.controlGroupbox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.spargeAdjustMessageLabel = QtWidgets.QTextEdit(self.controlGroupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spargeAdjustMessageLabel.sizePolicy().hasHeightForWidth())
        self.spargeAdjustMessageLabel.setSizePolicy(sizePolicy)
        self.spargeAdjustMessageLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.spargeAdjustMessageLabel.setStyleSheet("color: red;")
        self.spargeAdjustMessageLabel.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.spargeAdjustMessageLabel.setReadOnly(True)
        self.spargeAdjustMessageLabel.setObjectName("spargeAdjustMessageLabel")
        self.verticalLayout_2.addWidget(self.spargeAdjustMessageLabel)
        spacerItem1 = QtWidgets.QSpacerItem(504, 326, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.controlGroupbox)
        self.gridLayout.addWidget(self.groupBoxPhAdjust, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Adjuster)
        QtCore.QMetaObject.connectSlotsByName(Adjuster)

    def retranslateUi(self, Adjuster):
        _translate = QtCore.QCoreApplication.translate
        Adjuster.setWindowTitle(_translate("Adjuster", "Form"))
        self.label.setText(_translate("Adjuster", "DI pH et capacités tampon des malts utilisés"))
        self.mainCheckBox.setText(_translate("Adjuster", "CheckBox"))
        self.label_3.setText(_translate("Adjuster", "Ajustement du pH de l\'empâtage"))
        self.labelPhBefore.setText(_translate("Adjuster", "pH avant ajustement"))
        self.phTargetLabel.setText(_translate("Adjuster", "Cible de pH"))
        self.acidAgentLabel.setText(_translate("Adjuster", "Agent d\'acidification"))
        self.label_2.setText(_translate("Adjuster", "Ajustement du pH de l\'eau de rinçage"))
