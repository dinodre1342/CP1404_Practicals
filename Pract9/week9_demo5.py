import os

print(os.getcwd())

target = "/Users/yen/Google Drive/JCU_Others/codes_python"
os.chdir(target)
print(os.getcwd())
print(os.listdir(target))

#for filename, dirs, files in os.walk("."):
 #   print(files)