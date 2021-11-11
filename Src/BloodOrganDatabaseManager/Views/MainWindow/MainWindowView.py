

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

      self.add_doctor_push_btn.clicked.connect(self.add_doctor)
      self.remove_doctor_push_btn.clicked.connect(self.remove_doctor)

      self.add_patient_push_btn.clicked.connect(self.add_patient)
      self.remove_patient_push_btn.clicked.connect(self.remove_patient)

      # -----------------------------------------------------------------

      self.update_hospital_table()
      self.update_doctor_table()
      self.update_patient_table()


   # --Hospital----------------------------------------------------------

   def add_hospital(self):
      """
      This method is a slot which takes the user inputs and adds a Hospital entry to the table
      """

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
      """
      This method is a slot which which removes the selected Hospital entry from the table
      """

      row = self.hospital_table.currentRow()
      if not row:
         return False

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
      """
      This method updates the Hospital table to match the current status of the database
      """
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

   # --Doctor-------------------------------------------------------------

   def add_doctor(self):
      """
      This method is a slot which takes the user inputs and adds a Doctor entry to the table
      """

      doctor_id = self.doctor_id_line_edit.text()
      name = self.doctor_name_line_edit.text()
      age = self.doctor_age_spin_box.text()
      specialization = self.doctor_specialization_line_edit.text()
      fee = self.doctor_fee_spin_box.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Doctor (doctor_id, name, age, specialization, fee) VALUES ({doctor_id}, '{name}', {age}, '{specialization}', {fee})"

         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_doctor_table()
      return True


   def remove_doctor(self):
      """
      This method is a slot which which removes the selected Doctor entry from the table
      """

      row = self.doctor_table.currentRow()
      if not row:
         return False

      doctor_id = self.doctor_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Doctor WHERE doctor_id = {doctor_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_doctor_table()
      return True


   def update_doctor_table(self):
      """
      This method updates the Doctor table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Doctor"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.doctor_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.doctor_table.insertRow(idx)
            self.doctor_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.doctor_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.doctor_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.doctor_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.doctor_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))

      except Exception as e:
         print(e)
         return False

      return True

   # --Patient-------------------------------------------------------------

   def add_patient(self):
      """
      This method is a slot which takes the user inputs and adds a Patient entry to the table
      """

      patient_id = self.patient_id_spin_box.text()
      name = self.patient_name_line_edit.text()
      age = self.patient_age_spin_box.text()
      blood_type = self.patient_blood_type_line_edit.text()
      need = self.patient_need_line_edit.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Patient (patient_id, name, age, blood_type, need) VALUES ({patient_id}, '{name}', {age}, '{blood_type}', '{need}')"

         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_patient_table()
      return True


   def remove_patient(self):
      """
      This method is a slot which which removes the selected Patient entry from the table
      """

      row = self.patient_table.currentRow()
      if not row:
         return False

      patient_id = self.patient_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Patient WHERE patient_id = {patient_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
         return False

      self.update_patient_table()
      return True


   def update_patient_table(self):
      """
      This method updates the Patient table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Patient"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.patient_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.patient_table.insertRow(idx)
            self.patient_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.patient_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.patient_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.patient_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.patient_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))

      except Exception as e:
         print(e)
         return False

      return True
