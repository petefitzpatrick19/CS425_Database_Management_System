
import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QObject


# View imports
from BloodOrganDatabaseManager.Views.LoginView import LoginView
from BloodOrganDatabaseManager.Views.MainWindowView import MainWindowView

# Common Imports
from BloodOrganDatabaseManager.Common.CommonDefinitions import CREDENTIALS_MAP_USER_KEY, CREDENTIALS_MAP_PASS_KEY, DB_HOST, DB_NAME, DB_PORT


class ManagerSingleton(QObject):


   def __init__(self):

      QObject.__init__(self)

      self.__conn = None

      # --Views----------------------------------------------------------

      self.__login_view = LoginView()

      # -----------------------------------------------------------------

      # --Signals and Slots----------------------------------------------

      self.__login_view.login_signal.connect(self.start)

      # -----------------------------------------------------------------

      self.__login_view.show()


   @pyqtSlot( dict )
   def start(self, credentials_map):
      
      username = credentials_map[CREDENTIALS_MAP_USER_KEY]
      password = credentials_map[CREDENTIALS_MAP_PASS_KEY]

      try:
         self.__conn = psycopg2.connect(database = DB_NAME, user = username, 
                                 password = password, host = DB_HOST, port = DB_PORT)

         print("Database conencted successfully.")


      except Exception as e:
         print("Database not connected.")
         print(e)
         return False

      self.__login_view.close()

      self.__main_window_view = MainWindowView(self.__conn)
      self.__main_window_view.show()

      return True