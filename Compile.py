
from cx_Freeze import setup, Executable

setup(
    name='Panload',
    version='1.5',
    description='Download coub videos',
    executables=[Executable('Panload.py')]
)
