from vendor.application.components.classes.route import Route
from controllers.exampleController import ExampleController
import app

class ExampleRoutes(Route):
	def __init__(self):
		self.controller = ExampleController()
		app.gps.update_main_section("home")

	def go(self, path = ""):
		app.gps.update_coordinates(path)

		if(path == "home/standard"):			
			self.controller.standard()
		elif(path == "home/using-models"):			
			self.controller.using_models()
		elif(path == "home/using-another-database"):
			self.controller.using_another_database()
		else:
			app.gps.update_coordinates("home")
			app.gps.update_main_section("main")
			self.controller.index()

	