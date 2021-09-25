import os

print("Write file:")
a = input()
os.system("pyinstaller --onefile " + a + ".py")
os.system("del /q build")
os.system("del /q __pycache__")
os.system("mkdir source")
os.system("move " + a + " source\\")
os.system("del /q " + a + ".spec")
