import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
includefiles = ['Bin', 'File', 'Html', 'Pdf', 'Readme.txt']
includes = []
build_exe_options = {"includes": includes,
                     "packages": ["os", "idna", "encodings", "asyncio", "requests", "base64"],
                     "excludes": ["tkinter"],
                     "include_files": includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = None

setup(name="vepynet",
        version="0.1",
        description="Documento vmoney via (API) ",
        author='Eduardo Padilha',
        author_email='padilha@ventureservice.com.br',
        options={"build_exe": build_exe_options},
        executables=[Executable("vepynet.py", base=base)])
