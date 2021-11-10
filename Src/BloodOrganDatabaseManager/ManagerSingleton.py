
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QObject


# View imports
from BloodOrganDatabaseManager.Views.LoginView import LoginView
from BloodOrganDatabaseManager.Views.MainWindowView import MainWindowView


class ManagerSingleton(QObject):


   def __init__(self):

      QObject.__init__(self)

      # --Views----------------------------------------------------------

      self.__login_view = LoginView()
      self.__main_window_view = MainWindowView()

      # -----------------------------------------------------------------

      self.__login_view.login_signal.connect(self.start)

      self.__login_view.show()


   @pyqtSlot( dict )
   def start(self, credentials_map):

      self.__login_view.close()

      self.__main_window_view.show()

      return True