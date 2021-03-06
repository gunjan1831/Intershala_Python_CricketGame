# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_bnew.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
cricket=sqlite3.connect("cricket.db")
c=cricket.cursor()

class Ui_Dialog(object):
    def team_evaluate(self):
     try:
        self.listWidget.clear()
        self.listWidget_2.clear()
        team_name=self.comboBox.currentText()
        sql="select distinct players from teams where name='"+team_name+"'"
        players=[player[0] for player in c.execute(sql)]
        self.listWidget.addItems(players)
        for player in players:
            sql="select * from match where Player='"+player+"'"
            c.execute(sql)
            match=c.fetchone()
            value=0
            if match[1]!=0:
                value+=match[1]//2
            if match[1]>=50:
                value+=5
            if match[1]>=100:
                value+=10
            if match[2]!=0:
                sr=(match[1]/match[2])*100
                if sr>=80 and sr<100:
                    value+=2
                if sr>=100:
                    value+=4
            value+=match[3]
            value+=match[4]*2
            value+=match[8]*10
            if match[8]>=3:
                value+=5
            if match[8]>=5:
                value+=10
            if match[5]!=0:    
                er=(match[7]/match[5])*6
                if er<=4.5 and er>3.5:
                    value+=4
                if er<=3.5 and er>2:
                    value+=7
                if er<=2:
                    value+=10
            value+=(match[9]+match[10]+match[11])*10
            c.execute("update teams set value=%d where players='%s'"%(value, player))
            cricket.commit()
        sql="select value from teams where name='"+team_name+"'"
        values=[value[0] for value in c.execute(sql)]
        tot=0
        for value in values:
            tot+=value
            self.listWidget_2.addItem(str(value))
        self.label_3.setText(str(tot))
     except Exception as e:
         print(e)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(957, 638)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(60, 120, 821, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 90, 241, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        sql="select  distinct name from teams"
        allnames=[all_teams[0] for all_teams in c.execute(sql)]
        self.comboBox.addItems(allnames)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 90, 241, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 50, 571, 19))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 200, 801, 371))
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 371, 361))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: white")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.setGeometry(QtCore.QRect(435, 1, 361, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet("background-color: white")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 68, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 160, 68, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(500, 160, 68, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 590, 131, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: green")
        self.pushButton.clicked.connect(self.team_evaluate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Team"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Match 1"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Match 2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Match 3 "))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Match 4"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Match 5"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Evaluate the Performance of your Fantasy Team</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#0084ff;\">Players</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "-"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#0084ff;\">Points</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
