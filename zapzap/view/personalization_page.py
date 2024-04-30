from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/personalization_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Personalization(object):
    def setupUi(self, Personalization):
        Personalization.setObjectName("Personalization")
        Personalization.resize(565, 525)
        Personalization.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Personalization)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Personalization)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 565, 525))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.appThemeCBox = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.appThemeCBox.setObjectName("appThemeCBox")
        self.verticalLayout.addWidget(self.appThemeCBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.disableTrayIcon = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents)
        self.disableTrayIcon.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.disableTrayIcon.setObjectName("disableTrayIcon")
        self.gridLayout.addWidget(self.disableTrayIcon, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.trayIconCBox = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.trayIconCBox.setObjectName("trayIconCBox")
        self.gridLayout.addWidget(self.trayIconCBox, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 312, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Personalization)
        QtCore.QMetaObject.connectSlotsByName(Personalization)

    def retranslateUi(self, Personalization):
        
        self.label.setText(_("Personalization"))
        self.label_2.setText(_("Theme"))
        self.label_3.setText(_("Application theme"))
        self.disableTrayIcon.setText(_("On"))
        self.label_4.setText(_("Tray icon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Personalization = QtWidgets.QWidget()
    ui = Ui_Personalization()
    ui.setupUi(Personalization)
    Personalization.show()
    sys.exit(app.exec())
