def load_file(a):
    f = open(a.path)
    file_data = {"PATH": a.path, "CODE": f}
    return file_data

def lookforcommit():
    load_file(requests.get(https://github.com/Chess-For-All/COAIT/commit))
    return file_data.CODE

def use(file):
    YAML = {
      "name": "using",
      "jobs":
        "Work":
          "push": file,
          "version": "1.0.0"
    }
    return YAML

use(lookforcommit())
