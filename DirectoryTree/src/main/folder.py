class Folder:
    def __init__(self, name, id = None, parent=None):
        self.id = id
        self.name = name
        self.subFolders = []
        self.parent = parent

    def addSubFolder(self, subFolder):
        self.subFolders.append(subFolder)
        return subFolder

    def removeSubFolder(self, id):
        for subFolder in self.subFolders:
            if subFolder.id == id:
                self.subFolders.remove(subFolder)
                return

        raise Exception(f"sub folder with id {id} not found")

    def getById(self, subFolderId):
        for subFolder in self.subFolders:
            if subFolder.id == subFolderId:
                return subFolder

        return None

    def isSubFolder(self, subFolderId):
        return not self.getById(subFolderId) is None
