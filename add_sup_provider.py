# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_sup_provider.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class add_supplier:
    def __init__(self, centralwidget,verticalLayout):
        self.verticalLayout = verticalLayout
        self.centralwidget = centralwidget
        self.frame =QtWidgets.QFrame()
        self.verticalLayoutWidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 591, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.add_supplier = QtWidgets.QVBoxLayout()
        self.add_supplier.setContentsMargins(20, 10, 20, 10)
        self.add_supplier.setSpacing(8)
        self.add_supplier.setObjectName("add_supplier")
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setObjectName("header_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.header_layout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem1)
        self.header_layout.setStretch(0, 2)
        self.header_layout.setStretch(1, 1)
        self.header_layout.setStretch(2, 2)
        self.add_supplier.addLayout(self.header_layout)
        self.data_layout_1 = QtWidgets.QHBoxLayout()
        self.data_layout_1.setContentsMargins(50, -1, 50, -1)
        self.data_layout_1.setSpacing(20)
        self.data_layout_1.setObjectName("data_layout_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.data_layout_1.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.data_layout_1.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.data_layout_1.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.data_layout_1.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.data_layout_1.addWidget(self.label_6)
        self.contacts = QtWidgets.QComboBox(self.centralwidget)
        self.contacts.setEditable(True)
        self.contacts.setDuplicatesEnabled(False)
        self.contacts.setFrame(True)
        self.contacts.setObjectName("contacts")
        self.data_layout_1.addWidget(self.contacts)
        self.data_layout_1.setStretch(0, 1)
        self.data_layout_1.setStretch(1, 4)
        self.data_layout_1.setStretch(2, 1)
        self.data_layout_1.setStretch(3, 4)
        self.data_layout_1.setStretch(4, 1)
        self.data_layout_1.setStretch(5, 4)
        self.add_supplier.addLayout(self.data_layout_1)
        self.data_layout_2 = QtWidgets.QHBoxLayout()
        self.data_layout_2.setContentsMargins(50, -1, 50, -1)
        self.data_layout_2.setSpacing(20)
        self.data_layout_2.setObjectName("data_layout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.data_layout_2.addWidget(self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.data_layout_2.addWidget(self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.data_layout_2.addWidget(self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.data_layout_2.addWidget(self.lineEdit_6)
        self.add_supplier.addLayout(self.data_layout_2)
        self.add_layout = QtWidgets.QHBoxLayout()
        self.add_layout.setObjectName("add_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_layout.addItem(spacerItem2)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setFlat(True)
        self.save.setObjectName("save")
        self.add_layout.addWidget(self.save)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.add_layout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_layout.addItem(spacerItem3)
        self.add_supplier.addLayout(self.add_layout)
        self.verticalLayoutWidget.addLayout(self.add_supplier)
        self.frame.setLayout(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.frame)
        self.frame.hide()

        self.label.setText( "TextLabel")
        self.label_2.setText( "Name")
        self.label_3.setText( "Country")
        self.label_6.setText( "Contact")
        self.label_4.setText( "City")
        self.label_5.setText( "Address")
        self.save.setText( "Save")
        self.pushButton_2.setText( "Cancel")


    def get_date(self):
        data = []
        data.append(self.lineEdit.text())
        data.append(self.lineEdit_2.text())
        data.append(self.lineEdit_5.text())
        data.append(self.lineEdit_6.text())
        contacts =[]
        for i in range(self.contacts.count()):
            contacts.append(self.contacts.itemText(i))
        
        

        return data,contacts

    def hide(self):
        self.frame.hide()

    def show(self,employee):
        self.label.setText(f"Add {employee}")
        self.frame.show()

    def connect_save(self,func):
        self.save.clicked.connect(func)

