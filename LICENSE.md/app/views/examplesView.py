import app #this import is required to direct routes 
from vendor.application.components.mvc.view import View

class ExamplesView(View):		
	def index(self):
		self.clear()
		print("===========================\n\tExamples\n===========================\n")
		option = self.input_information("1 - Standard view with variables"
										+"\n2 - Using Models"
										+"\n3 - Using Another Database"
										+"\n0 - Return Main Menu\n\n"
										+"Option: ")
		
		if(option == "0"):
			app.routes.go(app.routes.go(app.gps.main_section_position))
		elif(option == "1"):
			app.routes.go("home/standard")
		elif(option == "2"):
			app.routes.go("home/using-models")
		elif(option == "3"):
			app.routes.go("home/using-another-database")
		else:
			app.routes.go("home")

	def standard(self, variables):
		self.clear()
		print("Your application is running!")
		for variable in variables:
			print(variable)
		print("\nSee example file: controllers/exampleController.py and views/examplesView.py")
		self.input_information("\n Press enter to back\n")
		app.routes.back()
	
	def using_models(self, variables = []):
		self.clear()
		print("# --- Create a model object ----"
		+"\n [obs: the database connection default is [DATABASE] of the enviroment.ini]"
		+"\n myTable = ExampleModel()\n\n"

		"\n#==================== MySql ============================================"
		+"\n \t# ---- select example -----"
		+"\n #	[obs: preferably make secure queries using Prepeared Statement as format below:"
		+"\n #			model.select (sql, parameters, prepared = True)]\n\n"

		+'\n result = myTable.select("select * from users where name = ? and email = ?", ("Teste Integrador","teste@sonda.com"), prepared=True)'
		+"\n print(result)\n\n"

		+"\n \t# ---- insert, update, delete example ----"
		+"\n myTable.execute_sql_command("+'"'+"insert into myTable(description) values('example')"+'")'
			+"\n\t\t OR"
		+'\n myTable.execute_sql_command("insert into myTable(description) values(?)", ("Example"))'
		+"\n #=======================================================================\n\n"

		+"\n #================== SQL Server =========================================="
		+"\n \t# ------ Select --------"
		+'\n result = myTable.select("select top 1 * from call_req where ref_num = %s",("1873271"), prepared=True)\n\n'

		+"\n \t# ---- insert, update, delete example ----"
		+"\n myTable.execute_sql_command("+'"'+"insert into contatos(nome) values('example')"+'")'
			+"\n\t\t OR"
		+'\n myTable.execute_sql_command("insert into contatos(nome) values(%s)", ("Example2"), prepared=True)'
		+"\n #=========================================================================")
		print('\n\n See the file controllers.exampleController in function "using_models()" to view details\n')
		self.input_information("\n Press enter to back\n")
		app.routes.back()
	
	def using_another_database(self, variables = []):
		self.clear()
		
		print("connection = 'SECOND_DATABASE_EXAMPLE'"
			   +"\nmyTable = ExampleModel(connection)")
		print("(obs: the connection must be created in the environment.ini file.)")
		print('\n See the file controllers.exampleController in function "using_another_database()" to view details\n')
		self.input_information("\n Press enter to back\n")
		app.routes.back()