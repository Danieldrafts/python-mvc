from vendor.application.components.classes.route import Route
from controllers.testController import TestController

class TestsRoutes(Route):
	def __init__(self):
		self.controller = TestController()

	def go(self, path = ""):
		if(path == "ROUTE 1"):
			pass
		elif(path == "ROUTE 2"):
			pass
		else:
			self.controller.tests()
		
	