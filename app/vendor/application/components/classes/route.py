import app

class Route:
    def go(self, path):
        pass

    def get_prefix(self, path):
        path = path.split('/')
        path = path[0]
        return path
    
    def back(self):
        self.go(app.gps.previous)