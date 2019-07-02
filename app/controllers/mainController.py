import app
from vendor.application.components.mvc.controller import Controller #Classe abstrata de Controller (necessário).
from views.initialView import Initial #Importe suas views (exemplo)


class MainController(Controller):
	#Exemplo:
	def initial(self):
		#Exemplo:
	#  Programa apresenta opções, a resposta é enviada como parâmetro para a rota GO que identificará qual caminho será tomado.
		view = Initial()	
		view.show()