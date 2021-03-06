from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from project import get_final_movie_info_list, get_movies_info_from_file
import os

class Ui_MovieLibrary(object):

    def setupUi(self, MovieLibrary):
        MovieLibrary.setObjectName("MovieLibrary")
        MovieLibrary.resize(659, 537)
        self.centralwidget = QtWidgets.QWidget(MovieLibrary)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(30, 480, 131, 31))
        self.b1.setObjectName("b1")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 661, 451))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Movie IMDb ID"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Movie Title"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Year"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Quality"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("IMDb Rating"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Movie Director"))
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.saving = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(180, 480, 101, 21))
        self.saving.setGeometry(QtCore.QRect(500, 480, 500, 21))
        self.loading.setText("")
        self.saving.setText("")
        self.loading.setObjectName("loading")
        self.saving.setObjectName("saving")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(350, 480, 131, 31))
        self.b2.setObjectName("b2")
        MovieLibrary.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MovieLibrary)
        self.statusbar.setObjectName("statusbar")
        MovieLibrary.setStatusBar(self.statusbar)
        self.actionAdd_file = QtWidgets.QAction(MovieLibrary)
        self.retranslateUi(MovieLibrary)
        QtCore.QMetaObject.connectSlotsByName(MovieLibrary)



    def retranslateUi(self, MovieLibrary):
        _translate = QtCore.QCoreApplication.translate
        MovieLibrary.setWindowTitle(_translate("MovieLibrary", "MovieLibrary"))
        self.b1.setText(_translate("MovieLibrary", "Load file"))
        self.b1.clicked.connect(self.button_press )
        self.b2.setText(_translate("MovieLibrary", "Save results"))
        self.b2.clicked.connect(self.save_results )

    def open_dialog_box(self):
        file_name = QFileDialog.getOpenFileName()
        path = file_name[0]
        
        with open(path, "r") as f:
            list1 = get_movies_info_from_file(path)
            # for i in list1:
            #     print(i)
            final_list = get_final_movie_info_list(list1)
            # for i in final_list:
            #     print(i)
        self.loading.setText("Done loading")  
        self.tableWidget.setRowCount(len(final_list) + 1 )  # now we know how many columns we have
        i = 1
        for row in final_list: 
            # print(1, row)   
            self.tableWidget.setItem(i,0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(i,2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(i,3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(i,5, QTableWidgetItem(row[5]))
            i += 1
        self.tableWidget.resizeColumnsToContents()
        

    
    def button_press(self):
        self.open_dialog_box()

    def save_results(self, final_list):
        self.load_rows(final_list)

        self.saving.setText("Done Saving to Desktop")

    def load_rows(self, final_list):
        with open(fr'C:/Users/{os.getlogin()}/Desktop/results.txt', 'w', encoding='utf-8') as stream:    
            for row in range(self.tableWidget.rowCount()):
                rowdata = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                stream.writelines(str(rowdata)+'\n')
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MovieLibrary = QtWidgets.QMainWindow()
    ui = Ui_MovieLibrary()
    ui.setupUi(MovieLibrary)
    MovieLibrary.show()
    sys.exit(app.exec_())
