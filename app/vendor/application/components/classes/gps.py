import configparser
from vendor.application.components.classes.session import Session

class GPS:
    def __init__(self, session_file):
        self.__session_file = session_file
        self.session = configparser.ConfigParser()
        self.session.sections()
        self.session.read(self.__session_file)
        self.__write_default_info()

    @property
    def current(self):
        position = self.__get_file_information('now')
        return position

    @property
    def previous(self):
        position = self.__get_file_information('previous')
        return position

    @property
    def main_section_position(self):
        position = self.__get_file_information('section_main')
        return position

    def update_coordinates(self, coordinates):
        current_location = self.current
        if(current_location != coordinates):            
            self.__update_position_information('previous', current_location)
        self.__update_position_information('now', coordinates)

    def update_main_section(self, path):
        self.__update_position_information('section_main', path)
        
    def __get_file_information(self, information):
        return self.session['position'][information]
        
    def __write_default_info(self):
        self.session['position'] = {
                                        "now":"main",
                                        "previous": "main",
                                        "section_main": "main",
        }
        with open(self.__session_file, 'w') as session_file:
            self.session.write(session_file)

    def __update_position_information(self, information, value):
        try:
            self.session.set('position', information, value)
            with open(self.__session_file, 'w') as session_file:
                self.session.write(session_file)
            return True
        except Exception as error:
            return False

    def all(self):
        return self.session['position']
    
    def dump(self):
        informations = self.all()
        print('-----------------\nPOSITIONS\n-----------------')
        for information in informations:
            print(information+": "+informations[information])
    
  
  