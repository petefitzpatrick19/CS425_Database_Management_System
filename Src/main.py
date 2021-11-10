
import sys  
from PyQt5 import QtWidgets
from BloodOrganDatabaseManager.ManagerSingleton import ManagerSingleton

def main():
   app = QtWidgets.QApplication(sys.argv)

   manager_singleton = ManagerSingleton()
   
   sys.exit( app.exec_() )

if __name__ == '__main__':
    main()
