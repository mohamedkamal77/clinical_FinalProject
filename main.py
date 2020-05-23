import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pylab as plt
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from ui import Ui_MainWindow
from add_eng import  add_eng
from add_sup_provider import add_supplier
from add_equipement import  add_eq
from add_daily_inspection import add_daily_inspection
from ppm_ui import add_ppm
from purchase_ui import  add_purchase
from  main_ui import main_page
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import  numpy as np
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="hospital_cmms"
)

mycursor = mydb.cursor()

class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(ApplicationWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.main_page=main_page(self.ui.centralwidget , self.ui.verticalLayout_2,self.ui.listWidget,self.fill_table,self.ui.select_dp)
		self.add_eq =add_eq(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.add_eng = add_eng(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.add_supplier = add_supplier(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.add_daily_inspection=add_daily_inspection(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.add_ppm = add_ppm(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.add_purchase = add_purchase(self.ui.centralwidget , self.ui.verticalLayout_2)
		self.currentItem = ""
		self.map = { "Departement":"dep","Equipment":"dep", "Engineer": "engineer"  ,"Technician":"technician","Supplier":"supplier","Service":"service_supplier","Equipement":"equipement","Daily Inspection":"daily_inspection","PPM":'ppm',"Purchase Order":'purchase'}
		self.ui.listWidget.currentRowChanged.connect(self.change_table)
		self.ui.pushButton.clicked.connect(self.add_data)
		self.add_supplier.connect_save(self.save_supplier)
		self.add_eng.connect_save(self.save_eng)
		self.add_eq.connect_save(self.save_equipement)
		self.add_eq.connect_supplier(self.add_supp_)
		self.add_eq.connect_service(self.add_service_)
		self.add_purchase.connect_save(self.save_purchase)
		self.add_purchase.connect_supplier(self.add_supp_)
		plt.ioff()
		self.fig , self.ax =plt.subplots(figsize=(27,27))
		plotWidget = FigureCanvas(self.fig) 
		
		self.ui.plot.addWidget(plotWidget)
		self.add_daily_inspection.connect_save(self.save_daily_inspection)
		self.add_ppm.connect_save(self.save_ppm)
		self.fill_dep(self.get_dep)
		self.ui.select_dp.currentIndexChanged.connect(self.change_dp)
	def change_table(self,ind):
		self.add_eq.hide()
		self.add_purchase.hide()
		self.add_supplier.hide()
		self.add_ppm.hide()
		self.add_daily_inspection.hide()
		self.add_eng.hide()

		self.currentItem =(self.ui.listWidget.currentItem().text())
		self.ui.label.setText(self.currentItem)
		if self.currentItem in ["Daily Inspection","PPM",'Purchase Order']:
			if self.currentItem == 'Purchase Order':
				self.ui.plt_frame.hide()
			self.ui.select_to_date.show()
			self.ui.select_from_date.show()
			self.ui.lab2.show()
			self.ui.lab3.show()
		else:
			self.ui.plt_frame.hide()
			self.ax.cla()
			self.ui.select_to_date.hide()
			self.ui.select_from_date.hide()
			self.ui.lab2.hide()
			self.ui.lab3.hide()

		if self.currentItem !='Home':
			self.fill_table(self.map[self.currentItem])
			self.main_page.hide()
			self.ui.show_data_frame.show()
		else:
			self.main_page.frame.show()
			self.ui.show_data_frame.hide()
				
	def add_data(self):

		if self.currentItem in ["Engineer" ,"Technician"] :
			self.add_eng.show(self.currentItem)
			self.add_eng.fill_dep(self.get_dep)			
		elif self.currentItem in ["Supplier" ,"Service"]:
			self.add_supplier.show(self.currentItem)
		elif self.currentItem in ["Equipement" ]:
			self.add_eq.show(self.currentItem)
			self.add_eq.fill_dep(self.get_dep)
			self.add_eq.fill_room(self.get_room)
			self.add_eq.fill_supplier(self.get_supplier)
			self.add_eq.fill_service_provider(self.get_service_provider)
		elif self.currentItem in ["Daily Inspection" ] :
			self.add_daily_inspection.show()
			self.add_daily_inspection.fill_dep(self.get_dep)
			self.add_daily_inspection.fill_eq(self.get_eq)
		elif self.currentItem =="PPM":
			self.add_ppm.show()
			self.add_ppm.fill_dep(self.get_dep)
			self.add_ppm.fill_eq(self.get_eq)
			self.add_ppm.fill_eng(self.get_eng)
			self.add_ppm.fill_tech(self.get_tech)
		elif self.currentItem =='Purchase Order':
			self.add_purchase.show()
			self.add_purchase.fill_eng(self.get_eng)
			self.add_purchase.fill_supplier(self.get_supplier)



	def save_eng(self):
		table = self.map[self.currentItem]
		if self.currentItem == "Engineer":
			mycursor.execute("SELECT eng_no FROM engineer ")
		else:
			mycursor.execute("SELECT t_no FROM technician ")
		no =mycursor.fetchall()
		no = np.max(no) + 1

		if self.currentItem == "Engineer":
			sql = "INSERT INTO engineer (eng_fname,eng_mname,eng_lname,eng_country,eng_city,eng_address,eng_salary,eng_hours,dep_no,eng_birthdate,ssd,eng_no)  VALUES (%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s,%s)"
		else:	
			sql = "INSERT INTO technician (t_fname,t_mname,t_lname,t_country,t_city,t_address,t_salary,t_hours,dep_no,t_birthdate,ssd,t_no) VALUES (%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s,%s)"
		val = self.add_eng.get_date()
		val.append(no)
		val = tuple(val)
		mycursor.execute(sql,val)
		mydb.commit()
		self.add_eng.hide()

	def save_supplier(self, supplier):
		table = self.map[supplier]
		if supplier == "Supplier":
			mycursor.execute("SELECT sup_no FROM supplier ")
		else:
			mycursor.execute("SELECT sup_no FROM service_supplier ")
		no = mycursor.fetchall()
		no = int(np.max(no)	+ 1 )
		if supplier == "Supplier":
			sql = "INSERT INTO supplier (sup_name,sup_country,sup_city,sup_address,sup_no)  VALUES (%s,%s, %s, %s,%s)"
		else:	
			sql = "INSERT INTO service_supplier (sup_name,sup_country,sup_city,sup_address,sup_no) VALUES (%s,%s, %s, %s,%s)"
		val ,contacts = self.add_supplier.get_date()
		val.append(no)
		val =tuple(val)
		mycursor.execute(sql,val)
		mydb.commit()		

		for i in contacts:
			val1 =tuple([i,np.int(no)])
			if supplier == "Supplier":
				sql1  = "INSERT INTO sup_contact (sup_contact,sup_no)  VALUES (%s,%s)"

			else:
				sql1  = "INSERT INTO service_sup_contact (service_sup_contact,sup_no)  VALUES (%s,%s)"

			mycursor.execute(sql1,val1)
			mydb.commit()
		self.add_supplier.hide()
		if self.currentItem == "Equipement":
			self.add_eq.fill_service_provider(self.get_service_provider)
			self.add_eq.fill_supplier(self.get_supplier)
			


	def save_equipement(self):
		print("IN")
		table = self.map[self.currentItem]
		mycursor.execute("SELECT eq_no FROM equipement ")
		eq_no = mycursor.fetchall()
		eq_no = int(np.max(eq_no) + 1)
		
		if self.currentItem == "Equipement":
			sql = "INSERT INTO equipement (eq_name,eq_dep_no,eq_room_no,eq_start_date,eq_make,eq_model,eq_country,eq_serial,parts,eq_supplier_no,eq_price,eq_entry_date,eq_waranty_period,ep_service_sup_no,eq_service_kind,eq_service_start,eq_service_end,eq_code,eq_no)  VALUES (%s, %s, %s,%s, %s,%s,%s, %s, %s,%s, %s,%s,%s, %s, %s,%s, %s,%s,%s)"
		val = self.add_eq.get_date()
		print(val)
		code = ""
		code= code + str(val[0][0])
		code= code + str(val[4][0])
		code= code +str(val[5][0])
		code= code + str(eq_no)
		val.append(code)
		val.append(eq_no)
		val = tuple(val)
		mycursor.execute(sql,val)
		mydb.commit()
		self.add_eq.hide()

	def save_daily_inspection(self):
		self.ui.label.setText(self.currentItem)	
		if self.currentItem == "Daily Inspection":
			sql = "INSERT INTO daily_inspection (clearing_check,physical_check,function_check,power_check,clearing_problem,physical_problem,function_problem,power_problem,check_date,eq_no)  VALUES (%s,%s, %s, %s,%s, %s,%s,%s, %s, %s)"
			val = self.add_daily_inspection.get_date()
			val = tuple(val)
			mycursor.execute(sql,val)
			mydb.commit()
		self.add_daily_inspection.hide()
	def save_ppm(self):
		self.ui.label.setText(self.currentItem)	
		if self.currentItem == "PPM":
			sql = "INSERT INTO ppm (eq_no,eng_no,t_no,battery_fault,battery_fault_details,circuit_fault,circuit_fault_details,cable_fault,cable_fault_details,software_fault,software_fault_details,wrong_output,wrong_output_details,internal_malfunction,internal_malfunction_details,incorrect_connection,incorrect_connection_details,current_leak,physical_leak,part_not_functionning,part_not_functionning_details,change_part,change_part_details,continous_alarm,continous_alarm_details,no_alarm,no_alarm_details ,cost,check_date)  VALUES (%s, %s, %s,%s, %s,%s,%s, %s, %s, %s,%s, %s,%s,%s, %s, %s, %s,%s, %s,%s,%s, %s, %s, %s,%s, %s,%s,%s, %s)"
			val = self.add_ppm.get_date()
			val = tuple(val)
			mycursor.execute(sql,val)
			mydb.commit()
			self.add_ppm.hide()

	def save_purchase(self):
		self.ui.label.setText(self.currentItem)	
		if self.currentItem == "Purchase Order":
			sql = "INSERT INTO purchase (p_product,p_eng_no,p_sup_no,p_date,p_expect_date,p_unit_no,p_unit_cost,p_additional_cost,p_additional_cost_details,p_status)  VALUES (%s,%s, %s, %s,%s, %s,%s,%s, %s,%s)"
			val = self.add_purchase.get_date()
			if val !=0:
				val.append('On Order')
				val = tuple(val)
				mycursor.execute(sql,val)
				mydb.commit()
				self.add_purchase.hide()

	def get_eq(self,dep):
		if dep==0:
			mycursor.execute("SELECT eq_name,eq_code FROM equipement")
			return mycursor.fetchall()

		else :
			mycursor.execute("SELECT eq_name,eq_code FROM equipement WHERE eq_dep_no = %s"%dep)
			return mycursor.fetchall()
	def add_supp_(self,fun):
		self.add_supplier.show("Supplier")
		fun(self.get_supplier)
		
		
	def add_service_(self,fun):
		self.add_supplier.show("Service Provider")
		fun(self.get_service_provider)

	def get_dep(self):
		mycursor.execute("SELECT dep_name FROM dep ")
		dep = mycursor.fetchall()
		return dep[1::]

	def get_room(self):
		mycursor.execute("SELECT room_name FROM room ")
		room = mycursor.fetchall()
		return room

	def get_supplier(self):
		mycursor.execute("SELECT sup_name FROM supplier ")
		supplier = mycursor.fetchall()
		return supplier

	def get_service_provider(self):
		mycursor.execute("SELECT sup_name FROM service_supplier ")
		supplier = mycursor.fetchall()
		return supplier

	def get_eng(self):
		mycursor.execute("SELECT eng_fname,eng_mname,eng_lname FROM engineer ")
		supplier = mycursor.fetchall()
		return supplier

	def get_tech(self):
		mycursor.execute("SELECT t_fname,t_mname,t_lname FROM technician ")
		supplier = mycursor.fetchall()
		return supplier

	def fill_table(self,table,dep_no=0):
		if table == 'ppm':
			if dep_no !=0:
				dep_no =dep_no 
				mycursor.execute("SELECT eq_name,eq_code,eng_fname,eng_lname,t_fname,t_lname,battery_fault,circuit_fault,cable_fault,software_fault,wrong_output,internal_malfunction,	incorrect_connection,current_leak,physical_leak,part_not_functionning,change_part,continous_alarm,no_alarm,cost  FROM ppm JOIN engineer ON ppm.eng_no=engineer.eng_no JOIN technician ON ppm.t_no=technician.t_no JOIN equipement ON equipement.eq_no=ppm.eq_no WHERE equipement.dep_no = %s"%dep_no)
				
			else:
				mycursor.execute("SELECT eq_name,eq_code,eng_fname,eng_lname,t_fname,t_lname,battery_fault,circuit_fault,cable_fault,software_fault,wrong_output,internal_malfunction,	incorrect_connection,current_leak,physical_leak,part_not_functionning,change_part,continous_alarm,no_alarm,cost  FROM ppm JOIN engineer ON ppm.eng_no=engineer.eng_no JOIN technician ON ppm.t_no=technician.t_no JOIN equipement ON equipement.eq_no=ppm.eq_no")
			row_headers=[x[0] for x in mycursor.description]
			myres = mycursor.fetchall()
			self.y=np.asarray(myres)
			self.y = self.y[:,6:19]
			self.y =np.sum(self.y.astype(np.int) ,axis=0)
			self.x =row_headers[6:19]
			self.report_plt(self.y,self.x,dep_no,0)
			
			print(self.y)
		elif table == 'purchase':
			if dep_no !=0:
				dep_no =dep_no +1
				mycursor.execute("SELECT p_product,p_date,p_expect_date,p_unit_cost,p_unit_no,p_status,eng_fname,eng_lname FROM purchase JOIN engineer ON purchase.p_eng_no=engineer.eng_no JOIN supplier ON supplier.sup_no=purchase.p_sup_no   WHERE engineer.dep_no = %s"%dep_no)
			else:
				mycursor.execute("SELECT p_product,p_date,p_expect_date,p_unit_cost,p_unit_no,p_status,eng_fname,eng_lname FROM purchase JOIN engineer ON purchase.p_eng_no=engineer.eng_no JOIN supplier ON supplier.sup_no=purchase.p_sup_no    ")
			row_headers=[x[0] for x in mycursor.description]
			myres = mycursor.fetchall()

		elif table=='daily_inspection':
			if dep_no !=0:
				dep_no =dep_no 
				mycursor.execute("SELECT eq_name,eq_code,clearing_check,physical_check,function_check,power_check FROM daily_inspection JOIN equipement ON equipement.eq_no=daily_inspection.eq_no  WHERE equipement.dep_no = %s"%dep_no)
			else:
				mycursor.execute("SELECT eq_name,eq_code,clearing_check,physical_check,function_check,power_check FROM daily_inspection JOIN equipement ON equipement.eq_no=daily_inspection.eq_no")
			row_headers=[x[0] for x in mycursor.description]
			print(row_headers)
			myres = mycursor.fetchall()
			y=np.asarray(myres)
			if y.size!=0:
				y=y[:,2:]
				x =row_headers[2:]
				y =np.sum(y.astype(np.int),axis=0)
				
				print(y)
				self.report_plt(y,x,dep_no,1)
		elif table in ['supplier','service_supplier']:
			mycursor.execute("SELECT * FROM %s"%table)
			row_headers=[x[0] for x in mycursor.description]
			myres = mycursor.fetchall()

		else:
			if dep_no !=0:
				if table== 'engineer':
					dep_no = dep_no+1
				mycursor.execute(f"SELECT * FROM {table} where dep_no = %s"%dep_no)
			else:
				mycursor.execute("SELECT * FROM %s"%table)
			row_headers=[x[0] for x in mycursor.description]
			myres = mycursor.fetchall()
		shape = np.shape(myres)
		if shape[0]!= 0:
			self.ui.tableWidget.setRowCount(shape[0] )
			self.ui.tableWidget.setColumnCount(shape[1] )
			
			for i in range(shape[1]):
				self.ui.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(row_headers[i]))			
				for j in range(shape[0]):
					if row_headers[i]=='dep_no':
						val =myres[j][i]
						mycursor.execute("SELECT dep_name FROM dep Where dep_no =%s"%val )
						self.ui.tableWidget.setItem(j,i, QtWidgets.QTableWidgetItem(str(mycursor.fetchone()[0])) ) 
					else:
						if table in['ppm','daily_inspection']:
							if row_headers[i]!='cost':
								if myres[j][i]==0:
									val = '--ve'
								elif myres[j][i]==1:
									val = '++ve'
								else:
									val =myres[j][i]
							else:
								val =myres[j][i]
						else:
							val =myres[j][i]

						self.ui.tableWidget.setItem(j,i, QtWidgets.QTableWidgetItem(str(val)) ) 
						if table in ['ppm','daily_inspection']:
							self.ui.plt_frame.show()               
		else :
			length = np.size(row_headers)
			self.ui.tableWidget.clear()
			self.ui.tableWidget.setRowCount(5 )
			self.ui.tableWidget.setColumnCount(length )
			for i in range(length):
				self.ui.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(row_headers[i]))	
	def report_plt(self,y,x,dep_no,index):
		dep = ['all','Emergency','OR','ICU']
		table=['PPM','Daily Inspection']

		size = np.size(x)
		x_pos = np.arange(size)
		self.ax.cla()
		self.ax.bar(x_pos,y)
		self.ax.set_xticks(x_pos)
		self.ax.set_xticklabels(x,rotation=40)
		self.ax.tick_params(axis='x',which='minor',labelsize=6)
		self.ax.tick_params(axis='x',which='major',labelsize=6)
		#bself.fig.tight_layout()
		plt.subplots_adjust(bottom=0.3,left=0.07,right=0.95)
		self.ax.set(title=f'{table[index]} for {dep[dep_no]} dep',xlabel = 'check',ylabel='no of proplems')

		self.fig.canvas.draw_idle()
	def fill_dep(self,func):	
		deps = func()
		self.ui.select_dp.addItem('None')
		for i in deps:
		    self.ui.select_dp.addItem(i[0])

	def change_dp(self):
		self.ui.plt_frame.hide()
		dep_no = self.ui.select_dp.currentIndex()
		self.fill_table(self.map[self.currentItem],dep_no )
				





def main():
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()
	application.show()
	app.exec_()


if __name__ == "__main__":
	main()