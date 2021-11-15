

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
      if row is -1:
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

         self.hospital_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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
      if row is -1:
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

         self.doctor_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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
      if row is -1:
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

         self.patient_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         print(e)
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

      try:

         cursor = self.__conn.cursor()

         insert_command1 = f"INSERT INTO Organ_Donor (organ_donor_id, name, age, blood_type, drug_use, last_tattoo_date, region, organ_name) VALUES ({organ_donor_id}, '{name}', {age}, '{blood_type}', B'{drug_use}', '{last_tattoo_date}', '{region}', '{organ_name}')"
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
         print(e)
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
         print(e)
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
         print(e)
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
      drug_use = self.patient_need_line_edit.text()
      last_tattoo_date = self.blood_donor_last_tattoo_date_line_edit.text()
      region = self.blood_donor_region_line_edit.text()
      last_donation = self.blood_donor_last_donation_line_edit.text()

      med_history_list = self.blood_donor_med_history_line_edit.text().split(",")
      chronic_diseases_list = self.blood_donor_chronic_diseases_line_edit.text().split(",")
      contact_info_list = self.blood_donor_contact_info_line_edit.text().split(",")

      try:

         cursor = self.__conn.cursor()

         insert_command1 = f"INSERT INTO Blood_Donor (blood_donor_id, name, age, blood_type, drug_use, last_tattoo_date, region, last_donation) VALUES ({blood_donor_id}, '{name}', {age}, '{blood_type}', '{last_tattoo_date}', '{region}', '{last_donation}')"
         cursor.execute(insert_command1)

         for medication in med_history_list:
            insert_command2 = f"INSERT INTO BD_Med_Hist (organ_donor_id, med_history) VALUES ({blood_donor_id}, '{medication}')"
            cursor.execute(insert_command2)

         for disease in chronic_diseases_list:
            insert_command3 = f"INSERT INTO BD_Chronic_Disease (organ_donor_id, chronic_disease) VALUES ({blood_donor_id}, '{disease}')"
            cursor.execute(insert_command3)

         for contact in contact_info_list:
            insert_command4 = f"INSERT INTO BD_Contact (organ_donor_id, contact) VALUES ({blood_donor_id}, '{contact}')"
            cursor.execute(insert_command4)

         self.__conn.commit()

      except Exception as e:
         print(e)
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

         delete_command2 = f"DELETE FROM BD_Med_Hist WHERE organ_donor_id = {blood_donor_id}"
         cursor.execute(delete_command2)

         delete_command3 = f"DELETE FROM BD_Chronic_Disease WHERE organ_donor_id = {blood_donor_id}"
         cursor.execute(delete_command3)

         delete_command4 = f"DELETE FROM BD_Contact WHERE organ_donor_id = {blood_donor_id}"
         cursor.execute(delete_command4)

         self.__conn.commit()

      except Exception as e:
         print(e)
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
         print(e)
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

         insert_command = f"INSERT INTO Blood_Bag (blood_bag_id, rh, used, blood_donor_id) VALUES ({blood_bag_id}, '{rh}', B'{used}', {blood_donor_id})"
         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
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
         print(e)
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
         print(e)
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
         print(e)
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
         print(e)
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
            self.organ_table.setItem(idx,5,QtWidgets.QTableWidgetItem(str(data[5])))

         self.organ_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         print(e)
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

         insert_command1 = f"INSERT INTO Transplant (tp_id, organ, status, organ_donor_id, patient_id, hospital_id) VALUES ({transplant_id}, '{organ}', {status}, {organ_donor_id}, {patient_id}, {hospital_id})"
         cursor.execute(insert_command1)

         for doctor in doctor_ids:
            insert_command2 = f"INSERT INTO TP_Operates (tp_id, doctor_id) VALUES ({transplant_id}, {doctor}"
            cursor.execute(insert_command2)

         self.__conn.commit()

      except Exception as e:
         print(e)
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
         print(e)
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
               doctor_ids.append(doctor[0])
            doctor_ids = ", ".join(doctor_ids)
            self.transplant_table.setItem(idx,6,QtWidgets.QTableWidgetItem(doctor_ids))

         self.transplant_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      except Exception as e:
         print(e)
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

         insert_command = f"INSERT INTO Transfusion (tf_id, organ, status, organ_donor_id, patient_id, hospital_id) VALUES ({transfusion_id}, '{status}', {blood_donor_id}, {doctor_id}, {patient_id}, {hospital_id})"
         cursor.execute(insert_command)

         self.__conn.commit()

      except Exception as e:
         print(e)
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
         print(e)
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
         print(e)
         return False

      return True