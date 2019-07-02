import app
from vendor.application.components.classes.route import Route
from routes.exampleRoutes import ExampleRoutes
from routes.settingsRoutes import SettingsRoutes
from routes.testsRoutes import TestsRoutes
from controllers.mainController import MainController


class Routes(Route):
	def go(self, path = "main"):
	#O "path" escolhido pelo usuário é analisado para decidir qual função da rota será acionada, ex: main. 
		#obs: get_prefix(path) identifica o primeiro termo da rota que é a chave para acionar o controller correto
		if (self.get_prefix(path) == "home"):
			examples = ExampleRoutes()
			examples.go(path)
		elif (path == "exit"):
			app.exit_application()
		elif (self.get_prefix(path) == "settings"):
			settings_routes = SettingsRoutes()
			settings_routes.go(path)
		elif (self.get_prefix(path) == "tests"):
			tests_routes = TestsRoutes()
			tests_routes.go(path)
		else:
			controller = MainController()
			controller.initial()
			app.gps.update_main_section("main")
	