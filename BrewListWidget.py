
'''
Copyright José FOURNIER 2023

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
from database.brews.brew import all_brew
from ListModels import BrewListModel
from PyQt6.QtWidgets import QListView,QVBoxLayout,QHBoxLayout,QPushButton,QSpacerItem,QWidget,QLabel
from PyQt6 import QtCore,QtWidgets
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QIcon,QPalette
from BrewWidget import BrewWidget



class BrewListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent
        self.icon_path='base-data/icons/'
        self.icon_size=QSize(32,32)
        self.sortButton=QPushButton()
        self.listView=QListView()
        self.selection=None
        
        self.brewWidget=None

        #set connections
        self.listView.clicked.connect(self.select_brew)

    def setup_gui(self):  
        #define colors
        pal=QPalette()
        pal=self.parent.palette()
        HighlightBg= pal.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight) 
        WindowBg= pal.color(QPalette.ColorGroup.Active, QPalette.ColorRole.Window)
        WindowFg= pal.color(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText)
        HighlightFg=pal.color(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText)
        self.WinFg=WindowFg.name()
        self.WinBg=WindowBg.name()
        self.HlBg=HighlightBg.name()
        self.HlFg=HighlightFg.name() 

        #create a toolbar
        toolbarLayout=QHBoxLayout()
   
        self.sortButton.setIcon(QIcon(self.icon_path+'sort-list-alt-svgrepo-com.svg'))
        self.sortButton.setIconSize(self.icon_size)
        self.sortButton.setMaximumSize(40,40)
        self.sortButton.setToolTip('Trier les recettes')
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        spacerItemSmall = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        toolbarLayout.addItem(spacerItem)
        toolbarLayout.addWidget(self.sortButton)
        toolbarLayout.setSpacing(20)

        #create a title bar
        titlebarLayout=QHBoxLayout()
        self.titleLabel=QLabel()
        self.titleLabel.setText('LISTE DES SESSIONS DE BRASSAGE')
        self.titleLabel.setStyleSheet('padding:5px;font-size: 20px; font-weight:bold; color:'+self.WinFg)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        titlebarLayout.addWidget(self.titleLabel) 
        titlebarLayout.addItem(spacerItem)


        #setting the model for list view
        listLayout=QVBoxLayout()
        self.brews=all_brew()
        self.brews.sort(key=lambda x: x.brew_date)
        self.model=BrewListModel(brews=self.brews)
        self.listView.setModel(self.model)
        self.listView.setSpacing(8)
        listLayout.addWidget(self.listView)

        #compose the widget layout
        mainLayout=QVBoxLayout()
        mainLayout.addLayout(toolbarLayout)
        mainLayout.addLayout(titlebarLayout)
        mainLayout.addLayout(listLayout)
        #listLayout.setContentsMargins(30,30,30,30)
        self.setLayout(mainLayout)

    def select_brew(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index=indexes[0]
            self.selection=self.model.brews[index.row()]
            self.brewWidget=BrewWidget(self.selection.id,None,self)
            #print(self.brewWidget)
            self.parent.brewTabWidget.addTab(self.brewWidget,self.brewWidget.nameEdit.text())
            stackIndex=self.parent.swapWidget('brew',self.parent.brewTabWidget)# ('brew',self.brewWidget)
            self.parent.stackedWidget.setCurrentIndex(stackIndex)
           

    def edit_brew(self):
        self.dlg=BrewWidget(self.selection.id,self)
        self.dlg.show()

    def delete_brew(self):
        pass    

    def new_brew(self):#not used at the moment
        #print('creating new brew')
        self.brewWidget=BrewWidget(None,self.parent)#we pass the parent i.e. MainWindow as parent
        self.brewWidget.show() 
        self.model.brews=all_brew()  
        self.model.layoutChanged.emit()
      


