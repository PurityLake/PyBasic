class PyBasicFileInterpreter:
    def __init__(self, filename: str):
        self.filename: str = filename

    def interpret(self):
        try:
            with open(self.filename) as f:
                print(f)
        except IOError:
            print(f'Failed to open file "{f}')
