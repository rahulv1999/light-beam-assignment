import sys
sys.path.append("../")
sys.path.append("../../")
from src.main import config

root = config.Config("root")
root.add("root", "f1")
root.add("root", "f2")
root.add("root", "f3")
root.add("root/f2", "f21")
root.add("root/f2", "f22")
root.print()
print("************************")
print(root.fetch("f21"))
root.update("f21", "f221")
root.print()
print("************************")
root.remove("f2")
root.print()
print("************************")

    

    

    


