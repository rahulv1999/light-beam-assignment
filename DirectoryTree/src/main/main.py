from folder import Folder
from config import Config
import os

root = Config("root")
root.add("root", "f1")
root.add("root", "f2")
root.add("root", "f3")
root.add("root/f2", "f21")
root.add("root/f2", "f22")
root.print()
root.remove("f2")
root.add("root/f7/f1", "f2")
root.print()
    

    

    


