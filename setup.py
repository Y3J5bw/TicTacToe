from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "itertools", "tkinter", "tkinter.ttk", "game"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "tictactoe",
    options = options,
    version = "0.1",
    description = '',
    executables = executables
)
