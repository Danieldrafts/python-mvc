from vendor.application.components.database import Database

class Model:
	def __init__(self, connection = None):
		self.connection = connection		

#Selects in SQL
	def select(self, sql, parameters = (), prepared=False):
		if(prepared):
			return self.__select_prepared(sql, parameters)
		else:
			return self.__select_raw(sql)

#Insert, Update and Delete 
	def execute_sql_command(self, sql, parameters = (), prepared=False):
		if(prepared):
			return self.__sql_command_prepared(sql, parameters)
		else:
			return self.__sql_command_raw(sql)

#private Prepared Statement select
	def __select_prepared(self, sql, parameters = ()):
		try:
			db = Database(self.connection)
			db.connect()
			db.set_prepared_statement()
			result = db.cursor.execute(sql, parameters)
			result = db.cursor.fetchall()
			db.close()
			return result
		except Exception as exception:
			print('An error occurred while executing a SQL command.\nDetails:')
			print(exception)

#private select without Prepared Statement
	def __select_raw(self, sql):
		try:
			db = Database(self.connection)
			db.connect()
			result = db.cursor.execute(sql)
			result = db.cursor.fetchall()
			db.connection.close()
			return result
		except Exception as exception:
			print('An error occurred while executing a SQL command.\nDetails:')
			print(exception)
			
#private Prepared Statement sql command
	def __sql_command_prepared(self, sql, parameters = ()):
		try:
			db = Database(self.connection)
			db.connect()
			db.set_prepared_statement()
			result = db.cursor.execute(sql, parameters)
			db.connection.commit()
			db.close()
			return result
		except Exception as exception:
			print('An error occurred while executing a SQL command.\nDetails:')
			print(exception)

#private sql command without Prepared Statement
	def __sql_command_raw(self, sql):
		try:
			db = Database(self.connection)
			db.connect()
			db.cursor.execute(sql)
			db.connection.commit()
			db.connection.close()
			return True
		except Exception as exception:
			print('An error occurred while executing a SQL command.\nDetails:')
			print(exception)
			return False