# Form implementation generated from reading ui file 'designer/supplierdialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SupplierDialog(object):
    def setupUi(self, SupplierDialog):
        SupplierDialog.setObjectName("SupplierDialog")
        SupplierDialog.resize(778, 557)
        SupplierDialog.setMinimumSize(QtCore.QSize(0, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(SupplierDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SupplierDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.introTextEdit = QtWidgets.QPlainTextEdit(SupplierDialog)
        self.introTextEdit.setObjectName("introTextEdit")
        self.verticalLayout.addWidget(self.introTextEdit)
        self.listView = QtWidgets.QListView(SupplierDialog)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.groupBox = QtWidgets.QGroupBox(SupplierDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 631, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_3.addWidget(self.addButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.updateButton = QtWidgets.QPushButton(self.layoutWidget)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout_3.addWidget(self.updateButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 642, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelName = QtWidgets.QLabel(self.layoutWidget1)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.labelName)
        self.nameEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nameEdit.setMinimumSize(QtCore.QSize(600, 0))
        self.nameEdit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setGeometry(QtCore.QRect(30, 30, 113, 26))
        self.idEdit.setObjectName("idEdit")
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.labelMessage = QtWidgets.QLabel(SupplierDialog)
        self.labelMessage.setMinimumSize(QtCore.QSize(50, 0))
        self.labelMessage.setText("")
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout.addWidget(self.labelMessage)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.deleteButton = QtWidgets.QPushButton(SupplierDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_4.addWidget(self.deleteButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.editButton = QtWidgets.QPushButton(SupplierDialog)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_4.addWidget(self.editButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.newButton = QtWidgets.QPushButton(SupplierDialog)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_4.addWidget(self.newButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(SupplierDialog)
        QtCore.QMetaObject.connectSlotsByName(SupplierDialog)

    def retranslateUi(self, SupplierDialog):
        _translate = QtCore.QCoreApplication.translate
        SupplierDialog.setWindowTitle(_translate("SupplierDialog", "Bière : fournisseurs de houblons"))
        self.label.setText(_translate("SupplierDialog", "Fournisseurs de houblons"))
        self.introTextEdit.setPlainText(_translate("SupplierDialog", "Les noms de fournisseurs que vous définissez ici seront les seuls à pouvoir être utilisées lors de l\'ajout de houblons dans la liste publique.\n"
"Cela a pour but de toujours utiliser le même nom, avec la même orthographe afin de permettre d\'éviter les doublons.\n"
"Les triplets nom, fournisseur et année de récolte des houblons sont uniques dans la base de données. \n"
""))
        self.addButton.setText(_translate("SupplierDialog", "Ajouter"))
        self.updateButton.setText(_translate("SupplierDialog", "Mettre à jour"))
        self.labelName.setText(_translate("SupplierDialog", "Nom"))
        self.deleteButton.setText(_translate("SupplierDialog", "Supprimer"))
        self.editButton.setText(_translate("SupplierDialog", "Modlifier"))
        self.newButton.setText(_translate("SupplierDialog", "Nouveau"))
