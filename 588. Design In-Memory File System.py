from typing import List, Optional

class Trie():
    def __init__(self):
        # key is name of directory and value is children inside dir
        self.children = {}
        self.isFile = False
        # Name only if it is a file
        self.name = None
        self.content = []
    
    def search(self, path, root):
        # path is /a/b/c

        node = root
        if path == "/":
            return node
        

        path_comp = path.split('/')[1:]
        for comp in path_comp:
            if comp not in node.children:
                return None
            node = node.children[comp]
        return node
    
    def insert(self, path, root, isFile):
        node = root

        path_comp = path.split('/')[1:]
        for comp in path_comp:
            if comp not in node.children:
                node.children[comp] = Trie()
            node = node.children[comp]
        
        if isFile:
            node.isFile = True
            node.name = path_comp[-1]
        
        return node

class FileSystem:
    """
    In-memory file system implementation using a Trie data structure.
    """

    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]:
        node = self.root.search(path, self.root)
        if not node:
            return []
        
        if node.isFile:
            return [node.name]

        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, self.root, isFile=False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath, self.root, isFile=True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath, self.root)
        return ''.join(node.content)


# Your FileSystem object will be instantiated and called as such:
path = '/a/b/c'
filePath = '/a/b/c/d'
content = 'Hi this is to create d file'
obj = FileSystem()
param_1 = obj.ls(path)
obj.mkdir(path)
obj.addContentToFile(filePath, content)
param_4 = obj.readContentFromFile(filePath)
print(param_1)
print(param_4)
print(obj.ls('/a'))
obj.mkdir('/a/b/d')
print(obj.ls('/a/b'))
