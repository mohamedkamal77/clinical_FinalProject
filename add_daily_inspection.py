# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_daily_inspection.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class add_daily_inspection:
    def __init__(self, centralwidget,verticalLayout_1):

        self.centralwidget = centralwidget
        self.verticalLayout_1 =verticalLayout_1
        self.frame =    QtWidgets.QFrame()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QHBoxLayout()
        self.header.setObjectName("header")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.header.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.header)
        self.select_eq = QtWidgets.QHBoxLayout()
        self.select_eq.setObjectName("select_eq")
        self.dep = QtWidgets.QComboBox(self.centralwidget)
        self.dep.setObjectName("dep")
        self.select_eq.addWidget(self.dep)
        self.eq = QtWidgets.QComboBox(self.centralwidget)
        self.eq.setObjectName("eq")

        

        self.select_eq.addWidget(self.eq)
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setObjectName("date")
        self.date.setDisplayFormat( "yyyy-MM-dd")
        self.date.setCalendarPopup(True)
        self.select_eq.addWidget(self.date)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.select_eq.addItem(spacerItem2)
        self.select_eq.setStretch(0, 1)
        self.select_eq.setStretch(1, 1)
        self.select_eq.setStretch(2, 1)
        self.select_eq.setStretch(2, 2)
        self.verticalLayout.addLayout(self.select_eq)
        self.check_1 = QtWidgets.QHBoxLayout()
        self.check_1.setContentsMargins(5, -1, 5, -1)
        self.check_1.setObjectName("check_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.check_1.addWidget(self.label)
        self.isproblem_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.isproblem_1.setObjectName("isproblem_1")
        self.check_1.addWidget(self.isproblem_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.check_1.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.check_1.addWidget(self.label_2)
        self.problem_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.problem_1.setObjectName("problem_1")
        self.check_1.addWidget(self.problem_1)
        self.check_1.setStretch(0, 2)
        self.check_1.setStretch(1, 1)
        self.check_1.setStretch(2, 1)
        self.check_1.setStretch(4, 4)
        self.verticalLayout.addLayout(self.check_1)
        self.check_2 = QtWidgets.QHBoxLayout()
        self.check_2.setContentsMargins(5, -1, 5, -1)
        self.check_2.setObjectName("check_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.check_2.addWidget(self.label_3)
        self.isproblem_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.isproblem_2.setObjectName("isproblem_2")
        self.check_2.addWidget(self.isproblem_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.check_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.check_2.addWidget(self.label_4)
        self.problem_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.problem_2.setObjectName("problem_2")
        self.check_2.addWidget(self.problem_2)
        self.check_2.setStretch(0, 2)
        self.check_2.setStretch(1, 1)
        self.check_2.setStretch(2, 1)
        self.check_2.setStretch(4, 4)
        self.verticalLayout.addLayout(self.check_2)
        self.check_3 = QtWidgets.QHBoxLayout()
        self.check_3.setContentsMargins(5, -1, 5, -1)
        self.check_3.setObjectName("check_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.check_3.addWidget(self.label_5)
        self.isproblem_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.isproblem_3.setObjectName("isproblem_3")
        self.check_3.addWidget(self.isproblem_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.check_3.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.check_3.addWidget(self.label_6)
        self.problem_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.problem_3.setObjectName("problem_3")
        self.check_3.addWidget(self.problem_3)
        self.check_3.setStretch(0, 2)
        self.check_3.setStretch(1, 1)
        self.check_3.setStretch(2, 1)
        self.check_3.setStretch(4, 4)
        self.verticalLayout.addLayout(self.check_3)
        self.check_4 = QtWidgets.QHBoxLayout()
        self.check_4.setContentsMargins(5, -1, 5, -1)
        self.check_4.setObjectName("check_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.check_4.addWidget(self.label_7)
        self.isproblem_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.isproblem_4.setObjectName("isproblem_4")
        self.check_4.addWidget(self.isproblem_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.check_4.addItem(spacerItem6)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.check_4.addWidget(self.label_8)
        self.problem_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.problem_4.setObjectName("problem_4")
        self.check_4.addWidget(self.problem_4)
        self.check_4.setStretch(0, 2)
        self.check_4.setStretch(1, 1)
        self.check_4.setStretch(2, 1)
        self.check_4.setStretch(4, 4)
        self.verticalLayout.addLayout(self.check_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Save.setFont(font)
        self.Save.setFlat(True)
        self.Save.setObjectName("Save")
        self.horizontalLayout_2.addWidget(self.Save)
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cancel.setFont(font)
        self.Cancel.setFlat(True)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_2.addWidget(self.Cancel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame.setLayout(self.verticalLayout)
        self.verticalLayout_1.addWidget(self.frame)
        self.frame.hide()
        self.Cancel.clicked.connect(self.hide)
        self.label_9.setText( "Daily  Inspection")
        self.label.setText( "  Cleaning")
        self.isproblem_1.setText( "No proble")
        self.label_2.setText( "Problem")
        self.label_3.setText( "  Phyisical")
        self.isproblem_2.setText( "No proble")
        self.label_4.setText( "Problem")
        self.label_5.setText( "  Visual")
        self.isproblem_3.setText( "No proble")
        self.label_6.setText( "Problem")
        self.label_7.setText( "  Power")
        self.isproblem_4.setText( "No proble")
        self.label_8.setText( "Problem")
        self.Save.setText( "Save")
        self.Cancel.setText( "Cancel")
        self.fill_eq_func=0

        self.dep.currentIndexChanged.connect(self.change_eq)
        self.Cancel.clicked.connect(self.hide)

    def fill_dep(self,func):
        deps = func()
        self.dep.addItem('None')
        for i in deps:
            self.dep.addItem(i[0])
    def fill_eq(self,func):
        self.eq.clear()
        self.fill_eq_func  = func
        eqs = func(0)
        for i in eqs:
            self.eq.addItem(i[0]+','+i[1])

    def connect_hide(self,func):
        self.Cancel.clicked.connect(func)


    def change_eq(self):
        index = int(self.dep.currentIndex() )
        if self.fill_eq_func!=0:
            self.eq.clear()
            eqs=self.fill_eq_func(index)
            for i in eqs:
                self.eq.addItem(i[0]+','+i[1])


    def get_date(self):
        data = []
        
        data.append(int(not self.isproblem_1.isChecked()))
        data.append(int(not self.isproblem_2.isChecked()))
        data.append(int(not self.isproblem_3.isChecked()))
        data.append(int(not self.isproblem_4.isChecked()))
        data.append(self.problem_1.text())
        data.append(self.problem_2.text())
        data.append(self.problem_3.text())
        data.append(self.problem_4.text())
        data.append(self.date.date().toPyDate())
        eq =self.eq.currentText()
        eq=eq.split(',')
        data.append(int(eq[1]))
    
        return data 

    def hide(self):
        self.frame.hide()

    def show(self):
        self.frame.show()

    def connect_save(self,func):
        self.Save.clicked.connect(func)
