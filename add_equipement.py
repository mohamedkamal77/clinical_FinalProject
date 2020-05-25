# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_eq.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class add_eq:
    def __init__(self,centralwidget,verticalLayout):
        self.verticalLayout1 = verticalLayout
        self.centralwidget = centralwidget
        self.frame = QtWidgets.QFrame()

        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setObjectName("header_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.header_layout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.header_layout)
        self.data_layout_1 = QtWidgets.QHBoxLayout()
        self.data_layout_1.setObjectName("data_layout_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.data_layout_1.addWidget(self.label)
        self.eq_name = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_name.setObjectName("eq_name")
        self.data_layout_1.addWidget(self.eq_name)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.data_layout_1.addWidget(self.label_3)
        self.eq_dep = QtWidgets.QComboBox(self.centralwidget)
        self.eq_dep.setEditable(True)
        self.eq_dep.setObjectName("eq_dep")
        self.data_layout_1.addWidget(self.eq_dep)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.data_layout_1.addWidget(self.label_4)
        self.eq_room = QtWidgets.QComboBox(self.centralwidget)
        self.eq_room.setEditable(True)
        self.eq_room.setObjectName("eq_room")
        self.data_layout_1.addWidget(self.eq_room)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.data_layout_1.addWidget(self.label_5)
        self.operation_date = QtWidgets.QDateEdit(self.centralwidget)
        self.operation_date.setObjectName("operation_date")
        self.operation_date.setDisplayFormat( "yyyy-MM-dd")
        self.operation_date.setCalendarPopup(True)
        self.data_layout_1.addWidget(self.operation_date)
        self.verticalLayout.addLayout(self.data_layout_1)
        self.data_layout_2 = QtWidgets.QHBoxLayout()
        self.data_layout_2.setObjectName("data_layout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.data_layout_2.addWidget(self.label_6)
        self.eq_make = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_make.setObjectName("eq_make")
        self.data_layout_2.addWidget(self.eq_make)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.data_layout_2.addWidget(self.label_7)
        self.eq_model = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_model.setObjectName("eq_model")
        self.data_layout_2.addWidget(self.eq_model)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.data_layout_2.addWidget(self.label_8)
        self.eq_serial = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_serial.setObjectName("eq_serial")
        self.data_layout_2.addWidget(self.eq_serial)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.data_layout_2.addWidget(self.label_9)
        self.eq_country = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_country.setObjectName("eq_country")
        self.data_layout_2.addWidget(self.eq_country)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.data_layout_2.addWidget(self.label_10)
        self.eq_parts = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_parts.setObjectName("eq_parts")
        self.data_layout_2.addWidget(self.eq_parts)
        self.verticalLayout.addLayout(self.data_layout_2)
        self.Data_layout_3 = QtWidgets.QHBoxLayout()
        self.Data_layout_3.setObjectName("Data_layout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.Data_layout_3.addWidget(self.label_11)
        self.eq_supplier = QtWidgets.QComboBox(self.centralwidget)
        self.eq_supplier.setObjectName("eq_supplier")
        self.Data_layout_3.addWidget(self.eq_supplier)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.Data_layout_3.addWidget(self.label_12)
        self.eq_price = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_price.setObjectName("eq_price")
        self.Data_layout_3.addWidget(self.eq_price)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.Data_layout_3.addWidget(self.label_13)
        self.entry_date = QtWidgets.QDateEdit(self.centralwidget)
        self.entry_date.setObjectName("entry_date")
        self.entry_date.setDisplayFormat( "yyyy-MM-dd")
        self.entry_date.setCalendarPopup(True)
        self.Data_layout_3.addWidget(self.entry_date)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.Data_layout_3.addWidget(self.label_14)
        self.eq_warant = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_warant.setObjectName("eq_warant")
        self.Data_layout_3.addWidget(self.eq_warant)
        self.add_supplier = QtWidgets.QPushButton(self.centralwidget)
        self.add_supplier.setFlat(True)
        self.add_supplier.setObjectName("add_supplier")
        self.Data_layout_3.addWidget(self.add_supplier)
        self.verticalLayout.addLayout(self.Data_layout_3)
        self.data_layout_4 = QtWidgets.QHBoxLayout()
        self.data_layout_4.setObjectName("data_layout_4")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.data_layout_4.addWidget(self.label_15)
        self.eq_service = QtWidgets.QComboBox(self.centralwidget)
        self.eq_service.setObjectName("eq_service")
        self.data_layout_4.addWidget(self.eq_service)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.data_layout_4.addWidget(self.label_16)
        self.eq_service_kind = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_service_kind.setObjectName("eq_service_kind")
        self.data_layout_4.addWidget(self.eq_service_kind)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.data_layout_4.addWidget(self.label_17)
        self.eq_service_start = QtWidgets.QDateEdit(self.centralwidget)
        self.eq_service_start.setObjectName("eq_service_start")
        self.eq_service_start.setDisplayFormat( "yyyy-MM-dd")
        self.eq_service_start.setCalendarPopup(True)
        self.data_layout_4.addWidget(self.eq_service_start)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.data_layout_4.addWidget(self.label_18)
        self.eq_service_end = QtWidgets.QDateEdit(self.centralwidget)
        self.eq_service_end.setObjectName("eq_service_end")
        self.eq_service_end.setDisplayFormat( "yyyy-MM-dd")
        self.eq_service_end.setCalendarPopup(True)
        self.data_layout_4.addWidget(self.eq_service_end)
        self.add_service = QtWidgets.QPushButton(self.centralwidget)
        self.add_service.setFlat(True)
        self.add_service.setObjectName("add_service")
        self.data_layout_4.addWidget(self.add_service)
        self.verticalLayout.addLayout(self.data_layout_4)
        self.save__layout = QtWidgets.QHBoxLayout()
        self.save__layout.setObjectName("save__layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save__layout.addItem(spacerItem2)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setFlat(True)
        self.Save.setObjectName("Save")
        self.save__layout.addWidget(self.Save)
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setFlat(True)
        self.Cancel.setObjectName("Cancel")
        self.save__layout.addWidget(self.Cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save__layout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.save__layout)
        self.frame.setLayout(self.verticalLayout)     
        self.verticalLayout1.addWidget(self.frame)
        self.frame.hide()
        self.label_2.setText( "Add")
        self.label.setText( "Name")
        self.label_3.setText( "Dep")
        self.label_4.setText( "Room")
        self.label_5.setText( "Op_date")
        self.label_6.setText( "Make")
        self.label_7.setText( "Model")
        self.label_8.setText( "S no")
        self.label_9.setText( "Made in")
        self.label_10.setText( "Parts")
        self.label_11.setText( "Supplier")
        self.label_12.setText( "Price")
        self.label_13.setText( "Entry Date")
        self.label_14.setText( "Waranty period")
        self.add_supplier.setText( "Add Supplier")
        self.label_15.setText( "Service provider")
        self.label_16.setText( "Service")
        self.label_17.setText( "Service start")
        self.label_18.setText( "End")
        self.add_service.setText( "Add Provider")
        self.Save.setText( "Save")
        self.Cancel.setText( "Cancel")
        self.service_f=0
        self.supplier_f=0
        self.Cancel.clicked.connect(self.hide)



    def fill_dep(self,func):
        self.eq_dep.clear()
        deps = func()
        for i in deps:
            self.eq_dep.addItem(i[0])
    def fill_room(self,func):
        self.eq_room.clear()
        rooms = func()
        for i in rooms:
            self.eq_room.addItem(i[0])
    def fill_supplier(self,func):
        self.eq_supplier.clear()
        self.supplier_f=func
        supplier = func()
        self.eq_supplier.addItem("None")
        for i in supplier:
            self.eq_supplier.addItem(i[0])
    def fill_service_provider(self,func):
        self.eq_service.clear()
        self.service_f=func
        rooms = func()
        self.eq_service.addItem("None")
        for i in rooms:
            self.eq_service.addItem(i[0])

    def change_sup(self):
        if self.supplier_f!=0:
            self.eq_supplier.clear()
            self.eq_supplier.addItem("None")
            sup=self.supplier_f()
            for i in sup:
                self.eq_supplier.addItem(i[0])

    def change_prov(self):
        if self.service_f!=0:
            self.eq_service.clear()
            self.eq_service.addItem("None")
            sup=self.service_f()
            for i in sup:
                self.eq_service.addItem(i[0])

    def get_date(self):
        data = []
        data.append(self.eq_name.text())
        data.append(int(self.eq_dep.currentIndex())+ 1)
        data.append(int(self.eq_room.currentIndex())+ 1)
        data.append(self.operation_date.date().toPyDate())

        data.append(self.eq_make.text())
        data.append(self.eq_model.text())
        data.append(self.eq_serial.text())
        data.append(self.eq_country.text())
        data.append(self.eq_parts.text())
        if self.eq_supplier.currentIndex() !=0:
            data.append(int(self.eq_supplier.currentIndex()))
        else:
            data.append(None)
        if self.eq_price.text() !='':
            data.append(int(self.eq_price.text()))
        data.append(self.entry_date.date().toPyDate())
        if self.eq_warant.text() =='':
            data.append(None)
        else:
            data.append(int(self.eq_warant.text()))

        if self.eq_service.currentIndex()!=0:
            data.append(int(self.eq_service.currentIndex()))
        else :
            data.append(None)
        data.append(self.eq_service_kind.text())
        data.append(self.eq_service_start.date().toPyDate())
        data.append(self.eq_service_end.date().toPyDate())
        if data[0]!=None and  data[4]!=None and data[5]!=None  :
            return data


    def hide(self):
        self.frame.hide()

    def show(self,employee):
        self.label_2.setText(f"Add {employee}")
        self.frame.show()

    def connect_save(self,func):
        self.Save.clicked.connect(func)

    def connect_supplier(self,func):
        self.add_supplier.clicked.connect(func)

    def connect_service(self,func):
        self.add_service.clicked.connect(func)
        