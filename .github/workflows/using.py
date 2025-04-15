def getCode(file1):
    C = file1.url
    code = C.data
    return code 
    return C

def load_file(file_text, file_path=None):
    file_data = {"CODE": file_text, "PATH": file_path}
    lf = open(file_data)
    return lf

def lookforcommit():
    URL = https://github.com/Chess-For-All/COAIT/commit
    Pth = URL.data.path
    LFP = load_file(requests.get(https://github.com/Chess-For-All/COAIT/commit), Pth)
    return LFP.PATH 

def getFile(file):
    getCode(file)
    load_file(requests.get(C), file)

def using(FILE):
    getFile(FILE)
    YAML = {
      "name": "coding",
      "jobs": 
        "Work":
          "push": lf, "version": 1.0.0
    }
    return YAML

using(lookforcommit())
