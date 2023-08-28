'''
Copyright José FOURNIER 2023

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

from database.recipes.recipe import all_recipe
from ListModels import RecipeListModel
from PyQt6.QtWidgets import QListView,QVBoxLayout,QHBoxLayout,QPushButton,QSpacerItem,QWidget,QLabel,QComboBox
from PyQt6 import QtCore,QtWidgets
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QIcon,QPalette,QFont
from RecipeWidget import RecipeWidget



class RecipeListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent
        self.icon_path='base-data/icons/'
        self.icon_size=QSize(32,32)
        self.newButton=QPushButton()
        self.sortButton=QPushButton()
        self.listView=QListView()
        self.selection=None
        self.recipeWidget=None
        

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
        self.sortCombo=QComboBox()
        self.sortCombo.addItem("")
        self.sortCombo.addItem('Nom-Style-Type')
        self.sortCombo.addItem("Style-Type-Nom")
        self.sortCombo.addItem("Type-Style-Nom")
        self.sortButton.setIcon(QIcon(self.icon_path+'sort-list-alt-svgrepo-com.svg'))
        self.sortButton.setIconSize(self.icon_size)
        self.sortButton.setMaximumSize(40,40)
        toolbarLayout=QHBoxLayout()
        self.newButton.setIcon(QIcon(self.icon_path+'add-square-svgrepo-com.svg'))
        self.newButton.setIconSize(self.icon_size)
        self.newButton.setMaximumSize(40,40)
        self.newButton.setToolTip('Ajouter une recette')
        self.sortButton.setIcon(QIcon(self.icon_path+'sort-list-alt-svgrepo-com.svg'))
        self.sortButton.setIconSize(self.icon_size)
        self.sortButton.setMaximumSize(40,40)
        self.sortButton.setToolTip('Trier les recettes')
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        spacerItemSmall = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        toolbarLayout.addItem(spacerItem)
        toolbarLayout.addWidget(self.sortButton)
        toolbarLayout.addWidget(self.sortCombo)
        toolbarLayout.addWidget(self.newButton)
        toolbarLayout.setSpacing(20)

        #create a title bar
        titlebarLayout=QHBoxLayout()
        self.titleLabel=QLabel()
        self.titleLabel.setText('LISTE DES RECETTES')
        self.titleLabel.setStyleSheet('padding:5px;font-size: 20px; font-weight:bold; color:'+self.WinFg)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        titlebarLayout.addWidget(self.titleLabel) 
        titlebarLayout.addItem(spacerItem)

        #setting the model for list view
        listLayout=QVBoxLayout()
        self.recipes=all_recipe()
        self.recipes.sort(key=lambda x: (x.id,x.name))
        self.model=RecipeListModel(recipes=self.recipes)
        font=QFont("Liberation Mono")
        #font=self.font().setStyle(QFont.styleItalic)
        self.listView.setFont(font)
        self.listView.setModel(self.model)
        self.listView.setSpacing(8)
        listLayout.addWidget(self.listView)

        #compose widget layout
        mainLayout=QVBoxLayout()
        mainLayout.addLayout(toolbarLayout)
        mainLayout.addLayout(titlebarLayout)
        mainLayout.addLayout(listLayout)
        self.setLayout(mainLayout)
     
        #set connections
        self.newButton.clicked.connect(self.new_recipe)
        self.listView.clicked.connect(self.select_recipe)
        self.sortCombo.currentTextChanged.connect(lambda: self.sort_list(self.sortCombo.currentText()))
        

    def sort_list(self, mode):
        #self.source_list.sort(key=lambda x: (x.brand,x.name,x.version))
        match mode:
            case "":
                self.model.recipes.sort(key=lambda x: (x.id))
            case 'Nom-Style-Type':
                self.model.recipes.sort(key=lambda x: (x.name,x.style,x.rtype))
            case "Style-Type-Nom":
                self.model.recipes.sort(key=lambda x: (x.style,x.rtype,x.name))
            case "Type-Style-Nom":
                self.model.recipes.sort(key=lambda x: (x.rtype,x.style,x.name))
        self.model.layoutChanged.emit()   
    

    def select_recipe(self):
        #print('LIST VIEW CLICKED')
        indexes = self.listView.selectedIndexes()
        if indexes:
            index=indexes[0]
            self.selection=self.model.recipes[index.row()]
            self.recipeWidget=RecipeWidget(self.selection.id,self)
            stackIndex=self.parent.swapWidget('recipe',self.recipeWidget)
            self.parent.stackedWidget.setCurrentIndex(stackIndex)

   
    def new_recipe(self):
        self.recipeWidget=RecipeWidget(None,self)#we pass the parent i.e. RecipeListWidget as parent sans Id
        stackIndex=self.parent.swapWidget('recipe',self.recipeWidget)

        #print('stackIndex is '+str(stackIndex))
        #self.recipeWidget.setCurrentStackIndex(stackIndex)#pass the index to the recipe editor 
        self.parent.stackedWidget.setCurrentIndex(stackIndex)
     

