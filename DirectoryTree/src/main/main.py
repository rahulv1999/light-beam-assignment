from folder import Folder
from config import Config


root = Config("root")
root.add("root", "f1")
root.add("root", "f2")
root.add("root", "f3")
root.add("f2", "f21")
root.add("f2", "f22")
root.print()
root.remove("f1")

    

    

    


