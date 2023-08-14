
'''
copyright José FOURNIER 2023

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtGui import QPalette,QColor,QFont
from MainWindow import MainWindow
from database.commons.settings import Setting,all_setting, update_setting, add_setting, find_setting_by_id

import os

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
print(app.style().objectName())
print(sys.platform)
screen_resolution = QtGui.QGuiApplication.primaryScreen().availableGeometry()

#window.resize(w,h)
new_font = QFont()
new_font.setFamily('Carlito Sans') 
#if sys.platform.startswith('linux'):
#    new_font.setPointSize(9)
#    new_font.setFamily('Carlito Sans')
#else:
#    new_font.setPointSize( 9 )#your option
settings=all_setting()
for item in settings:
    if item.name=='Font Size':
        new_font.setPointSize(int(item.val))
    else:    
        new_font.setPointSize(11)

app.setFont( new_font ) 
window = MainWindow()
window.resize(1280,720)
window.show()
app.exec()
