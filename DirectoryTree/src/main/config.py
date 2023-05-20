import os

class Config:
    
    def __init__(self, root):
        self.root = root
        self.id = 1

    def print(self):
        pass

    def add(self, parentPath, subFolder):
        parentName = parentPath.split(os.sep)[-1]
        parent = self.fetch(parentName)
        #duplicacy check
        if self.fetch(subFolder.name) is not None:
            raise Exception(f"sub folder with name {subFolder.name} exists")
        parent.addSubFolder(subFolder)
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
            raise Exception(f"sub folder with name {name} exists")
       
        subFolder.name = name 
        return subFolder

    def fetch(self, name):
        path, _ = self.__getByNameHelper(self.root, name, "")
        return path
        
    def __getCheck(self, id):
        subFolder = self.__fetch(id)
        if subFolder is None:
            raise Exception(f"sub folder with id {id} not found")
        return subFolder

    def __getCheckByName(self, name):
        _, subFolder = self.__getByNameHelper(self.root, name, "")
        if subFolder is None:
            raise Exception(f"sub folder with name {name} not found")
        return subFolder

    def __getByIdHelper(self, subFolder, id, s):
        if subFolder.id == id :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders:
            return self.__getByIdHelper(sf, id, os.path.join(s, subFolder.name))

        return None

    def __getByNameHelper(self, subFolder, name, s):
        if subFolder.name == name :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders:
            return self.__getByIdHelper(sf, name, os.path.join(s, subFolder.name))

        return None

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

        

    


