
'''
copyright José FOURNIER 2023

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from profile.EquipmentDialogWidget import EquipmentDialogWidget
from profile.RestDialog import RestDialog
from profile.StyleDialog import StyleDialog
from profile.WaterDialogWidget import WaterDialogWidget
from profile.WaterTargetDialogWidget import WaterTargetDialogWidget

from PyQt6 import  QtWidgets,QtGui
from PyQt6.QtCore import QSize,pyqtSignal
from PyQt6.QtGui import QAction, QActionGroup, QIcon
from PyQt6.QtWidgets import QMenu, QStackedWidget, QTabWidget, QVBoxLayout

from BrewListWidget import BrewListWidget
from commons.CountryDialog import CountryDialog
from fermentable.BrandDialog import BrandDialog
from fermentable.FermentableInventoryWidget import FermentableInventoryWidget
from HelpWidget import HelpWidget
from hop.HopInventoryWidget import HopInventoryWidget
from hop.SupplierDialog import SupplierDialog
from ImportDialog import ImportDialog
from MoveInitFilesDialog import MoveInitFilesDialog
from MainWindowBase import Ui_MainWindowBase
from misc.MiscInventoryWidget import MiscInventoryWidget
from RecipeListWidget import RecipeListWidget
from yeast.YBrandDialog import YBrandDialog
from yeast.YeastInventoryWidget import YeastInventoryWidget
from FontDialogWidget import FontDialogWidget
from SignalObject import SignalObject
from HelpMessage import HelpMessage
import sys
from pathlib import Path
from ConfirmationDialog import ConfirmationDialog
import logging


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindowBase):
    keyboard_signal=pyqtSignal(SignalObject)
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.WinBg=None
        log=logging.getLogger(__name__)
        path1=Path(__file__).parent.resolve()
        self.this_file_path=Path(__file__).parent
        self.icon_path=str(path1)+"/base-data/icons/" #a string
        self.recipeListWidget=RecipeListWidget(self)
        self.recipeListWidget.setup_gui()
        self.brewListWidget=BrewListWidget(self)
        self.brewListWidget.setup_gui()
        self.fermentableInventoryWidget=FermentableInventoryWidget(self)
        self.hopInventoryWidget=HopInventoryWidget(self)
        self.yeastInventoryWidget=YeastInventoryWidget(self)
        self.miscInventoryWidget=MiscInventoryWidget(self)
        self.equipmentDialogWidget=EquipmentDialogWidget(self)
        self.waterDialogWidget=WaterDialogWidget(self)
        self.waterTargetDialogWidget=WaterTargetDialogWidget(self)
        self.stackedWidget=QStackedWidget()


        self.stackedWidget.addWidget(self.recipeListWidget)

        self.brewTabWidget=QTabWidget()
        self.stackedWidget.addWidget(self.brewListWidget)
        self.stackedWidget.addWidget(self.fermentableInventoryWidget)
        self.stackedWidget.addWidget(self.hopInventoryWidget)
        self.stackedWidget.addWidget(self.yeastInventoryWidget)
        self.stackedWidget.addWidget(self.miscInventoryWidget)
        self.stackedWidget.addWidget(self.equipmentDialogWidget)
        self.stackedWidget.addWidget(self.waterDialogWidget)
        self.stackedWidget.addWidget(self.waterTargetDialogWidget)
        layout=QVBoxLayout()
        
        layout.addWidget(self.stackedWidget)
        self.centralwidget.setLayout(layout)
        
        
        #left tool bar

        actionGroup=QActionGroup(self)
        actionGroup.setExclusive(True)

        self.actionToolRecipes=QAction(QIcon(self.icon_path+'recipe-svgrepo-com.svg'),"Mes recettes", self)
        self.toolBar.addAction(self.actionToolRecipes)
        self.actionToolRecipes.setCheckable(1)
        actionGroup.addAction(self.actionToolRecipes)

        self.actionToolBrews=QAction(QIcon(self.icon_path+'beer-svgrepo-com.svg'),'Mes sessions',self)
        self.toolBar.addAction(self.actionToolBrews)
        self.actionToolBrews.setCheckable(1)
        actionGroup.addAction(self.actionToolBrews)
       
    
        #self.toolBar.addSeparator()
        self.actionToolInventoryFermentables=QAction(QIcon(self.icon_path+'cereal-wheat-svgrepo-com.svg'),'Mes fermentables',self)
        self.toolBar.addAction(self.actionToolInventoryFermentables)
        self.actionToolInventoryFermentables.setCheckable(1)
        actionGroup.addAction(self.actionToolInventoryFermentables)

        self.actionToolInventoryHops=QAction(QIcon(self.icon_path+'hops-svgrepo-com.svg'),'Mes houblons',self)
        self.toolBar.addAction(self.actionToolInventoryHops)
        self.actionToolInventoryHops.setCheckable(1)
        actionGroup.addAction(self.actionToolInventoryHops)

        self.actionToolInventoryYeasts=QAction(QIcon(self.icon_path+'petri-dish-svgrepo-com.svg'),'Mes levures',self)
        self.toolBar.addAction(self.actionToolInventoryYeasts)
        self.actionToolInventoryYeasts.setCheckable(1)
        actionGroup.addAction(self.actionToolInventoryYeasts)
        
        self.actionToolInventoryMisc=QAction(QIcon(self.icon_path+'ingredients-svgrepo-com.svg'),'Mes ingrédients divers',self)
        self.toolBar.addAction(self.actionToolInventoryMisc)
        self.actionToolInventoryMisc.setCheckable(1)
        actionGroup.addAction(self.actionToolInventoryMisc)

        
        #self.toolBar.addSeparator()
        self.actionToolEquipment=QAction(QIcon(self.icon_path+'brew-svgrepo-com.svg'),'Mes équipments',self)
        self.toolBar.addAction(self.actionToolEquipment)
        self.actionToolEquipment.setCheckable(1)
        actionGroup.addAction(self.actionToolEquipment)

        self.actionToolSourceWaters=QAction(QIcon(self.icon_path+'tap-faucet-svgrepo-com.svg'),'Mes eaux sources',self)
        self.toolBar.addAction(self.actionToolSourceWaters)
        self.actionToolSourceWaters.setCheckable(1)
        actionGroup.addAction(self.actionToolSourceWaters)

        self.actionToolTargetWaters=QAction(QIcon(self.icon_path+'target-svgrepo-com.svg'),'Mes eaux cibles',self)
        self.toolBar.addAction(self.actionToolTargetWaters)
        self.actionToolTargetWaters.setCheckable(1)
        actionGroup.addAction(self.actionToolTargetWaters)

        
        #self.toolBar.addSeparator() 


      
        self.icon_size=QSize(32,32)
        self.actionToolHelp=QAction(QIcon(self.icon_path+'help-question-question-mark-svgrepo-com.svg'),'Aide',self)
        self.toolBar.addAction(self.actionToolHelp)
        self.actionToolHelp.setCheckable(1)
        actionGroup.addAction(self.actionToolHelp)
        actionGroup.setExclusive(1)
        
        #a special menu for view
        
       
        toggleToolbarAction=self.toolBar.toggleViewAction()#return a checkable action to hide or show the tool bar
        self.menuView.addAction(toggleToolbarAction)
        toggleToolbarAction.setText('Barre d\'outils')
        self.toggleHeaderViewAction=QAction("Cacher/Afficher l'entête (Alt+E")
        self.menuView.addAction(self.toggleHeaderViewAction)
        self.toggleCalculationsViewAction=QAction("Cacher/Afficher les valeurs calculées (Alt+C)")
        self.menuView.addAction(self.toggleCalculationsViewAction)
        self.actionInventoryFermentables.triggered.connect(self.showInventoryFermentableEditor)
        self.actionToolInventoryFermentables.triggered.connect(self.showInventoryFermentableEditor)
        self.actionInventoryHops.triggered.connect(self.showInventoryHopEditor)
        self.actionToolInventoryHops.triggered.connect(self.showInventoryHopEditor)
        self.actionInventoryYeasts.triggered.connect(self.showInventoryYeastEditor)
        self.actionToolInventoryYeasts.triggered.connect(self.showInventoryYeastEditor)
        self.actionInventoryMiscs.triggered.connect(self.showInventoryMiscEditor)
        self.actionToolInventoryMisc.triggered.connect(self.showInventoryMiscEditor)
        self.actionAbout.triggered.connect(lambda: self.show_contextual_help("about"))
        self.actionEffacer_les_choix_initiaux.triggered.connect(self.erase_initial_choices)


        self.actionImport.triggered.connect(self.showImportDialog)
        self.actionRecopier.triggered.connect(self.showRecopyDialog)
    
        
        self.actionBrand.triggered.connect(self.showBrandDialog)
        self.actionSuppliers.triggered.connect(self.showSupplierDialog)
        self.actionCountries.triggered.connect(self.showCountryDialog)
        self.actionYBrand.triggered.connect(self.showYBrandDialog)

        self.actionEquipmentProfiles.triggered.connect(self.showEquipmentDialog)
        self.actionToolEquipment.triggered.connect(self.showEquipmentDialog)
        self.actionWaterProfiles.triggered.connect(self.showWaterDialog)
        self.actionToolSourceWaters.triggered.connect(self.showWaterDialog)
        self.actionWaterTargetProfiles.triggered.connect(self.showWaterTargetDialog)
        self.actionToolTargetWaters.triggered.connect(self.showWaterTargetDialog)


        self.actionMyRecipes.triggered.connect(self.showRecipeListDialog)
        self.actionToolRecipes.triggered.connect(self.showRecipeListDialog)

        self.actionMySessions.triggered.connect(self.showBrewListDialog)
        self
        self.actionToolBrews.triggered.connect(self.showBrewListDialog)

        self.actionStyles.triggered.connect(self.showStyleDialog)
        self.actionRests.triggered.connect(self.showRestDialog)
     

        self.actionToolHelp.triggered.connect(self.showHelp)
        self.actionFont.triggered.connect(self.showFontDialog)

        QtGui.QShortcut(QtGui.QKeySequence("Alt+E"), self, activated=  lambda todo="toggle_header": self.shortcut_triggered(todo))
        self.toggleHeaderViewAction.triggered.connect(lambda: self.shortcut_triggered('toggle_header'))
        QtGui.QShortcut(QtGui.QKeySequence("Alt+C"), self, activated=  lambda todo="toggle_calculations": self.shortcut_triggered(todo))
        self.toggleCalculationsViewAction.triggered.connect(lambda: self.shortcut_triggered('toggle_calculations'))
        log.info("mainwindow initialized")
    #---------------------------------------------------------------------------    
    def shortcut_triggered(self,todo)    :
        print('key is '+todo)
        self.keyboard_signal.emit(SignalObject('clavier',todo))
        
    def erase_initial_choices(self):
        msgBox=ConfirmationDialog()
        msgBox.setTitle("Confirmer l’effacement des choix initiaux")
        
        msgBox.setIcon(self.icon_path+'alert-48px-svgrepo-com.svg')
        message="""
 <p>Vous êtes sur le point d’effacer vos choix initiaux, c.-à-d. le choix du système de base de données, le nom de la base de données et éventuellement le mot de passe d’accès au serveur de 
base de données.</p>

<p>Si vous confirmez, ces choix seront effacés et l’application sera immédiatement fermée. Donc si nécessaire enregistrez vos modifications avant de le faire.</p>

<p>Sachez cependant, que l’effacement des choix initiaux n’entraîne pas l’effacement de la base de données sur laquelle vous travaillez actuellement.</p>
 <p>Vous pourrez toujours y revenir par la suite à condition
d’en avoir mémorisé le nom.</p>

<p style="font-weight:bold; color:red;">Attention : si vous êtes sur une plateforme Linux, vous devrez faire le prochain lancement de l'application dans un terminal, avec la commande suivante</p>
<p style="font-weight:bold; color:red;background-color: yellow;"> /opt/biere/biere </p>
<p>Confirmez-vous l’effacement ?</p>"""
        msgBox.setMessage(message) 
        msgBox.setCancelButtonText('Non. Ne pas effacer')
        msgBox.setConfirmButtonText('Oui. Effacer et terminer l’application')
        confirm=msgBox.exec()   
        if(confirm == 1):
            if sys.platform.startswith('linux'):
                path1=Path.home()
                path_to_cred=(path1/".biere"/"cred").resolve() #a string                 
            else:
                path_to_cred=Path('./cred/windows')

        path=path_to_cred/"db-choice.txt"
        path.unlink(missing_ok=True)    
        path=path_to_cred/"password.bin"
        path.unlink(missing_ok=True)
        path=path_to_cred/"dbname.bin"
        path.unlink(missing_ok=True)
        exit()
      
 


        
    def swapWidget(self,what,newWidget=None):
        #call from the recipe list or session list after an item has been selected
        match what:
            case 'recipe':
                if(newWidget):
                    index=self.stackedWidget.indexOf(self.recipeListWidget)
                    self.stackedWidget.removeWidget(self.recipeListWidget)
                    self.stackedWidget.insertWidget(index,newWidget)
                else:
                    index=self.stackedWidget.currentIndex()   
                    self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
                    self.stackedWidget.insertWidget(index,self.recipeListWidget)
                return index
            case 'brew':
                if(newWidget):
                    index=self.stackedWidget.indexOf(self.brewListWidget)
                    self.stackedWidget.removeWidget(self.brewListWidget)
                    self.stackedWidget.insertWidget(index,newWidget)
                else:
                    index=self.stackedWidget.currentIndex()   
                    self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
                    self.stackedWidget.insertWidget(index,self.brewListWidget)  
                return index

    def closeEvent(self,event):
        event.accept()


    def showFontDialog(self):
        self.fontDlg=FontDialogWidget()
        self.fontDlg.exec()
        
    def showHelp(self):
        self.helpW=HelpWidget()
        self.helpW.show()

    def showImportDialog(self):
        self.showImportDlg=ImportDialog()
        self.showImportDlg.exec()
    
    def showRecopyDialog(self):
        self.recopyDialog=MoveInitFilesDialog()
        self.recopyDialog.exec()
    #------------------------------------------------------------------
    def show_contextual_help(self,what):
        helpPopup=HelpMessage()
        filename=(self.this_file_path/"help/Head.html").resolve()
        prepend=open(filename,'r',encoding="utf-8").read()
       
        match what:
            case "about":
                helpPopup.set_title("À propos de ce logiciel")
                filename=(self.this_file_path/"help/About.html").resolve()


        text=open(filename,'r',encoding="utf-8").read()
        helpPopup.set_message(prepend+text)
        helpPopup.exec()
        

    def showInventoryFermentableEditor(self):
        #create a new object here to take into account any new brand
        self.stackedWidget.setCurrentIndex(2)
        


    def showInventoryHopEditor(self):
        #create a new object here to take into account any new brand
        self.stackedWidget.setCurrentIndex(3)
        return
        #self.hopSelector=HopSelector(self)
        #self.hopSelector.exec()    
        
    def showInventoryYeastEditor(self):
        #create a new object here to take into account any new brand
        self.stackedWidget.setCurrentIndex(4)
        return
        #self.yeastSelector=YeastSelector(self)
        #self.yeastSelector.exec()  

    def showInventoryMiscEditor(self):
        self.stackedWidget.setCurrentIndex(5)
           
    def showEquipmentDialog(self):
        self.stackedWidget.setCurrentIndex(6)
        #self.equipmentDlg=EquipmentDialog(self)
        #self.equipmentDlg.exec()     

    def showWaterDialog(self):
        self.stackedWidget.setCurrentIndex(7)
        #self.waterDlg=WaterDialog(self)
        #self.waterDlg.exec()

    #-----------------------------------------------
    #profiles

    def showWaterTargetDialog(self):
        self.stackedWidget.setCurrentIndex(8)
        #self.waterTargetDlg=WaterTargetDialog(self)
        #self.waterTargetDlg.exec()

    def showBrandDialog(self):
        self.brandDlg=BrandDialog(self)
        self.brandDlg.exec()     
    
    def showYBrandDialog(self):
        self.ybrandDlg=YBrandDialog(self)
        self.ybrandDlg.exec()    

    def showSupplierDialog(self):
        self.suppDlg=SupplierDialog(self)
        self.suppDlg.exec()
    
    def showCountryDialog(self):
        self.countryDlg=CountryDialog(self)
        self.countryDlg.exec()
            
   
        

    def showRestDialog(self):
        self.restDlg=RestDialog(self)
        self.restDlg.exec()    



    def showRecipeListDialog(self):
        self.stackedWidget.setCurrentIndex(0)
        #self.centralwidget.breakLayout()
        #self.recipeListWidget.setup_gui()
        #self.centralwidget.setLayout(self.recipeListWidget)
    
        
        

    def showBrewListDialog(self):
        self.stackedWidget.setCurrentIndex(1)
        #self.brewListWidget.setup_gui()
        #self.centralwidget.setLayout(self.brewListWidget)

    def showStyleDialog(self):
   

        self.styleDlg=StyleDialog(self)
        self.styleDlg.exec()    

