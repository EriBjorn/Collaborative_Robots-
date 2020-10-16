# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colab_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.WidgetMenu = QtWidgets.QWidget(self.centralwidget)
        self.WidgetMenu.setMaximumSize(QtCore.QSize(500, 16777215))
        self.WidgetMenu.setObjectName("WidgetMenu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.WidgetMenu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.WidgetJustifier = QtWidgets.QWidget(self.WidgetMenu)
        self.WidgetJustifier.setObjectName("WidgetJustifier")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.WidgetJustifier)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LogoJustifier = QtWidgets.QWidget(self.WidgetJustifier)
        self.LogoJustifier.setObjectName("LogoJustifier")
        self.gridLayout_3.addWidget(self.LogoJustifier, 0, 0, 1, 1)
        self.PageSelectors = QtWidgets.QFrame(self.WidgetJustifier)
        self.PageSelectors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PageSelectors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PageSelectors.setObjectName("PageSelectors")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PageSelectors)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Demo1PageBtn = QtWidgets.QCommandLinkButton(self.PageSelectors)
        self.Demo1PageBtn.setObjectName("Demo1PageBtn")
        self.verticalLayout.addWidget(self.Demo1PageBtn)
        self.Demo2PageBtn = QtWidgets.QCommandLinkButton(self.PageSelectors)
        self.Demo2PageBtn.setObjectName("Demo2PageBtn")
        self.verticalLayout.addWidget(self.Demo2PageBtn)
        self.Demo3PageBtn = QtWidgets.QCommandLinkButton(self.PageSelectors)
        self.Demo3PageBtn.setObjectName("Demo3PageBtn")
        self.verticalLayout.addWidget(self.Demo3PageBtn)
        self.AboutPageBtn = QtWidgets.QCommandLinkButton(self.PageSelectors)
        self.AboutPageBtn.setObjectName("AboutPageBtn")
        self.verticalLayout.addWidget(self.AboutPageBtn)
        self.gridLayout_3.addWidget(self.PageSelectors, 1, 0, 1, 1)
        self.NightModeOrg = QtWidgets.QWidget(self.WidgetJustifier)
        self.NightModeOrg.setObjectName("NightModeOrg")
        self.gridLayout_3.addWidget(self.NightModeOrg, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.WidgetJustifier, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.WidgetMenu, 0, 0, 1, 1)
        self.Widget_Contents = QtWidgets.QWidget(self.centralwidget)
        self.Widget_Contents.setObjectName("Widget_Contents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Widget_Contents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.WidgetPages = QtWidgets.QStackedWidget(self.Widget_Contents)
        self.WidgetPages.setObjectName("WidgetPages")
        self.Demo1Page = QtWidgets.QWidget()
        self.Demo1Page.setObjectName("Demo1Page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Demo1Page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Demo1Label = QtWidgets.QLabel(self.Demo1Page)
        self.Demo1Label.setTextFormat(QtCore.Qt.PlainText)
        self.Demo1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Demo1Label.setObjectName("Demo1Label")
        self.verticalLayout_2.addWidget(self.Demo1Label)
        self.StartDemo1Btn = QtWidgets.QPushButton(self.Demo1Page)
        self.StartDemo1Btn.setObjectName("StartDemo1Btn")
        self.verticalLayout_2.addWidget(self.StartDemo1Btn)
        self.StopDemo1Btn = QtWidgets.QPushButton(self.Demo1Page)
        self.StopDemo1Btn.setObjectName("StopDemo1Btn")
        self.verticalLayout_2.addWidget(self.StopDemo1Btn)
        self.WidgetPages.addWidget(self.Demo1Page)
        self.Demo2Page = QtWidgets.QWidget()
        self.Demo2Page.setObjectName("Demo2Page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Demo2Page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Demo2Label = QtWidgets.QLabel(self.Demo2Page)
        self.Demo2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Demo2Label.setObjectName("Demo2Label")
        self.verticalLayout_3.addWidget(self.Demo2Label)
        self.StartDemo2Btn = QtWidgets.QPushButton(self.Demo2Page)
        self.StartDemo2Btn.setObjectName("StartDemo2Btn")
        self.verticalLayout_3.addWidget(self.StartDemo2Btn)
        self.StopDemo2Btn = QtWidgets.QPushButton(self.Demo2Page)
        self.StopDemo2Btn.setObjectName("StopDemo2Btn")
        self.verticalLayout_3.addWidget(self.StopDemo2Btn)
        self.WidgetPages.addWidget(self.Demo2Page)
        self.horizontalLayout.addWidget(self.WidgetPages)
        self.gridLayout.addWidget(self.Widget_Contents, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Demo1PageBtn.toggled['bool'].connect(self.WidgetPages.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Demo1PageBtn.setText(_translate("MainWindow", "Demo 1: Easy Assembly"))
        self.Demo2PageBtn.setText(_translate("MainWindow", "Demo 2: Name Pending"))
        self.Demo3PageBtn.setText(_translate("MainWindow", "Demo 3: Name Pending"))
        self.AboutPageBtn.setText(_translate("MainWindow", "About this project"))
        self.Demo1Label.setText(_translate("MainWindow", "Demo 1: Easy Assembly"))
        self.StartDemo1Btn.setText(_translate("MainWindow", "Start Demo 1"))
        self.StopDemo1Btn.setText(_translate("MainWindow", "Stop Demo 1"))
        self.Demo2Label.setText(_translate("MainWindow", "Demo 2: Name Pending"))
        self.StartDemo2Btn.setText(_translate("MainWindow", "Start Demo 2"))
        self.StopDemo2Btn.setText(_translate("MainWindow", "Stop Demo 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())