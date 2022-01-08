import os
folder_path = r'E:\\Python'
def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('file name:' + fileName)
        print('folder path:' + os.path.abspath(os.path.join(dir, fileName)), sep="\n")
if __name__ == '__main__':
    listDir(folder_path)
