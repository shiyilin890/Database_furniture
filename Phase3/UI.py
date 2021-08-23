from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import mysql.connector as mc
import MySQLdb as mdb
import sys, os, time
import report as reportdemo

psw=''
dbname = "cs6400_sp21_team043"


class ProgramWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("LEOFURN Sales Reporting System (LSRS)")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,750,600)
        self.InitUI()

    def InitUI(self):
        self.tabWigdet()
        self.mainlayout()
        self.widget1()
        self.layout1()
        self.widget2()
        self.layout2()
        self.widget3()
        self.layout3()
        # self.holiday1()


    def tabWigdet(self):
        self.tabs=QTabWidget()
        self.tabs.setStyleSheet('QTabBar::tab { height: 50px; width: 150px; font-size: 16pt; }')#font-family: Courier;
        # self.tabs.currentChanged.connect(self.tabChanged)

        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"Reports")
        self.tabs.addTab(self.tab2,"Holiday")
        self.tabs.addTab(self.tab3,"City")

    def mainlayout(self):
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.addWidget(self.tabs)

    def layout1(self):
        L1 = QVBoxLayout()
        self.tab1.setLayout(L1)

        self.L11 = QVBoxLayout()
        self.L12 = QVBoxLayout()
        L1.addLayout(self.L11)
        L1.addLayout(self.L12)

        self.g1 = QGridLayout()
        self.l11 = QLabel("Count of stores")
        self.l12 = QLabel("Stores offer food (restaurant and-or snack bar)")
        self.l13 = QLabel("Stores offering childcare")
        self.l14 = QLabel("Count of products")
        self.l15 = QLabel("Distinct advertising campaigns")
        self.l16 = QLabel("")
        self.e11 = QLabel()
        self.e12 = QLabel()
        self.e13 = QLabel()
        self.e14 = QLabel()
        self.e15 = QLabel()

        self.g1.addWidget(self.l11, 0, 0)
        self.g1.addWidget(self.l12, 1, 0)
        self.g1.addWidget(self.l13, 2, 0)
        self.g1.addWidget(self.l14, 3, 0)
        self.g1.addWidget(self.l15, 4, 0)
        self.g1.addWidget(self.l16, 5, 0)

        self.g1.addWidget(self.e11, 0, 1)
        self.g1.addWidget(self.e12, 1, 1)
        self.g1.addWidget(self.e13, 2, 1)
        self.g1.addWidget(self.e14, 3, 1)
        self.g1.addWidget(self.e15, 4, 1)

        self.L11.addLayout(self.g1)

        self.L12.addWidget(self.btn1)
        self.L12.addWidget(self.btn2)
        self.L12.addWidget(self.btn3)
        self.L12.addWidget(self.btn4)
        self.L12.addWidget(self.btn5)
        self.L12.addWidget(self.btn6)
        self.L12.addWidget(self.btn7)
        self.L12.addWidget(self.btn8)
        self.L12.addWidget(self.btn9)

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()
            self.l16.setText("Database connected successfully!")
            # self.l16.setStyleSheet('background-color: cyan')
            self.l16.setStyleSheet('color: green')

            f = open('sql/Report0.sql', "r")
            s = f.read().split(';')

            sql = s[0]
            # sql = "SELECT COUNT(storeID) AS ‘num_store’ FROM Store;"
            mycursor.execute(sql)
            x = mycursor.fetchall()[0][0]
            self.e11.setText(str(x))

            sql = s[1]
            # sql = "SELECT COUNT(storeID) AS ‘num_storefood’ FROM Store WHERE has_restaurant = 1 OR has_snack_bar = 1;"
            mycursor.execute(sql)
            x = mycursor.fetchall()[0][0]
            self.e12.setText(str(x))

            sql = s[2]
            # sql = "SELECT COUNT(storeID) AS ‘num_childcare’ FROM Store WHERE childcare_limit != 'No childcare';"
            mycursor.execute(sql)
            x = mycursor.fetchall()[0][0]
            self.e13.setText(str(x))

            sql = s[3]
            # sql = "SELECT COUNT(PID) AS ‘num_product’ FROM Product;"
            mycursor.execute(sql)
            x = mycursor.fetchall()[0][0]
            self.e14.setText(str(x))

            sql = s[4]
            # sql = "SELECT COUNT(camp_description) AS ‘num_camp’ FROM AdCamp;"
            mycursor.execute(sql)
            x = mycursor.fetchall()[0][0]
            self.e15.setText(str(x))

        except mc.Error as e:
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn9.setEnabled(False)
            self.l16.setText("Cannot connect to database!")
            self.l16.setStyleSheet('color: red')


    def widget1(self):
        self.btn1 = QPushButton("Report1: View Products by Category")
        self.btn1.clicked.connect(self.report1)
        self.btn2 = QPushButton("Report2: Analyze Revenue for Couches and Sofas")
        self.btn2.clicked.connect(self.report2)
        self.btn3 = QPushButton("Report3: View Store Revenue by Year by State")
        self.btn3.clicked.connect(self.report3)

        self.btn4 = QPushButton("Report4: Analyze Sales for Outdoor Furniture on Groundhog Day")
        self.btn4.clicked.connect(self.report4)
        self.btn5 = QPushButton("Report5: View States with Highest Volume Sold by Category")
        self.btn5.clicked.connect(self.report5)
        self.btn6 = QPushButton("Report6: Calculate Revenue by Population Categories")
        self.btn6.clicked.connect(self.report6)

        self.btn7 = QPushButton("Report7: Analyze Sales by Volume for each Childcare Category")
        self.btn7.clicked.connect(self.report7)
        self.btn8 = QPushButton("Report8: Analyze Restaurant Impact on Sales by Categories")
        self.btn8.clicked.connect(self.report8)
        self.btn9 = QPushButton("Report9: Analyze Sales during Advertising Campaigns")
        self.btn9.clicked.connect(self.report9)


    def layout2(self):
        L2 = QVBoxLayout()
        self.tab2.setLayout(L2)

        self.L21 = QVBoxLayout()
        self.L22 = QVBoxLayout()
        L2.addLayout(self.L21, 80)
        L2.addLayout(self.L22, 20)

        self.l21 = QLabel("New Holiday Name")
        self.l22 = QLabel("New Holiday Date")
        self.l23 = QLabel("")
        self.e21 = QLineEdit("")

        self.e22 = QtWidgets.QDateEdit(calendarPopup=True)
        self.e22.setDateTime(QtCore.QDateTime.currentDateTime())

        self.L21.addWidget(self.tableWidget)

        self.L22.addWidget(self.btn21)
        self.L22.addWidget(self.l21)
        self.L22.addWidget(self.e21)
        self.L22.addWidget(self.l22)
        self.L22.addWidget(self.e22)
        self.L22.addWidget(self.btn22)
        self.L22.addWidget(self.l23)

    def widget2(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Holiday Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Date"))
        self.tableWidget.setObjectName("tableWidget")
        self.btn21 = QPushButton("View Holiday")
        self.btn21.clicked.connect(self.select_data)
        self.btn22 = QPushButton("Add Holiday")
        self.btn22.clicked.connect(self.func1)

    def layout3(self):
        L3 = QVBoxLayout()
        self.tab3.setLayout(L3)

        self.L31 = QVBoxLayout()
        L3.addLayout(self.L31)

        self.l31 = QLabel("Select State:")
        self.l32 = QLabel("Select City:")
        self.l33 = QLabel("")
        self.l34 = QLabel("Enter new population:")
        self.e31 = QLineEdit("")
        self.l35 = QLabel("")

        self.L31.addWidget(self.l31)
        self.L31.addWidget(self.drop1)
        self.L31.addWidget(self.l32)
        self.L31.addWidget(self.drop2)
        self.L31.addWidget(self.btn31)
        self.L31.addWidget(self.l33)
        self.L31.addWidget(self.l34)
        self.L31.addWidget(self.e31)
        self.L31.addWidget(self.btn32)
        self.L31.addWidget(self.l35)

    def widget3(self):
        self.drop1 = QComboBox()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=psw,
            database=dbname
        )
        mycursor = mydb.cursor()
        sql = 'select distinct state as s from City order by s ASC;'
        mycursor.execute(sql)
        y = mycursor.fetchall()
        n=len(y)
        x = []
        for i in range(n):
            x.append(str(y[i][0]))
        self.drop1.addItems(x)
        self.drop1.currentIndexChanged[str].connect(self.comboch)

        self.drop2 = QComboBox()
        self.comboch(x[0])

        self.btn31 = QPushButton("View current population")
        self.btn31.clicked.connect(self.func2)
        self.btn32 = QPushButton("Update population")
        self.btn32.clicked.connect(self.func3)


    def comboch(self,index):
        self.drop2.clear()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=psw,
            database=dbname
        )
        mycursor = mydb.cursor()
        sql = 'select city_name from city where state=\'' + index + '\';'
        mycursor.execute(sql)
        y = mycursor.fetchall()
        n=len(y)
        x = []
        for i in range(n):
            x.append(y[i][0])
        self.drop2.addItems(x)


    def DBConnect(self):
        try:
            db = mdb.connect('localhost', 'root', psw, dbname)
            QMessageBox.about(self, "Hint", "Database connected successfully!")
        except mdb.Error as e:
            QMessageBox.about(self, "Hint", "Failed to connect Database")

    def func1(self):
        x = self.e21.text()

        if not x:
            self.l23.setText("Holiday Name cannot be empty.")
            self.l23.setStyleSheet('color: red')
        elif x:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password=psw,
                    database=dbname
                )
                mycursor = mydb.cursor()

                sql = 'SELECT 1 FROM holiday WHERE holiday_name = \'' + x + '\';'
                mycursor.execute(sql)
                y = mycursor.fetchall()

                if len(y):
                    self.l23.setText('Holiday name exist! Please enter a different name.')
                else:
                    value = self.e22.date().toString("yyyy-MM-dd")
                    sql = "INSERT INTO holiday (holiday_name, date_attr) VALUES (%s, %s)"
                    val = (x, value)
                    try:
                        mycursor.execute(sql, val)
                        mydb.commit()
                        self.select_data()
                        self.l23.setText("Data Inserted Successfully!")
                        self.l23.setStyleSheet('color: green')
                    except mc.Error as e:
                        self.l23.setText("Error Inserting Data")
                        self.l23.setStyleSheet('color: red')

            except mc.Error as e:
                self.l23.setText("Cannot connect to database!")
                self.l23.setStyleSheet('color: red')


    def select_data(self):
        try:
            # dbname = self.lineEditDb.text()
            # tablename = self.lineEditTable.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM Holiday")

            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


        except mc.Error as e:
            print("Error")

    def func2(self):
        x = self.drop1.currentText() #state
        y = self.drop2.currentText() #city

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            # f = open('sql/Report0.sql', "r")
            # s = f.read().split(';')
            # sql = s[0]

            sql = "SELECT population FROM City WHERE city_name = %s AND state = %s;"
            val = (y, x)
            mycursor.execute(sql, val)

            pop = mycursor.fetchall()[0][0]
            self.l33.setText('Population is: ' + str(pop))

        except mc.Error as e:
            self.l35.setText("Database not connected.")
            self.l35.setStyleSheet('color: red')

    def func3(self):
        x = self.drop1.currentText() #state
        y = self.drop2.currentText() #city
        z = self.e31.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            # f = open('sql/Report0.sql', "r")
            # s = f.read().split(';')
            # sql = s[0]

            sql = "update City set population = %s WHERE city_name = %s AND state = %s;"
            val = (z, y, x)
            mycursor.execute(sql, val)
            mydb.commit()

            sql = "SELECT population FROM City WHERE city_name = %s AND state = %s;"
            val = (y, x)
            mycursor.execute(sql, val)
            pop = mycursor.fetchall()[0][0]
            self.l33.setText('Population is: ' + str(pop))
            self.l35.setText('Population has been updated.')
            self.l35.setStyleSheet('color: green')

        except mc.Error as e:
            self.l35.setText("Update error")
            self.l35.setStyleSheet('color: red')

    def report1(self):
        self.r1 = reportdemo.report1()

    def report2(self):
        self.r2 = reportdemo.report2()

    def report3(self):
        self.r3 = reportdemo.report3()

    def report4(self):
        self.r4 = reportdemo.report4()

    def report5(self):
        self.r5 = reportdemo.report5()

    def report6(self):
        self.r6 = reportdemo.report6()

    def report7(self):
        self.r7 = reportdemo.report7()

    def report8(self):
        self.r8 = reportdemo.report8()

    def report9(self):
        self.r9 = reportdemo.report9()

def main():
    APP=QApplication(sys.argv)
    window=ProgramWindow()
    window.show()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
