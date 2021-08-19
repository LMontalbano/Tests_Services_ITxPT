# How to create an .exe?
You just have to use the PyInstaller library.

Enter the following command in a terminal:

`` pyinstaller --onefile main.py``

- The ``--onefile`` option allows all of them to be grouped into a single .exe file
- The ``main.py`` argument is the name of your main.py file to transform into .exe

You can also rename your *main.py* to *main.pyw* so that you don't have a terminal that opens when launching the .exe