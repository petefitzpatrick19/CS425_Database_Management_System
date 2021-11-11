

"""Module to contain the LoginView"""


from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5 import QtWidgets

from BloodOrganDatabaseManager.Views.UI.BloodOrganDatabaseManagerMainWindowGenerated import Ui_BloodOrganDatabaseManagerMainWindow


class MainWindowView(QtWidgets.QMainWindow, Ui_BloodOrganDatabaseManagerMainWindow, QObject):

   """This class provides the view which allows the user to interact with the database"""

   def __init__(self, conn, parent=None):
      """
      Constructor
      """

      QObject.__init__(self)
      super(MainWindowView, self).__init__(parent)
      self.setupUi(self)

      self.__conn = conn

      # --Signals and Slots----------------------------------------------

      self.add_hospital_push_btn.clicked.connect(self.add_hospital)
      self.remove_hospital_push_btn.clicked.connect(self.remove_hospital)

      # -----------------------------------------------------------------

      self.update_hospital_table()

   
   def add_hospital(self):

      hospital_id = self.hospital_id_spin_box.text()
      name = self.hospital_name_line_edit.text()
      field = self.hospital_field_line_edit.text()
      cost = self.hospital_cost_spin_box.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Hospital (hospital_id, name, field, cost) VALUES ({hospital_id}, '{name}', '{field}', {cost})"

         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_hospital_table()
      return True


   def remove_hospital(self):

      row = self.hospital_table.currentRow()
      hospital_id = self.hospital_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Hospital WHERE hospital_id = {hospital_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_hospital_table()
      return True


   def update_hospital_table(self):
      
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Hospital"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.hospital_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.hospital_table.insertRow(idx)
            self.hospital_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.hospital_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.hospital_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.hospital_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))

      except Exception as e:
         print(e)
         return False

      return True
