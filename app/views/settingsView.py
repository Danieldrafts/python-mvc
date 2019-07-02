import app
from vendor.application.components.mvc.view import View


class SettingsView(View):
	def show(self, function = "index", variables = []):
		self.clear()
		if(function == "index"):
			return self.index()
		
	def index(self):
		print("==========================================")
		print("-------------- Settings ------------------")
		print("==========================================\n")

		option = self.input_information(
			"1 - Show current settings."
			+"\n2 - Create new setting."
			+"\n3 - Modify setting."
			+"\n4 - Delete setting."
			+"\n0 - Return to main menu.\n"
		)
		if option == "0":
			path = "main"
		elif option == "1":
			path = "settings/current-settings"
		elif option == "2":
			path = "settings/new-setting"
		elif option == "3":
			path = "settings/modify-setting"
		elif option == "4":
			path = "settings/delete-setting"
		else:
			path = "settings"

		app.routes.go(path)

	def current_settings(self, settings):
		print("\tCONFIGURATION FILE \nCurrent Settings:\n")
		for section in settings.sections():
			print("["+section+"]")
			for item in settings[section]:
				print("- "+item+": "+settings[section][item])
			print("============================")
		wait = self.input_information("\n<<-- Return")

		app.routes.back()

	def create_setting_index(self):
		print("Setting type:\n")
		option = self.input_information("1 - New Database\n2 - Other\n") # input("1 - New Database\n2 - Other\n")
		if(option == "1"):
			path = "settings/new-setting/create-database-settings"
		elif(option == "2"):
			path = "settings/new-setting/create-other-settings"

		app.routes.go(path)

	def create_database_settings(self):
		section_name = self.input_information("Section Database Name: ").upper()# input("Section Database Name: ")
		driver = self.input_information("Driver (mysql, sqlserver, oracle): ")# input("Driver (mysql, sqlserver, oracle): ")
		host = self.input_information("Host: ")# input("Host: ")
		port = self.input_information("Port: ")# input("Port: ")
		database = self.input_information("Database: ")# input("Database: ")
		user = self.input_information("User: ")# input("User: ")
		password = self.input_information("Password: ")# input("Password: ")

		configuration = {
			"driver": driver,
			"host": host,
			"port": port,
			"database": database,
			"user": user,
			"password": password
		}
		return [configuration, section_name]

	def create_other_settings(self):
		print("\tNEW CONFIGURATION")
		section_name = self.input_information("Configuration Section Name: ").upper()

		while not section_name:
			self.clear()
			print("The configuration need a Section Name!")
			section_name = self.input_information("Configuration Section Name: ").upper()		
		configuration = {}
		answer = True

		while (answer == True):
			self.clear()
			print("\tNEW CONFIGURATION")
			self.__print_configuration(section_name, configuration)
			item_name = self.input_information("Option Name: ")
			value = self.input_information("{} Value: ".format(item_name))

			if not item_name:
				pass
			else:
				configuration[item_name] = value
				answer = self.get_confirmation("Add new item?")

		self.clear()
		print("\tNEW CONFIGURATION")
		self.__print_configuration(section_name, configuration)
		
		confirm = self.get_confirmation("confirm the above configuration?")
		if confirm == True:
			return [configuration, section_name]
		else:
			return False

	def __print_configuration(self, section_name, configuration_dictionary):
		print("[{}]".format(section_name))
		for item, value in configuration_dictionary.items():
			print(item+": "+value)

	def modify_settings_index(self, sections):
		print("\tCHOOSE THE CONFIGURATION:\n")
		for section in sections:
			print("- ["+section+"]")
		section = self.input_information("Enter the setting name: ").upper()
		return section
	
	def modify_settings(self, section, section_settings):
		self.clear()
		print("Current settings:")
		self.__print_configuration(section, section_settings)
		print("\nEditing configuration section:\n [{}]".format(section))
		for item in section_settings.items():
			section_settings[item[0]] = self.input_information(item[0]+": ")
		self.clear()
		self.__print_configuration(section, section_settings)
		confirm_change = self.get_confirmation("Confirm the changes?")

		if (confirm_change == True):
			return section_settings
		else:
			return False

	def delete_settings_index(self, sections):
		print("\tCHOOSE THE CONFIGURATION:\n")
		for section in sections:
			print("- ["+section+"]")
		section = self.input_information("Enter the setting name: ").upper()
		return section
	
	def delete_setting(self, section, section_settings):
		self.clear()
		print("Current settings:")
		self.__print_configuration(section, section_settings)
		confirm = self.get_confirmation("Confirms the deletion of the {} configuration?".format(section))
		
		return confirm


			