import configparser
import os, platform, datetime, hashlib

class Session:
    @property
    def session_id(self):
        return self.__session_id
    
    @property
    def session_file(self):
        return self.__session_file

    def start_session(self):
        self.__generate_session_id()
        self.__create_session_file(self.__timestamp)
        

    def end_session(self):
        os.remove(self.__session_file)

    def __generate_session_id(self):
        date = datetime.datetime.now()
        now = date.strftime("%c")
        hasher = hashlib.md5()
        timestamp = str(date.timestamp()).replace(".","")
        self.__timestamp = timestamp        
        hasher.update(now.encode())
        self.__session_id = hasher.hexdigest()
    
    def __create_session_file(self, timestamp):
        file_name = "session"+timestamp+".ini"
        exists = self.__verify_if_file_exists("storage/sessions", file_name)
        if (exists == False):
            path = self.__adapt_path_by_os("storage/sessions/"+file_name)
            self.__session_file = path
            self.session = configparser.ConfigParser()
            self.session.sections()
            self.session.read(self.__session_file)
            self.__write_default_info()
        else:
            print("The file aready exists!")

    def __verify_if_file_exists(self, directory, file_name):       
        directory = self.__adapt_path_by_os(directory)        
        files_in_directory = os.listdir(directory)
        found = False
        for file_listed in files_in_directory:
            if file_listed == file_name:
                found = True
        
        return found

    def __adapt_path_by_os(self, path):
        oparation_system = platform.system()
        if(oparation_system == "Windows"):
            path = path.replace('/', '\\')
        elif(oparation_system == "Linux"):
            path = path.replace("\\", '/')
        return path

    def __write_default_info(self):
        session_info = {}
        self.session['session'] = {"id": self.__session_id, "time" : datetime.datetime.now().strftime("%c")}
        with open(self.__session_file, 'w') as session_file:
            self.session.write(session_file)

    def write_session_information(self, section, information = []):
        try:
            self.session[section] = settings
            with open(self.__session_file, 'w') as session_file:
                self.session.write(session_file)
            return True
        except Exception as error:
            return False
    
    def update_session_information(self, section, information, value):
        try:
            self.session.set(section, information, value)
            with open(self.__session_file, 'w') as session_file:
                self.session.write(session_file)
            return True
        except Exception as error:
            return False
            
    def get_session_information(self, section):
        session_information = {}
        for information in self.session[section]:
            session_information[information] = self.session[section][information]
        return session_information
