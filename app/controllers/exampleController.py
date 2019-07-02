import app
from vendor.application.components.mvc.controller import Controller #Classe abstrata de Controller (necessário).
from models.exampleModel import ExampleModel #Importe suas models (exemplo)
from views.examplesView import ExamplesView #Importe suas views (exemplo)
from components.classes.exampleClass import ExampleClass #Importe suas classes (exemplo).

class ExampleController(Controller):
#Exemplos:
	def __init__(self):
		self.view = ExamplesView()

	def index(self):
		self.view.index()

	def standard(self):

		var1 = "Variavel 1"
		var2 = "Variavel 2"
		var3 = "Variavel 3"
		teste = ExampleClass() 

		#Send yours variables to view
		self.view.standard([var1,var2,var3])

  #Example of communication with databases (SQL)
	def using_models(self):
		# --- Create model object ----
		#obs: the database connection default is [DATABASE] of the enviroment.ini
		myTable = ExampleModel()

		#==================== MySql ============================================
		# ---- select example -----
		#	obs: preferably make secure queries using Prepeared Statement as format below:
		#			model.select (sql, parameters, prepared = True)
		#result = myTable.select("select * from users where name = 'Teste Integrador' and email = teste@sonda.com")
			#OR
		#result = myTable.select("select * from users where name = ? and email = ?", ("Teste Integrador","teste@sonda.com"), prepared=True)
		#print(result)

		# ---- insert, update, delete example ----
		#myTable.execute_sql_command("insert into myTable(description) values('example')")
			#OR
		#myTable.execute_sql_command("insert into myTable(description) values(?)", ("Example"))
		#=======================================================================

		#================== SQL Server ==========================================
		# ------ Select --------
		#result = myTable.select("select top 1 * from call_req where ref_num = '1873271'")
			#OR
		#result = myTable.select("select top 1 * from call_req where ref_num = %s",("1873271"), prepared=True)

		# ---- insert, update, delete example ----
		#result = myTable.execute_sql_command("insert into contatos(nome) values('example')")
			#OR
		#myTable.execute_sql_command("insert into contatos(nome) values(%s)", ("Example2"), prepared=True)
		#=========================================================================

		self.view.using_models()

#Example Create a model object stating which connection to use.
	def using_another_database(self):	
		# obs: the connection must be created in the environment.ini file.
		connection = 'SECOND_DATABASE_EXAMPLE'
		myTable = ExampleModel(connection)
				
		#From now on all model operations will be performed on the other indicated database.
		#...
		self.view.using_another_database()

#fim exemplo
