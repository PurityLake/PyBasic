from pybasic import PyBasicFileInterpreter


def test_interpreter_create():
    interpreter = PyBasicFileInterpreter("hello.bsc")
    assert interpreter.filename == "hello.bsc"
