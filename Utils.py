import os

def list_file(path):
    files = os.listdir(path)
    print(files)
    return files
def hello():
    print('Hello!')
    return None
if __name__=='__main__':
    None