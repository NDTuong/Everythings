import os
path = input("Enter path: ")
# path = "F:\\Downloads\\Dowload\\wallpaper"
for a, b, fileName in os.walk(path):
    for i in range(len(fileName)):
        os.rename(path + "\\" + fileName[i], path + "\\" + str(i+1) + ".jpg")