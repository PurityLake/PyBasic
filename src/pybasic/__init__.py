from typing import IO


class PyBasicFileInterpreter:
    def __init__(self, filename: str):
        self.file: IO = open(filename, 'r')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def interpret(self):
        print("Interpreting...")
