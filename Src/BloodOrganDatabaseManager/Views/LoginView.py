

"""Module to contain the LoginView"""


from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5 import QtWidgets

from BloodOrganDatabaseManager.Views.UI.BloodOrganDatabaseManagerLoginGenerated import Ui_BloodOrganDatabaseManagerLogin

CREDENTIALS_MAP_USER_KEY = "user"
CREDENTIALS_MAP_PASS_KEY = "pass"


class LoginView(QtWidgets.QMainWindow, Ui_BloodOrganDatabaseManagerLogin, QObject):

   """This class provides the view which allows the user to enter their credentials for logging into the database"""

   login_signal = pyqtSignal( dict )

   def __init__(self, parent=None):
      """
      Constructor
      """

      QObject.__init__(self)
      super(LoginView, self).__init__(parent)
      self.setupUi(self)

      self.enter_btn.clicked.connect(self.on_submit_login)


   @pyqtSlot()
   def on_submit_login(self):
      """
      This method is a slot which checks that the fields were filled in correctly and signals upon success
      """ 

      username = self.user_line_edit.text()
      password = self.pass_line_edit.text()

      print(f"{username}: {password}")

      if username and password:

         credentials_map = {CREDENTIALS_MAP_USER_KEY: username, CREDENTIALS_MAP_PASS_KEY: password}
         self.login_signal.emit(credentials_map)

      else:
         print("Please enter a valid username and password.")

