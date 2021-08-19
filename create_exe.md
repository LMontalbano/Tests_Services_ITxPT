# How to create an .exe?
You just have to use the PyInstaller library.

Make sure you are in the directory where you want to install the .exe and enter the following command in a terminal:

``$ pyinstaller --onefile ../IHM/main.py``

- The ``--onefile`` option allows all of them to be grouped into a single .exe file
- The ``../IHM/main.py`` argument is the path of your main.py file to transform into .exe

You can also rename your *main.py* to *main.pyw* so that you don't have a terminal that opens when launching the .exe
