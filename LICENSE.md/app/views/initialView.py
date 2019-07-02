import app
from vendor.application.components.mvc.view import View 

class Initial(View):
    def show(self):
        self.clear()
        print("==========================================")
        print("---------------- Welcome ------------------")
        print("==========================================\n")
        option = self.input_information("1 - Start Application"
                                        +"\n2 - Settings"
                                        +"\n3 - Tests"
                                        +"\n0 - Exit"
                                        +"\n\nChoose an option: ")
        if(option == "0"):
            path = "exit"
        elif(option == "1"):
            path = "home"
        elif(option == "2"):
            path = "settings"
        elif(option == "3"):
            path = "tests"
        else:
            path = "/"

        app.routes.go(path)
        
        