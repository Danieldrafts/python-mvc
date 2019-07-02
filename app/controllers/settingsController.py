import app
from vendor.application.components.mvc.controller import Controller #Classe abstrata de Controller (necessário).
from views.settingsView import SettingsView
from vendor.application.components.classes.enviroment import Enviroment

class SettingsController(Controller):

	def __init__(self):
		self.view = SettingsView()

	def index(self):
		self.view.show()

	def current_settings(self):		
		settings = app.env.get_configurations()
		self.view.current_settings(settings)

	def create_new_setting(self):
		self.view.create_setting_index()

	def create_new_database_settings(self):
		database_information = self.view.create_database_settings()
		section_name = database_information[1]
		database_information = database_information[0]
		app.env.write_new_setting(section_name, database_information)
		app.routes.back()

	def create_other_settings(self):
		configuration = self.view.create_other_settings()		
		if configuration != False:
			section_name = configuration[1]
			configuration = configuration[0]
			app.env.write_new_setting(section_name, configuration)
		app.routes.back()

	def modify_settings_index(self):
		options = app.env.get_sections()
		section_name = self.view.modify_settings_index(options)
		self.modify_settings(section_name)

	def modify_settings(self, configuration_section_name):
		settings = app.env.get_section_settings(configuration_section_name)
		if(settings != False):
			settings = self.view.modify_settings(configuration_section_name, settings)		
		if(settings != False):
			app.env.edit_configuration_section(configuration_section_name, settings)
		else:
			print("The changes were aborted!")
		app.routes.back()

	def delete_settings_index(self):
		sections = app.env.get_sections()
		section_name = self.view.delete_settings_index(sections)
		self.delete_settings(section_name)

	def delete_settings(self, configuration_section_name):
		settings = app.env.get_section_settings(configuration_section_name)
		settings = self.view.delete_setting(configuration_section_name, settings)
		if settings == True:
			app.env.delete_configuration_section(configuration_section_name)			
		else:
			input("Aborted!")
		app.routes.back()
