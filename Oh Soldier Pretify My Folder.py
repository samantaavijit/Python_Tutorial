"""
 Oh soldier prettify my folder
 path, directory, file formats
 def soldier("C://","avi.txt","jpg")
"""
import os


def soldier(path, file, ext):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        fileList = f.read().split("\n")
    for file in files:
        if file not in fileList:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == ext:
            os.rename(file, f"{i}{ext}")
            i += 1


if __name__ == '__main__':
    soldier(r"C:\Users\Avijit Samanta\Desktop\New folder", r"C:\Users\Avijit Samanta\Desktop\New folder\avi.txt",
            ".png")
