from vendor.application.components.classes.route import Route
from routes.settingsRoutes import SettingsRoutes
from routes.testsRoutes import TestsRoutes

from controllers.mainController import MainController
from controllers.exampleController import ExampleController #Cada controller usado nas rotas deve ser importado (exemplo)
import app

class MainRoutes(Route):
	def go(self, path = ""):
	#O "path" escolhido pelo usuário é analisado para decidir qual função da rota será acionada, ex: main. 
		if path == "1":
			self.start()
		elif path == "2":
			settings_routes = SettingsRoutes()
			settings_routes.go()
		elif path == "3":
			tests_routes = TestsRoutes()
			tests_routes.go()
		else:
			self.main()

	def main(self):
		controller = MainController()
		path = controller.initial()
		self.go(path)

	def start(self):
		controller = ExampleController()
		controller.index()