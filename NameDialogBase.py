# Form implementation generated from reading ui file 'designer/namedialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 293)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.introEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.introEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.introEdit.setStyleSheet("background-color:transparent; border:none; ")
        self.introEdit.setObjectName("introEdit")
        self.verticalLayout_2.addWidget(self.introEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.messageEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.messageEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.messageEdit.setStyleSheet("background-color:transparent; border:none; color: red;")
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout_2.addWidget(self.messageEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tryButton = QtWidgets.QPushButton(parent=Dialog)
        self.tryButton.setObjectName("tryButton")
        self.horizontalLayout.addWidget(self.tryButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(parent=Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 121, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choisir un nom"))
        self.label.setText(_translate("Dialog", "Nom à tester"))
        self.tryButton.setText(_translate("Dialog", "Essayer ce nom "))
        self.cancelButton.setText(_translate("Dialog", "Abandonner"))