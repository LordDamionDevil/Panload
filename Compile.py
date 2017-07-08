
from cx_Freeze import setup, Executable

setup (
    name = 'Panload',
    version = '1.1', description = 'Download the galaxy',
    executables = [ Executable ( 'Panload.py' ) ]
)
