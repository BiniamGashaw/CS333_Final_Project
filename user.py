class User:
    def __init__(self, name):
        self.name = name
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append((operation, result))

    def get_history(self):
        return self.history
