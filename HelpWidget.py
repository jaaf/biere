'''
Copyright José FOURNIER 2023

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

from HelpWidgetBase import Ui_helpWidget as hw
from PyQt6.QtWidgets import QWidget,QVBoxLayout,QPushButton
from PyQt6 import QtCore
from PyQt6.QtCore import Qt,QRegularExpression,QTimer,QSize
from database.fermentables.fermentable_brand import all_fbrand, find_fbrand_by_name
from PyQt6 import QtGui
import copy
import jsonpickle
from database.profiles.rest import Rest
from PyQt6.QtGui import QDoubleValidator,QRegularExpressionValidator,QIntValidator

class HelpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui =hw()
        self.ui.setupUi(self)

        self.resize(QSize(1600,800))
        self.vl=QVBoxLayout()
        self.chapter1Button=QPushButton('Introduction')
        self.chapter2Button=QPushButton("Présentation de l'interface")
        self.chapter3Button=QPushButton("Principe des saisies d'ingrédients dans une recette")
        self.vl.addWidget(self.chapter1Button)
        self.vl.addWidget(self.chapter2Button)
        self.vl.addWidget(self.chapter3Button)
        self.ui.groupBox.setMaximumWidth(200)
        self.ui.groupBox.setLayout(self.vl)
        self.set_connections()

    def set_connections(self):
        self.chapter1Button.clicked.connect(lambda: self.show_chapter('1')) 
        self.chapter2Button.clicked.connect(lambda: self.show_chapter('2')) 
        self.chapter3Button.clicked.connect(lambda: self.show_chapter('3'))

    def show_chapter(self,nb):
        filename="help/Head.html"
        prepend=open(filename,'r',encoding="utf-8").read()
        filename="help/GeneralHelp/chapter"+str(nb)+".html"
          
        text=open(filename,'r',encoding="utf-8").read()
        self.ui.textEdit.setHtml(prepend+text) 
