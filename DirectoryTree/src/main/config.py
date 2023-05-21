import os
import folder

class Config:
    
    def __init__(self, name):
        self.root = folder.Folder(name, 0)
        self.__id = 1

    def print(self):
        print(self.root)

    def add(self, parentPath, name):
        parentName = parentPath.split(os.sep)[-1]
        parent = self.__getCheckByName(parentName)
        subFolder = folder.Folder(name, self.__id, parent)
        #duplicacy check
        if self.fetch(subFolder.name) is not None:
            raise Exception(f"sub folder with name {subFolder.name} exists")
        parent.addSubFolder(subFolder)
        self.__id += 1 
        return parent

    def remove(self, name):
        subFolder = self.__getCheckByName(name)
        parent = subFolder.parent
        self.__removeHelper(subFolder)
        parent.removeSubFolder(subFolder.id)

    def update(self, id, name):
        subFolder = self.__getCheck(id)  
        #check duplicacy
        _, folder = self.__getByNameHelper(self.root, name, "")

        if folder is None and name != subFolder.name:
            raise Exception(f"folder with name {name} exists")
       
        subFolder.name = name 
        return subFolder

    def fetch(self, name):
        path, _ = self.__getByNameHelper(self.root, name, "")
        return path

        
    def __getCheck(self, id):
        subFolder = self.__fetch(id)
        if subFolder is None:
            raise Exception(f"folder with id {id} not found")
        return subFolder

    def __getCheckByName(self, name):
        _, subFolder = self.__getByNameHelper(self.root, name, "")
        if subFolder is None:
            raise Exception(f"folder with name {name} not found")
        return subFolder

    def __getByIdHelper(self, subFolder, id, s):
        if subFolder.id == id :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders:
            return self.__getByIdHelper(sf, id, os.path.join(s, subFolder.name))

        return None,None

    def __getByNameHelper(self, subFolder, name, s):
        if subFolder.name == name :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders:
            return self.__getByIdHelper(sf, name, os.path.join(s, subFolder.name))

        return None,None

    def __fetch(self, id):
        s = self.root.name
        _, folder = self.__getByIdHelper(self.root, id, s)
        return folder

    def __removeHelper(self, folder):
        if len(folder.subFolder) == 0:
            return 
        for child in folder.subFolders:
            self.__removeHelper(child)
            folder.removeSubFolder(child.id) 

        

    


