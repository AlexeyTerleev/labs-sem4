import shelve


class Save:
    def __init__(self):
        self.file = shelve.open('data/data')

    def save(self, name):
        self.file['name'] = name

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except:
            return 0

    def __del__(self):
        self.file.close()
