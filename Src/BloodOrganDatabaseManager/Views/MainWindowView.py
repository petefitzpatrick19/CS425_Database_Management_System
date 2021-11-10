

"""Module to contain the LoginView"""


from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5 import QtWidgets

from BloodOrganDatabaseManager.Views.UI.BloodOrganDatabaseManagerMainWindowGenerated import Ui_BloodOrganDatabaseManagerMainWindow


class MainWindowView(QtWidgets.QMainWindow, Ui_BloodOrganDatabaseManagerMainWindow, QObject):

   """This class provides the view which allows the user to interact with the database"""

   def __init__(self, parent=None):
      """
      Constructor
      """

      QObject.__init__(self)
      super(MainWindowView, self).__init__(parent)
      self.setupUi(self)
