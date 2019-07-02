import os
import app

class View():
	def show(self, function, variables = []):
		pass

	def clear(self):
		try:
			clear = lambda: os.system('cls')
			clear()
			clear = lambda: os.system('clear')
			clear()
		except Exception as identifier:
			clear = lambda: os.system('clear')
			clear()

	def input_information(self, question = ""):
		receiver = input(question)
		if(receiver == "cancel()" or receiver == "back()"):
			if(app.gps.main_section_position != "main"):
				app.routes.go(app.gps.previous)
			else:
				app.routes.go("main")
		else:
			return receiver

	def get_confirmation(self, question):
		answer = ""
		while (not answer) or (answer != "y" and answer != "n"):
			answer = input(question + "(y/n): ")
		if answer == "y":
			return True
		else:
			return False