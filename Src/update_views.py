

"""Script to easily update all of the QT Designer generated .ui files"""


import os

current_path = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_path, "BloodOrganDatabaseManager", "Views", "UI")

dir_list = os.listdir(ui_path)

for file in dir_list:
   
   if ".ui" in file:
      name = file.split(".")[0]
      command = "pyuic5 -x {} -o {}".format(os.path.join(ui_path, file), os.path.join(ui_path, name + ".py"))
      os.system(command)