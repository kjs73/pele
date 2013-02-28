# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dgraph_browser.ui'
#
# Created: Thu Feb 28 16:50:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(834, 572)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = MPLWidgetWithToolbar(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.chkbx_center_gmin = QtGui.QCheckBox(self.layoutWidget)
        self.chkbx_center_gmin.setObjectName(_fromUtf8("chkbx_center_gmin"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.chkbx_center_gmin)
        self.lineEdit_Emax = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Emax.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_Emax.setObjectName(_fromUtf8("lineEdit_Emax"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_Emax)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.chkbx_show_minima = QtGui.QCheckBox(self.layoutWidget)
        self.chkbx_show_minima.setObjectName(_fromUtf8("chkbx_show_minima"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.chkbx_show_minima)
        self.lineEdit_subgraph_size = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_subgraph_size.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_subgraph_size.setObjectName(_fromUtf8("lineEdit_subgraph_size"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_subgraph_size)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_nlevels = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_nlevels.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_nlevels.setObjectName(_fromUtf8("lineEdit_nlevels"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_nlevels)
        self.chkbx_order_by_energy = QtGui.QCheckBox(self.layoutWidget)
        self.chkbx_order_by_energy.setObjectName(_fromUtf8("chkbx_order_by_energy"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.chkbx_order_by_energy)
        self.chkbx_order_by_basin_size = QtGui.QCheckBox(self.layoutWidget)
        self.chkbx_order_by_basin_size.setObjectName(_fromUtf8("chkbx_order_by_basin_size"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.chkbx_order_by_basin_size)
        self.chkbx_include_gmin = QtGui.QCheckBox(self.layoutWidget)
        self.chkbx_include_gmin.setObjectName(_fromUtf8("chkbx_include_gmin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.chkbx_include_gmin)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnRebuild = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRebuild.sizePolicy().hasHeightForWidth())
        self.btnRebuild.setSizePolicy(sizePolicy)
        self.btnRebuild.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnRebuild.setObjectName(_fromUtf8("btnRebuild"))
        self.gridLayout_2.addWidget(self.btnRebuild, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnRebuild, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.rebuild_disconnectivity_graph)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_center_gmin.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>make sure the global minimum is centered</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_center_gmin.setText(QtGui.QApplication.translate("Form", "center global min", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>set the maximum energy level</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Emax", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_show_minima.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>show the minima as points at the end of each line</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_show_minima.setText(QtGui.QApplication.translate("Form", "show minima", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>change the minimum size of a disconnected region to be included in the graph</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Minimum subgraph size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "nlevels", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_order_by_energy.setText(QtGui.QApplication.translate("Form", "order_by_energy", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_order_by_basin_size.setText(QtGui.QApplication.translate("Form", "order_by_basin_size", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbx_include_gmin.setText(QtGui.QApplication.translate("Form", "include global min", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRebuild.setText(QtGui.QApplication.translate("Form", "Rebuild Graph", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MPLWidgetWithToolbar
