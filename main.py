from pybasic import PyBasicFileInterpreter

if __name__ == "__main__":
    try:
        with PyBasicFileInterpreter("hello.bsc") as interp:
            interp.interpret()
    except IOError as e:
        print("Oopsie")
