import app
from vendor.application.components.classes.route import Route
from controllers.settingsController import SettingsController
from views.settingsView import SettingsView

class SettingsRoutes(Route):
	def __init__(self):
		self.controller = SettingsController()
		app.gps.update_main_section("settings")

	def go(self, path = ""):
		app.gps.update_coordinates(path)

		if (path =="settings"):
			app.gps.update_coordinates("settings")
			app.gps.update_main_section("main")
			self.controller.index()
		elif(path == "settings/current-settings"):
			self.controller.current_settings()
		elif(path == "settings/new-setting"):
			self.controller.create_new_setting()
		elif(path == "settings/new-setting/create-database-settings"):
			self.controller.create_new_database_settings()
		elif(path == "settings/new-setting/create-other-settings"):
			self.controller.create_other_settings()
		elif(path == "settings/modify-setting"):
			self.controller.modify_settings_index()
		elif(path == "settings/delete-setting"):
			self.controller.delete_settings_index()
		else:
			app.gps.update_coordinates("settings")
			app.gps.update_main_section("main")
			self.controller.index()
		
	