import app
import os, platform

from vendor.application.components.mvc.controller import Controller #Classe abstrata de Controller (necessário).
from models.exampleModel import ExampleModel


class TestController(Controller):
	def tests(self):
			#Create a model object stating which connection to use.
			# obs: the connection must be created in the environment.ini file.
		connection = 'SECOND_DATABASE_EXAMPLE'
		myTable = ExampleModel(connection)
			
			#From now on all model operations will be performed on the other indicated database.
			#...
		print('This is just a test.\n')
		print('See the file: ExampleController, function tests() to learn how to use multiples databases!')
		app.routes.go("exit")
		
		
		


