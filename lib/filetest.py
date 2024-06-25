import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = ROOT_PATH + "\\ writetest.txt"

print("Root Path:",ROOT_PATH)


print("File Path:",FILE_PATH)

file = open(FILE_PATH,"w")
file.write("Test Write")
file.close()





