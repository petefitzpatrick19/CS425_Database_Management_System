

"""Module to contain the LoginView"""


import datetime
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

      self.add_organ_donor_push_btn.clicked.connect(self.add_organ_donor)
      self.remove_organ_donor_push_btn.clicked.connect(self.remove_organ_donor)

      self.add_blood_donor_push_btn.clicked.connect(self.add_blood_donor)
      self.remove_blood_donor_push_btn.clicked.connect(self.remove_blood_donor)

      self.add_organ_push_btn.clicked.connect(self.add_organ)
      self.remove_organ_push_btn.clicked.connect(self.remove_organ)

      self.add_blood_bag_push_btn.clicked.connect(self.add_blood_bag)
      self.remove_blood_bag_push_btn.clicked.connect(self.remove_blood_bag)

      self.add_transplant_push_btn.clicked.connect(self.add_transplant)
      self.remove_transplant_push_btn.clicked.connect(self.remove_transplant)

      self.add_transfusion_push_btn.clicked.connect(self.add_transfusion)
      self.remove_transfusion_push_btn.clicked.connect(self.remove_transfusion)

      self.organ_enter_btn.clicked.connect(self.enter_organ_donor_list_options)

      self.blood_enter_btn.clicked.connect(self.enter_blood_donor_list_options)

      self.donor_match_enter_btn.clicked.connect(self.enter_donor_match_list_options)

      self.update_income_report_push_btn.clicked.connect(self.on_income_report_push_btn_clicked)

      self.update_operations_report_push_btn.clicked.connect(self.on_operations_report_push_btn_clicked)

      # -----------------------------------------------------------------

      self.update_hospital_table()
      self.update_doctor_table()
      self.update_patient_table()
      self.update_organ_donor_table()
      self.update_blood_donor_table()
      self.update_organ_table()
      self.update_blood_bag_table()
      self.update_transplant_table()
      self.update_transfusion_table()

      self.update_organ_donor_list_view()
      self.update_blood_donor_list_view()
      self.update_donor_match_list_view()
      self.update_income_report_view()
      self.update_operations_report_view()


   def report_error(self, title, msg):
      """
      This method creates a popup box displaying the title and message passed in.
      """
      box = QtWidgets.QMessageBox()
      box.setWindowTitle(title)
      box.setText(msg)
      box.exec_()


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
         self.report_error("Add Hospital Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_hospital_table()
      return True


   def remove_hospital(self):
      """
      This method is a slot which which removes the selected Hospital entry from the table
      """

      row = self.hospital_table.currentRow()
      if row is -1:
         return False

      hospital_id = self.hospital_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Hospital WHERE hospital_id = {hospital_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Hospital Failure", str(e))
         self.__conn.rollback()
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

         self.hospital_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Hospital Failure", str(e))
         self.__conn.rollback()
         return False

      return True

   # --Doctor-------------------------------------------------------------

   def add_doctor(self):
      """
      This method is a slot which takes the user inputs and adds a Doctor entry to the table
      """

      doctor_id = self.doctor_id_spin_box.text()
      name = self.doctor_name_line_edit.text()
      age = self.doctor_age_spin_box.text()
      specialization = self.doctor_specialization_line_edit.text()
      fee = self.doctor_fee_spin_box.text()
      region = self.doctor_region_line_edit.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Doctor (doctor_id, name, age, specialization, fee, region) VALUES ({doctor_id}, '{name}', {age}, '{specialization}', {fee}, '{region}')"

         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Doctor Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_doctor_table()
      return True


   def remove_doctor(self):
      """
      This method is a slot which which removes the selected Doctor entry from the table
      """

      row = self.doctor_table.currentRow()
      if row is -1:
         return False

      doctor_id = self.doctor_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Doctor WHERE doctor_id = {doctor_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Doctor Failure", str(e))
         self.__conn.rollback()
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
            self.doctor_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))

         self.doctor_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Doctor Failure", str(e))
         self.__conn.rollback()
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
      region = self.patient_region_line_edit.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Patient (patient_id, name, age, blood_type, need, region) VALUES ({patient_id}, '{name}', {age}, '{blood_type}', '{need}', '{region}')"

         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Patient Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_patient_table()
      return True


   def remove_patient(self):
      """
      This method is a slot which which removes the selected Patient entry from the table
      """

      row = self.patient_table.currentRow()
      if row is -1:
         return False

      patient_id = self.patient_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Patient WHERE patient_id = {patient_id}"

         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Patient Failure", str(e))
         self.__conn.rollback()
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
            self.patient_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))

         self.patient_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Patient Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   # --Organ Donor----------------------------------------------------------

   def add_organ_donor(self):
      """
      This method is a slot which takes the user inputs and adds a Organ Donor entry to the table
      """
      organ_donor_id = self.organ_donor_id_spin_box.text()
      name = self.organ_donor_name_line_edit.text()
      age = self.organ_donor_age_spin_box.text()
      blood_type = self.organ_donor_blood_type_line_edit.text()
      drug_use = 1 if self.organ_donor_drug_use_check_box.isChecked() else 0
      last_tattoo_date = self.organ_donor_last_tattoo_date_line_edit.text()
      region = self.organ_donor_region_line_edit.text()
      organ_name = self.organ_donor_organ_name_line_edit.text()

      med_history_list = self.organ_donor_med_history_line_edit.text().split(",")
      chronic_diseases_list = self.organ_donor_chronic_diseases_line_edit.text().split(",")
      contact_info_list = self.organ_donor_contact_info_line_edit.text().split(",")

      # Case for last_tattoo_date where the user does not enter anything
      if not last_tattoo_date:
         last_tattoo_date = 'null'
      else:
         last_tattoo_date = f"'{last_tattoo_date}'"

      try:

         cursor = self.__conn.cursor()

         insert_command1 = f"INSERT INTO Organ_Donor (organ_donor_id, name, age, blood_type, drug_use, last_tattoo_date, region, organ_name) VALUES ({organ_donor_id}, '{name}', {age}, '{blood_type}', B'{drug_use}', {last_tattoo_date}, '{region}', '{organ_name}')"
         cursor.execute(insert_command1)

         for medication in med_history_list:
            insert_command2 = f"INSERT INTO OD_Med_Hist (organ_donor_id, med_history) VALUES ({organ_donor_id}, '{medication}')"
            cursor.execute(insert_command2)

         for disease in chronic_diseases_list:
            insert_command3 = f"INSERT INTO OD_Chronic_Disease (organ_donor_id, chronic_disease) VALUES ({organ_donor_id}, '{disease}')"
            cursor.execute(insert_command3)

         for contact in contact_info_list:
            insert_command4 = f"INSERT INTO OD_Contact (organ_donor_id, contact) VALUES ({organ_donor_id}, '{contact}')"
            cursor.execute(insert_command4)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Organ Donor Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_organ_donor_table()
      return True


   def remove_organ_donor(self):
      """
      This method is a slot which which removes the selected Organ Donor entry from the table
      """

      row = self.organ_donor_table.currentRow()
      if row is -1:
         return False

      organ_donor_id = self.organ_donor_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command1 = f"DELETE FROM Organ_Donor WHERE organ_donor_id = {organ_donor_id}"
         cursor.execute(delete_command1)

         delete_command2 = f"DELETE FROM OD_Med_Hist WHERE organ_donor_id = {organ_donor_id}"
         cursor.execute(delete_command2)

         delete_command3 = f"DELETE FROM OD_Chronic_Disease WHERE organ_donor_id = {organ_donor_id}"
         cursor.execute(delete_command3)

         delete_command4 = f"DELETE FROM OD_Contact WHERE organ_donor_id = {organ_donor_id}"
         cursor.execute(delete_command4)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Organ Donor Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_organ_donor_table()
      return True


   def update_organ_donor_table(self):
      """
      This method updates the Organ Donor table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command1 = "SELECT * FROM Organ_Donor"

         cursor.execute(select_command1)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.organ_donor_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.organ_donor_table.insertRow(idx)
            self.organ_donor_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.organ_donor_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.organ_donor_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.organ_donor_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.organ_donor_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.organ_donor_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.organ_donor_table.setItem(idx,6,QtWidgets.QTableWidgetItem(str(data[6])))
            self.organ_donor_table.setItem(idx,7,QtWidgets.QTableWidgetItem(str(data[7])))

            select_command2 = f"SELECT med_history FROM OD_Med_Hist WHERE organ_donor_id = {data[0]}"
            cursor.execute(select_command2)
            self.__conn.commit()
            med_history_list = []
            for med in cursor.fetchall():
               med_history_list.append(med[0])
            med_history_list = ", ".join(med_history_list)
            self.organ_donor_table.setItem(idx,8,QtWidgets.QTableWidgetItem(med_history_list))

            select_command3 = f"SELECT chronic_disease FROM OD_Chronic_Disease WHERE organ_donor_id = {data[0]}"
            cursor.execute(select_command3)
            self.__conn.commit()
            chronic_disease_list = []
            for disease in cursor.fetchall():
               chronic_disease_list.append(disease[0])
            chronic_disease_list = ", ".join(chronic_disease_list)
            self.organ_donor_table.setItem(idx,9,QtWidgets.QTableWidgetItem(chronic_disease_list))

            select_command4 = f"SELECT contact FROM OD_Contact WHERE organ_donor_id = {data[0]}"
            cursor.execute(select_command4)
            self.__conn.commit()
            contact_info_list = []
            for contact in cursor.fetchall():
               contact_info_list.append(contact[0])
            contact_info_list = ", ".join(contact_info_list)
            self.organ_donor_table.setItem(idx,10,QtWidgets.QTableWidgetItem(contact_info_list))

         self.organ_donor_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Organ Donor Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   # --Blood Donor----------------------------------------------------------

   def add_blood_donor(self):
      """
      This method is a slot which takes the user inputs and adds a Blood Donor entry to the table
      """
      blood_donor_id = self.blood_donor_id_spin_box.text()
      name = self.blood_donor_name_line_edit.text()
      age = self.blood_donor_age_spin_box.text()
      blood_type = self.blood_donor_blood_type_line_edit.text()
      drug_use = 1 if self.blood_donor_drug_use_check_box.isChecked() else 0
      last_tattoo_date = self.blood_donor_last_tattoo_date_line_edit.text()
      region = self.blood_donor_region_line_edit.text()
      last_donation = self.blood_donor_last_donation_line_edit.text()

      med_history_list = self.blood_donor_med_history_line_edit.text().split(",")
      chronic_diseases_list = self.blood_donor_chronic_diseases_line_edit.text().split(",")
      contact_info_list = self.blood_donor_contact_info_line_edit.text().split(",")

      # Case for last_tattoo_date where the user does not enter anything
      if not last_tattoo_date:
         last_tattoo_date = 'null'
      else:
         last_tattoo_date = f"'{last_tattoo_date}'"

      # Case for last_donation where the user does not enter anything
      if not last_donation:
         last_donation = 'null'
      else:
         last_donation = f"'{last_donation}'"

      try:

         cursor = self.__conn.cursor()

         insert_command1 = f"INSERT INTO Blood_Donor (blood_donor_id, name, age, blood_type, drug_use, last_tattoo_date, region, last_donation) VALUES ({blood_donor_id}, '{name}', {age}, '{blood_type}', B'{drug_use}', {last_tattoo_date}, '{region}', {last_donation})"
         cursor.execute(insert_command1)

         for medication in med_history_list:
            insert_command2 = f"INSERT INTO BD_Med_Hist (blood_donor_id, med_history) VALUES ({blood_donor_id}, '{medication}')"
            cursor.execute(insert_command2)

         for disease in chronic_diseases_list:
            insert_command3 = f"INSERT INTO BD_Chronic_Disease (blood_donor_id, chronic_disease) VALUES ({blood_donor_id}, '{disease}')"
            cursor.execute(insert_command3)

         for contact in contact_info_list:
            insert_command4 = f"INSERT INTO BD_Contact (blood_donor_id, contact) VALUES ({blood_donor_id}, '{contact}')"
            cursor.execute(insert_command4)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Blood Donor Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_blood_donor_table()
      return True


   def remove_blood_donor(self):
      """
      This method is a slot which which removes the selected Blood Donor entry from the table
      """

      row = self.blood_donor_table.currentRow()
      if row is -1:
         return False

      blood_donor_id = self.blood_donor_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command1 = f"DELETE FROM Blood_Donor WHERE blood_donor_id = {blood_donor_id}"
         cursor.execute(delete_command1)

         delete_command2 = f"DELETE FROM BD_Med_Hist WHERE blood_donor_id = {blood_donor_id}"
         cursor.execute(delete_command2)

         delete_command3 = f"DELETE FROM BD_Chronic_Disease WHERE blood_donor_id = {blood_donor_id}"
         cursor.execute(delete_command3)

         delete_command4 = f"DELETE FROM BD_Contact WHERE blood_donor_id = {blood_donor_id}"
         cursor.execute(delete_command4)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Blood Donor Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_blood_donor_table()
      return True


   def update_blood_donor_table(self):
      """
      This method updates the Blood Donor table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Blood_Donor"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.blood_donor_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.blood_donor_table.insertRow(idx)
            self.blood_donor_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.blood_donor_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.blood_donor_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.blood_donor_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.blood_donor_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.blood_donor_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.blood_donor_table.setItem(idx,6,QtWidgets.QTableWidgetItem(str(data[6])))
            self.blood_donor_table.setItem(idx,7,QtWidgets.QTableWidgetItem(str(data[7])))

            select_command2 = f"SELECT med_history FROM BD_Med_Hist WHERE blood_donor_id = {data[0]}"
            cursor.execute(select_command2)
            self.__conn.commit()
            med_history_list = []
            for med in cursor.fetchall():
               med_history_list.append(med[0])
            med_history_list = ", ".join(med_history_list)
            self.blood_donor_table.setItem(idx,8,QtWidgets.QTableWidgetItem(med_history_list))

            select_command3 = f"SELECT chronic_disease FROM BD_Chronic_Disease WHERE blood_donor_id = {data[0]}"
            cursor.execute(select_command3)
            self.__conn.commit()
            chronic_disease_list = []
            for disease in cursor.fetchall():
               chronic_disease_list.append(disease[0])
            chronic_disease_list = ", ".join(chronic_disease_list)
            self.blood_donor_table.setItem(idx,9,QtWidgets.QTableWidgetItem(chronic_disease_list))

            select_command4 = f"SELECT contact FROM BD_Contact WHERE blood_donor_id = {data[0]}"
            cursor.execute(select_command4)
            self.__conn.commit()
            contact_info_list = []
            for contact in cursor.fetchall():
               contact_info_list.append(contact[0])
            contact_info_list = ", ".join(contact_info_list)
            self.blood_donor_table.setItem(idx,10,QtWidgets.QTableWidgetItem(contact_info_list))

         self.blood_donor_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Blood Donor Failure", str(e))
         self.__conn.rollback()
         return False

      return True

   # --Blood Bag----------------------------------------------------------

   def add_blood_bag(self):
      """
      This method is a slot which takes the user inputs and adds a Blood Bag entry to the table
      """
      blood_bag_id = self.blood_bag_donor_id_spin_box.text()
      rh = self.blood_bag_rh_line_edit.text()
      used = 1 if self.blood_bag_used_check_box.isChecked() else 0
      blood_donor_id = self.blood_bag_donor_id_spin_box.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Blood_Bag (bag_id, rh, used, blood_donor_id) VALUES ({blood_bag_id}, '{rh}', B'{used}', {blood_donor_id})"
         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Blood Bag Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_blood_bag_table()
      return True


   def remove_blood_bag(self):
      """
      This method is a slot which which removes the selected Blood Bag entry from the table
      """
      row = self.blood_bag_table.currentRow()
      if row is -1:
         return False

      blood_bag_id = self.blood_bag_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Blood_Bag WHERE blood_bag_id = {blood_bag_id}"
         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Blood Bag Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_blood_bag_table()
      return True


   def update_blood_bag_table(self):
      """
      This method updates the Blood Bag table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Blood_Bag"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.blood_bag_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.blood_bag_table.insertRow(idx)
            self.blood_bag_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.blood_bag_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.blood_bag_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.blood_bag_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))

         self.blood_bag_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Blood Bag Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   # --Organ-------------------------------------------------------------

   def add_organ(self):
      """
      This method is a slot which takes the user inputs and adds an Organ entry to the table
      """
      organ_id = self.organ_id_spin_box.text()
      name = self.organ_name_line_edit.text()
      life = self.organ_life_spin_box.text()
      availability_date = self.organ_availability_date_line_edit.text()
      used = 1 if self.organ_used_check_box.isChecked() else 0
      organ_donor_id = self.organ_organ_donor_id_spin_box.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Organ (organ_id, name, life, availability_date, used, organ_donor_id) VALUES ({organ_id}, '{name}', {life}, '{availability_date}', B'{used}', {organ_donor_id})"
         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Organ Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_organ_table()
      return True


   def remove_organ(self):
      """
      This method is a slot which which removes the selected Organ entry from the table
      """
      row = self.organ_table.currentRow()
      if row is -1:
         return False

      organ_id = self.organ_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Organ WHERE organ_id = {organ_id}"
         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Organ Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_organ_table()
      return True


   def update_organ_table(self):
      """
      This method updates the Organ table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Organ"

         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.organ_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.organ_table.insertRow(idx)
            self.organ_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.organ_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.organ_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.organ_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.organ_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.organ_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5]))) # TODO: Add organ_donor_id to UI File in Table

         self.organ_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Organ Failure", str(e))
         self.__conn.rollback()
         return False

      return True
   
   # --Transplant--------------------------------------------------------

   def add_transplant(self):
      """
      This method is a slot which takes the user inputs and adds a Transplant entry to the table
      """
      transplant_id = self.transplant_id_spin_box.text()
      organ = self.transplant_organ_line_edit.text()
      status = self.transplant_status_line_edit.text()
      organ_donor_id = self.transplant_organ_donor_id_spin_box.text()
      patient_id = self.transplant_patient_id_spin_box.text()
      hospital_id = self.transplant_hospital_id_spin_box.text()

      doctor_ids = self.transplant_doctor_ids_line_edit.text().split(",")

      try:

         cursor = self.__conn.cursor()

         insert_command1 = f"INSERT INTO Transplant (tp_id, organ, status, organ_donor_id, patient_id, hospital_id) VALUES ({transplant_id}, '{organ}', '{status}', {organ_donor_id}, {patient_id}, {hospital_id})"
         cursor.execute(insert_command1)

         for doctor in doctor_ids:
            insert_command2 = f"INSERT INTO TP_Operates (tp_id, doctor_id) VALUES ({transplant_id}, {int(doctor)})"
            cursor.execute(insert_command2)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Transplant Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_transplant_table()
      return True


   def remove_transplant(self):
      """
      This method is a slot which which removes the selected Transplant entry from the table
      """
      row = self.transplant_table.currentRow()
      if row is -1:
         return False

      transplant_id = self.transplant_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command1 = f"DELETE FROM Transplant WHERE tp_id = {transplant_id}"
         cursor.execute(delete_command1)

         delete_command2 = f"DELETE FROM TP_Operates WHERE tp_id = {transplant_id}"
         cursor.execute(delete_command2)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Transplant Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_transplant_table()
      return True


   def update_transplant_table(self):
      """
      This method updates the Transfusion table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command1 = "SELECT * FROM Transplant"
         cursor.execute(select_command1)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.transplant_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.transplant_table.insertRow(idx)
            self.transplant_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.transplant_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.transplant_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.transplant_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.transplant_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.transplant_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))

            select_command2 = f"SELECT doctor_id FROM TP_Operates WHERE tp_id = {data[0]}"
            cursor.execute(select_command2)
            self.__conn.commit()
            doctor_ids = []
            for doctor in cursor.fetchall():
               doctor_ids.append(str(doctor[0]))
            doctor_ids = ", ".join(doctor_ids)
            self.transplant_table.setItem(idx,6,QtWidgets.QTableWidgetItem(doctor_ids))

         self.transplant_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Transplant Failure", str(e))
         self.__conn.rollback()
         return False

      return True
      

   # --Transfusion-------------------------------------------------------

   def add_transfusion(self):
      """
      This method is a slot which takes the user inputs and adds a Transfusion entry to the table
      """
      transfusion_id = self.transfusion_id_spin_box.text()
      status = self.transfusion_status_line_edit.text()
      blood_donor_id = self.transfusion_blood_donor_id_spin_box.text()
      doctor_id = self.transfusion_doctor_id_spin_box.text()
      patient_id = self.transfusion_patient_id_spin_box.text()
      hospital_id = self.transfusion_hospital_id_spin_box.text()

      try:

         cursor = self.__conn.cursor()

         insert_command = f"INSERT INTO Transfusion (tf_id, status, blood_donor_id, doctor_id, patient_id, hospital_id) VALUES ({transfusion_id}, '{status}', {blood_donor_id}, {doctor_id}, {patient_id}, {hospital_id})"
         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Add Transfusion Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_transfusion_table()
      return True


   def remove_transfusion(self):
      """
      This method is a slot which which removes the selected Transfusion entry from the table
      """
      row = self.transfusion_table.currentRow()
      if row is -1:
         return False

      transfusion_id = self.transfusion_table.item(row,0).text()

      try:

         cursor = self.__conn.cursor()

         delete_command = f"DELETE FROM Transfusion WHERE tf_id = {transfusion_id}"
         cursor.execute(delete_command)

         self.__conn.commit()

      except Exception as e:
         self.report_error("Remove Transfusion Failure", str(e))
         self.__conn.rollback()
         return False

      self.update_transfusion_table()
      return True


   def update_transfusion_table(self):
      """
      This method updates the Transfusion table to match the current status of the database
      """
      try:

         cursor = self.__conn.cursor()

         select_command = "SELECT * FROM Transfusion"
         cursor.execute(select_command)

         self.__conn.commit()

         rows = cursor.fetchall()
         self.transfusion_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.transfusion_table.insertRow(idx)
            self.transfusion_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.transfusion_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.transfusion_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.transfusion_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.transfusion_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.transfusion_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.transfusion_table.setItem(idx,6,QtWidgets.QTableWidgetItem(str(data[5])))

         self.transfusion_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Transfusion Failure", str(e))
         self.__conn.rollback()
         return False

      return True

   # --Organ Donor List View---------------------------------------------

   def get_available_organ_donor_regions(self):
      """
      This method returns a list of the available regions from the Organ Donor table
      """
      available_regions_list = []

      try:

         cursor = self.__conn.cursor()

         select_regions_command = """SELECT DISTINCT region FROM Organ_Donor"""
         cursor.execute(select_regions_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         for region in rows:
            available_regions_list.append(region[0])

      except Exception as e:
         self.report_error("Get Available Organ Donor Regions Failure", str(e))
         self.__conn.rollback()

      return available_regions_list


   def get_available_organ_donor_organs(self):
      """
      This method returns a list of the available organs from the Organ Donor table
      """
      available_organs_list = []

      try:

         cursor = self.__conn.cursor()

         select_regions_command = """SELECT DISTINCT organ_name FROM Organ_Donor"""
         cursor.execute(select_regions_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         for organ in rows:
            available_organs_list.append(organ[0])

      except Exception as e:
         self.report_error("Get Available Organs Failure", str(e))
         self.__conn.rollback()

      return available_organs_list


   def update_organ_donor_list_view(self):
      """
      This method updates the selection options for the for the Organ Donor List View
      """
      available_regions_list = self.get_available_organ_donor_regions()
      available_organs_list = self.get_available_organ_donor_organs()

      self.organ_region_combo_box.clear()
      for region in available_regions_list:
         self.organ_region_combo_box.addItem(region)

      self.organ_type_combo_box.clear()
      for organ in available_organs_list:
         self.organ_type_combo_box.addItem(organ)


   def enter_organ_donor_list_options(self):
      """
      This method updates the Organ Donor List and Recommended Doctors tables based on the currently
      selected options.
      """

      region = self.organ_region_combo_box.currentText()
      organ = self.organ_type_combo_box.currentText()

      try:
         cursor = self.__conn.cursor()

         select_donors_command = f"SELECT organ_donor_id, name FROM Organ_Donor where region = '{region}' AND organ_name = '{organ}'"
         cursor.execute(select_donors_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.organ_donors_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.organ_donors_table.insertRow(idx)
            self.organ_donors_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.organ_donors_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))

         self.organ_donors_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

         select_doctors_command = f"SELECT doctor_id, name FROM Doctor where specialization = '{organ}'"
         cursor.execute(select_doctors_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.recommended_doctors_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.recommended_doctors_table.insertRow(idx)
            self.recommended_doctors_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.recommended_doctors_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))

         self.recommended_doctors_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Get Organ Donors Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   # --Blood Donor List View---------------------------------------------

   def get_available_blood_donor_regions(self):
      """
      This method returns a list of the available regions from the Organ Donor table
      """
      available_regions_list = []

      try:

         cursor = self.__conn.cursor()

         select_regions_command = """SELECT DISTINCT region FROM Blood_Donor"""
         cursor.execute(select_regions_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         for region in rows:
            available_regions_list.append(region[0])

      except Exception as e:
         self.report_error("Get Available Blood Donor Regions Failure", str(e))
         self.__conn.rollback()

      return available_regions_list


   def get_available_blood_donor_blood_types(self):
      """
      This method returns a list of the available blood types from the Blood Donor table
      """
      available_blood_types_list = []

      try:

         cursor = self.__conn.cursor()

         select_regions_command = """SELECT DISTINCT blood_type FROM Blood_Donor"""
         cursor.execute(select_regions_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         for organ in rows:
            available_blood_types_list.append(organ[0])

      except Exception as e:
         self.report_error("Get Available Blood Types Failure", str(e))
         self.__conn.rollback()

      return available_blood_types_list


   def get_available_blood_donor_age_groups(self):
      """
      This method returns a list of the available Age Groups from the Blood Donor table
      """
      available_age_groups_list = []

      try:

         cursor = self.__conn.cursor()

         select_regions_command = """SELECT DISTINCT age FROM Blood_Donor"""
         cursor.execute(select_regions_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         for age in rows:
            available_age_groups_list.append(str(age[0]))

      except Exception as e:
         self.report_error("Get Available Blood Donor Age Groups Failure", str(e))
         self.__conn.rollback()

      return available_age_groups_list


   def update_blood_donor_list_view(self):
      """
      This method updates the selection options for the for the Blood Donor List View
      """
      available_regions_list = self.get_available_blood_donor_regions()
      available_blood_types_list = self.get_available_blood_donor_blood_types()
      available_availabilities_list = ['Available', 'Not Available']
      available_age_groups_list = self.get_available_blood_donor_age_groups()

      self.blood_region_combo_box.clear()
      for region in available_regions_list:
         self.blood_region_combo_box.addItem(region)

      self.blood_type_combo_box.clear()
      for blood_type in available_blood_types_list:
         self.blood_type_combo_box.addItem(blood_type)

      self.blood_availability_combo_box.clear()
      for availability in available_availabilities_list:
         self.blood_availability_combo_box.addItem(availability)

      self.blood_age_group_combo_box.clear()
      for age in available_age_groups_list:
         self.blood_age_group_combo_box.addItem(age)


   def enter_blood_donor_list_options(self):
      """
      This method updates the Organ Donor List and Recommended Doctors tables based on the currently
      selected options.
      """
      region = self.organ_region_combo_box.currentText()
      blood_type = self.blood_type_combo_box.currentText()
      age_group = int(self.blood_age_group_combo_box.currentText())

      availability_date = datetime.datetime.today() - datetime.timedelta(days=56)
      availability_date = availability_date.strftime('%Y-%m-%d')

      if self.blood_availability_combo_box.currentText() == 'Available':
         availability_comparison = f"last_donation <= '{availability_date}'::date"
      else:
         availability_comparison = f"last_donation > date'{availability_date}'::date"

      try:
         cursor = self.__conn.cursor()

         select_donors_command = f"SELECT blood_donor_id, name FROM Blood_Donor where region = '{region}' AND blood_type = '{blood_type}' AND {availability_comparison} AND age = {age_group}"
         cursor.execute(select_donors_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.blood_donors_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.blood_donors_table.insertRow(idx)
            self.blood_donors_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.blood_donors_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))

         self.blood_donors_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Enter Blood Donor List Options Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   # --Donor Match List View-------------------------------------------

   def update_donor_match_list_view(self):
      """
      This method updates the selection options for the for the Donor Match List View
      """
      try:
         cursor = self.__conn.cursor()

         select_patients_command = f"SELECT patient_id, name, blood_type, region, need FROM Patient"
         cursor.execute(select_patients_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.patients_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.patients_table.insertRow(idx)
            self.patients_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.patients_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.patients_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.patients_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.patients_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))

         self.patients_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Enter Blood Donor List Options Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   def enter_donor_match_list_options(self):
      """
      This method updates the Organ Donor List and Recommended Doctors tables based on the currently
      selected options.
      """
      patient = self.patients_table.currentRow()

      blood_type = self.patients_table.item(patient, 2).text()
      region = self.patients_table.item(patient, 3).text()
      need = self.patients_table.item(patient, 4).text()

      try:
         cursor = self.__conn.cursor()
         self.matching_donors_table.setRowCount(0)

         if need == 'blood':
            if blood_type in ['AB+', 'AB-']:
               select_donors_command = f"SELECT blood_donor_id, name, blood_type, region FROM Blood_Donor where region = '{region}'"
            else:
               select_donors_command = f"SELECT blood_donor_id, name, blood_type, region FROM Blood_Donor where region = '{region}' AND blood_type IN ('O+', 'O-', '{blood_type}')"

            cursor.execute(select_donors_command)
            self.__conn.commit()
            rows = cursor.fetchall()

            for data in rows:
               idx = rows.index(data)
               self.matching_donors_table.insertRow(idx)
               self.matching_donors_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
               self.matching_donors_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
               self.matching_donors_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
               self.matching_donors_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
               self.matching_donors_table.setItem(idx,4,QtWidgets.QTableWidgetItem('N/A'))

         else:
            if blood_type in ['AB+', 'AB-']:
               select_donors_command = f"SELECT organ_donor_id, name, blood_type, region, organ_name FROM Organ_Donor where region = '{region}' AND organ_name = '{need}'"
            else:
               select_donors_command = f"SELECT organ_donor_id, name, blood_type, region, organ_name FROM Organ_Donor where region = '{region}' AND blood_type IN ('O+', 'O-', '{blood_type}') AND organ_name = '{need}'"

            cursor.execute(select_donors_command)
            self.__conn.commit()
            rows = cursor.fetchall()

            for data in rows:
               idx = rows.index(data)
               self.matching_donors_table.insertRow(idx)
               self.matching_donors_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
               self.matching_donors_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
               self.matching_donors_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
               self.matching_donors_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))
               self.matching_donors_table.setItem(idx,4,QtWidgets.QTableWidgetItem(str(data[4])))

         self.matching_donors_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Enter Donor Match List Options Failure", str(e))
         self.__conn.rollback()
         return False

      return True

   # --Income Report View----------------------------------------------

   def update_income_report_view(self):
      """
      This method updates the Income Report View which displays the total income for each hospital from transplants.
      """
      try:
         cursor = self.__conn.cursor()

         select_incomes_command = f"SELECT Hospital.hospital_id, Hospital.name, SUM(cost) FROM Transplant INNER JOIN Hospital ON Transplant.hospital_id = Hospital.hospital_id GROUP BY Hospital.hospital_id"
         cursor.execute(select_incomes_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.income_report_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.income_report_table.insertRow(idx)
            self.income_report_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.income_report_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.income_report_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))

         self.income_report_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Income Report Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   def on_income_report_push_btn_clicked(self):
      """
      This method is a slot that triggers the update_income_report function when the update_income_report_push_btn is clicked.
      """
      self.update_income_report_view()

   # --Operations Report View----------------------------------------------

   def update_operations_report_view(self):
      """
      This method updates the Income Operations Report View which displays the Doctor's Name grouped by Region along with the 
      Number of Operations sorted from the highest to lowest Number of Operations.
      """
      try:
         cursor = self.__conn.cursor()

         select_operations_command = """SELECT Doctor.doctor_id, Doctor.name, Doctor.region, COUNT(*)
                                        FROM Transplant JOIN Tp_Operates ON Transplant.tp_id = Tp_Operates.tp_id 
                                        JOIN Doctor ON Doctor.doctor_id = Tp_Operates.doctor_id 
                                        GROUP BY Doctor.doctor_id
                                        ORDER BY region ASC, count DESC"""
                                        
         cursor.execute(select_operations_command)

         self.__conn.commit()

         rows = cursor.fetchall()

         self.operations_report_table.setRowCount(0)

         for data in rows:
            idx = rows.index(data)
            self.operations_report_table.insertRow(idx)
            self.operations_report_table.setItem(idx,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.operations_report_table.setItem(idx,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.operations_report_table.setItem(idx,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.operations_report_table.setItem(idx,3,QtWidgets.QTableWidgetItem(str(data[3])))

         self.operations_report_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         self.report_error("Update Operations Report Failure", str(e))
         self.__conn.rollback()
         return False

      return True


   def on_operations_report_push_btn_clicked(self):
      """
      This method is a slot that triggers the update_operations_report function when the update_operations_report_push_btn is clicked.
      """
      self.update_operations_report_view()
