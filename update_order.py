# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class update_purchase:
    def __init__(self,centralwidget,verticalLayout):
        self.centralwidget = centralwidget
        self.verticalLayout = verticalLayout
        self.frame = QtWidgets.QFrame()

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout1.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.order = QtWidgets.QComboBox(self.centralwidget)
        self.order.setObjectName("order")
        self.horizontalLayout_2.addWidget(self.order)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.received = QtWidgets.QCheckBox(self.centralwidget)
        self.received.setObjectName("received")
        self.horizontalLayout_2.addWidget(self.received)
        self.verticalLayout1.addLayout(self.horizontalLayout_2)

        self.save_layout = QtWidgets.QHBoxLayout()
        self.save_layout.setObjectName("save_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_layout.addItem(spacerItem3)
        self.Save_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Save_bt.setFont(font)
        self.Save_bt.setFlat(True)
        self.Save_bt.setObjectName("Save_bt")
        self.save_layout.addWidget(self.Save_bt)
        self.Cancel_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cancel_bt.setFont(font)
        self.Cancel_bt.setDefault(False)
        self.Cancel_bt.setFlat(True)
        self.Cancel_bt.setObjectName("Cancel_bt")
        self.save_layout.addWidget(self.Cancel_bt)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_layout.addItem(spacerItem4)
        self.verticalLayout1.addLayout(self.save_layout)
        self.frame.setLayout(self.verticalLayout1)
        self.verticalLayout.addWidget(self.frame)
        self.frame.hide()

        self.label.setText( "Update Purchase Order")
        self.label_2.setText( "Order")
        self.received.setText( "Received")
        self.Save_bt.setText( "Save")
        self.Cancel_bt.setText( "Cancel")

        self.Cancel_bt.clicked.connect(self.hide)

    def fill_order(self,func):
        deps = func()
        for i in deps:
            self.order.addItem(i[0]+','+str(i[1]))

    def get_date(self):
        data = []
        order = self.order.currentText()
        order=order.split(',')
        order = order[1]
        data.append(int(order))
        if self.received.isChecked():

            data.append('Received')
        else:
            data.append('On Order')
        return data

    def hide(self):
        self.frame.hide()

    def show(self):
        self.frame.show()

    def connect_save(self,func):
        self.Save_bt.clicked.connect(func)


