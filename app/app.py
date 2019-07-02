from vendor.application.components.classes.enviroment import Enviroment
from vendor.application.components.classes.session import Session
from vendor.application.components.classes.gps import GPS
from routes.routes import Routes

#This file loads all objects essential for application, which must be shared by subsequent classes

session = Session()
session.start_session()
gps = GPS(session.session_file)
routes = Routes()
env = Enviroment()

def exit_application():
    session.end_session()
    print("\nExit application {}...".format(env.app_name))
    exit()