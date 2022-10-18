from pybasic import PyBasicFileInterpreter

if __name__ == "__main__":
    try:
        interpreter = PyBasicFileInterpreter("hello.bsc")
    except IOError as e:
        print("Oopsie")
