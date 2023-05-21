import os
import folder

class Config:
    
    def __init__(self, name):
        self.root = folder.Folder(name, 0)
        self.__id = 1

    def print(self):
        self.__print(self.root, 0)

    def add(self, parentPath, name):
        print(parentPath)
        pathList = parentPath.split(os.sep)
        #for base case -> root folder
        if pathList[0] != self.root.name :
            raise Exception("invalid path")

        parent = self.__getFromPath(pathList, self.root, 0)
        if parent is None:
            raise Exception("invalid path")
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

    def update(self, folderName, name):
        subFolder = self.__getCheckByName(folderName)  
        #check duplicacy
        _, folder = self.__getByNameHelper(self.root, name, "")

        if folder is not None and folder.id != subFolder.id: #idempotency check -> when trying to change name with its own name
            raise Exception(f"folder with name {name} exists")
       
        subFolder.name = name 
        return subFolder

    def fetch(self, name):
        path, _ = self.__getByNameHelper(self.root, name, "")
        return path

    def __getCheckByName(self, name):
        _, subFolder = self.__getByNameHelper(self.root, name, "")
        if subFolder is None:
            raise Exception(f"folder with name {name} not found")
        return subFolder

    def __getByIdHelper(self, subFolder, id, s):
        if subFolder.id == id :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders: 
            path_temp, folder_temp = self.__getByIdHelper(sf, id, os.path.join(s, subFolder.name))
            if folder_temp is not None:
                return path_temp, folder_temp 


        return None,None

    def __getByNameHelper(self, subFolder, name, s):
        if subFolder.name == name :
            return os.path.join(s, subFolder.name), subFolder
        
        for sf in subFolder.subFolders:
            path_temp, folder_temp = self.__getByNameHelper(sf, name, os.path.join(s, subFolder.name))
            if folder_temp is not None:
                return path_temp, folder_temp 

        return None,None

    def __fetch(self, id):
        s = self.root.name
        _, folder = self.__getByIdHelper(self.root, id, s)
        return folder

    def __removeHelper(self, folder):
        if len(folder.subFolders) == 0:
            return 
        for child in folder.subFolders:
            self.__removeHelper(child)
            folder.removeSubFolder(child.id) 

    def __print(self, root, lvl):        
        print('\t'*lvl + root.name)
        for child in root.subFolders:
            self.__print(child, lvl+1)

    def __getFromPath(self, path, root, index):
        if index == len(path):
            return None
        
        if index == len(path) - 1:
            return root
        for child in root.subFolders:
            if child.name == path[index+1]:
                folder_temp = self.__getFromPath(path, child, index+1)
                if folder_temp is not None :
                    return folder_temp

        return None


        

    


