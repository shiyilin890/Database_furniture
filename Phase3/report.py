from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import mysql.connector as mc
import MySQLdb as mdb
import sys, os, time

psw=''
dbname = "cs6400_sp21_team043"

class report1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 1")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,650,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addStretch()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.L1.addStretch()
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("View Products by Category")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func1)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Category Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Total Products"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Minimum Price"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Average Price"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Maximum Price"))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(450,150,650,550)

    def func1(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            sqlFile = open('sql/Report1.sql', 'r')
            sql = sqlFile.read().rstrip()
            mycursor.execute(sql)
            x = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mdb.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")


class report2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 2")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,950,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addStretch()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.L1.addStretch()
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Analyze Revenue for Couches and Sofas")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func2)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Retail\n Price"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Total Units \nSold"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Discount Units \nSold"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Retail \nUnits Sold"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Actual \nRevenue"))
        self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem("Predicted \nRevenue"))
        self.tableWidget.setHorizontalHeaderItem(8, QTableWidgetItem("Revenue \nDifference"))
        self.tableWidget.setObjectName("tableWidget")

    def func2(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            sqlFile = open('sql/Report2.sql', 'r')
            sql = sqlFile.read().rstrip()

            mycursor.execute(sql)
            x = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mdb.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")


class report3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 3")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,550,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.label2)
        self.L1.addWidget(self.qcbox)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Store ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Store address"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("City name"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Sales year"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Total revenue"))
        self.tableWidget.setObjectName("tableWidget")

        self.label1 = QLabel("View Store Revenue by Year by State:")
        self.label2 = QLabel("Select a state:")

        self.qcbox = QComboBox()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=psw,
            database=dbname
        )
        mycursor = mydb.cursor()
        sql = 'SELECT DISTINCT state FROM City ORDER BY state;'
        mycursor.execute(sql)
        y = mycursor.fetchall()
        n=len(y)
        x = []
        for i in range(n):
            x.append(str(y[i][0]))
        self.qcbox.addItems(x)

        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func3)

    def func3(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report3.sql', "r")
            sqlFile = f.read()
            f.close()
            sql = sqlFile.split(';')
            state = self.qcbox.currentText()
            for command in sql:
                try:
                    command = command.replace('$state', state)
                    mycursor.execute(command)
                except mdb.Error as e:
                    QMessageBox.about("Connect", "Failed to connect Database")
            x = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")



class report4(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 4")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(350, 150, 550, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Analyze Sales for Outdoor Furniture on Groundhog Day:")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func4)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Sales year"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Total units sold per year"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Avg units sold per day"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Total units sold on GroundHog Day"))
        self.tableWidget.setObjectName("tableWidget")

    def func4(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()
            f = open('sql/Report4.sql', "r")
            sqlFile = f.read()
            f.close()
            sql = sqlFile.split(';')
            for command in sql:
                try:
                    mycursor.execute(command)
                except mdb.Error as e:
                    QMessageBox.about("Connect", "Failed to connect Database")
            x = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")



class report5(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 5")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.label2)
        self.L1.addWidget(self.e51)
        self.L1.addWidget(self.label3)
        self.L1.addWidget(self.e52)

        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Catetory name"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("State sold highest"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Units sold in state"))
        self.tableWidget.setObjectName("tableWidget")

        self.label1 = QLabel("View States with Highest Volume Sold by Category:")
        self.label2 = QLabel("Select a year:")
        self.label3 = QLabel("Select a month:")
        self.e51 = QComboBox()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=psw,
            database=dbname
        )
        mycursor = mydb.cursor()
        sql = 'select distinct YEAR(date_attr) as yy from Sold order by yy ASC;'
        mycursor.execute(sql)
        y = mycursor.fetchall()
        n=len(y)
        x = []
        for i in range(n):
            x.append(str(y[i][0]))
        self.e51.addItems(x)
        self.e51.currentIndexChanged[str].connect(self.comboch)

        self.e52 = QComboBox()
        self.comboch(x[0])

        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func5)

    def func5(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report5.sql', "r")
            s = f.read().split(';')
            sql = s[1]

            month = self.e52.currentText()
            year = self.e51.currentText()
            sql = sql.replace('$month', month)
            sql = sql.replace('$year', year)
            mycursor.execute(sql)
            x = mycursor.fetchall()
            # print(x)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")

    def comboch(self,index):
        self.e52.clear()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=psw,
            database=dbname
        )
        mycursor = mydb.cursor()
        sql = 'select distinct MONTH(date_attr) as m from Sold where YEAR(date_attr)=' + index + ' order by m;'
        mycursor.execute(sql)
        y = mycursor.fetchall()
        n=len(y)
        x = []
        for i in range(n):
            x.append(str(y[i][0]))
        self.e52.addItems(x)


class report6(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 6")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 600, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Calculate Revenue by Population Categories:")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func6)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Year"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Small City"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Medium City"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Large City"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Extra Large City"))
        self.tableWidget.setObjectName("tableWidget")

    def func6(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report6.sql', "r")
            s = f.read().split(';')
            sql = s[0]

            mycursor.execute(sql)
            x = mycursor.fetchall()
            # print(x)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")


class report7(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 7")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 600, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Analyze Sales by Volume for each Childcare Category")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func7)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Month"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("No \nChildcare Service"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Short \nChildcare Service"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Long \nChildcare Service"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Full \nChildcare Service"))
        self.tableWidget.setObjectName("tableWidget")

    def func7(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report7.sql', "r")
            s = f.read().split(';')
            sql=s[0]
            mycursor.execute(sql)
            x = mycursor.fetchall()
            # print(x)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")


class report8(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 8")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Analyze Restaurant Impact on Sales by Categories")
        self.btn1 = QPushButton("Get Report")
        self.btn1.clicked.connect(self.func8)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Category"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Store Type"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Quantity Sold"))
        self.tableWidget.setObjectName("tableWidget")

    def func8(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report8.sql', "r")
            s = f.read().split(';')
            sql=s[0]
            mycursor.execute(sql)
            x = mycursor.fetchall()
            # print(x)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    y = str(data)
                    # print(y)
                    if y=='1':
                        y = 'Restaurant'
                    if y=='0':
                        y = 'Non-Restaurant'
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(y))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Failed to connect Database")


class report9(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report 9")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 600, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.label1)
        self.L1.addWidget(self.btn1)
        self.L1.addWidget(self.tableWidget)
        self.setLayout(self.L1)

    def widgets(self):
        self.label1 = QLabel("Analyze Sales during Advertising Campaigns")
        self.btn1 = QPushButton("Get Report: top 10 + bottom 10")
        self.btn1.clicked.connect(self.func9)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Product \nName"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Sold During \nCampaign"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Sold Outside \nCampaign"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Difference"))
        self.tableWidget.setObjectName("tableWidget")

    def func9(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=psw,
                database=dbname
            )
            mycursor = mydb.cursor()

            f = open('sql/Report9.sql', "r")
            s = f.read().split(';')

            k=len(s)
            for i in range(k-1):
                mycursor.execute(s[i])

            mycursor.execute(s[k-1])
            x = mycursor.fetchall()


            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(x):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.about(self, "Connect", "Query Failed")


