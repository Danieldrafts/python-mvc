import configparser
import reprlib

class Database:

	def __init__(self, database_connection = None):
		self.config = configparser.ConfigParser()
		self.config.sections()
		self.config.read('enviroment.ini')

		if (database_connection == None):
			self.database_connection = 'DATABASE'
		else: 
			self.database_connection = database_connection

		self.config.sections()
		[self.database_connection]

	def connect(self):
		try:
			if (self.get_driver() == 'mysql'):			
					self.connection_to_mysql()			
			elif (self.get_driver() == 'sqlserver'):
					self.connection_to_sqlserver()		
			elif (self.get_driver() == 'oracle'):
					print('Oracle connection not yet configured')
		except Exception as exception:
			print("Error to conect to database: "+self.config[self.database_connection]['database']+"\n")
			print (exception)

	def get_driver(self):
		return self.config[self.database_connection]['driver']

	def connection_to_mysql(self):
		import mysql.connector
		self.connection = mysql.connector.connect(
							user=self.config[self.database_connection]['user'],
							password=self.config[self.database_connection]['password'],
                            host=self.config[self.database_connection]['host'],
                            database=self.config[self.database_connection]['database'])
		self.cursor = self.connection.cursor()

	def connection_to_sqlserver(self):
		import pymssql
		self.connection = pymssql.connect(
							host=self.config[self.database_connection]['host'],
							user=self.config[self.database_connection]['user'],
							password=self.config[self.database_connection]['password'],                            
                            database=self.config[self.database_connection]['database'])
		self.cursor = self.connection.cursor()
	
	def close(self):
			self.connection.close()

	def set_prepared_statement(self):
		if (self.get_driver() == 'mysql'):
			self.cursor = self.connection.cursor(prepared=True)
		elif (self.get_driver() == 'sql_server'):
			pass
		elif (self.get_driver() == 'oracle'):
			#need to check for implementation 
			pass
		

	