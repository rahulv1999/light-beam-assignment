import sys 
sys.path.append("../")
sys.path.append("../../")
import unittest
from  src.main.config import Config

class ConfigTest(unittest.TestCase):
    def test_config_init(self):
        name = "root"
        tree = Config(name)
        self.assertEqual(name, tree.root.name)
        self.assertEqual(0, tree.root.id)
    
    def test_config_add(self):
        name = "root"
        subFolderName = "f1"
        tree = Config(name)
        tree.add(name, subFolderName)
        subFolder = tree.root.subFolders[0]
        self.assertEqual(1, len(tree.root.subFolders))
        self.assertEqual(subFolderName, subFolder.name)
        self.assertEqual(1, subFolder.id)

    def test_config_add_depth_2(self):
        name = "root"
        subFolderName = "f11"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", subFolderName)
        subFolder = tree.root.subFolders[0].subFolders[0]
        self.assertEqual(1, len(tree.root.subFolders[0].subFolders))
        self.assertEqual(subFolderName, subFolder.name)
        self.assertEqual(2, subFolder.id)

    def test_config_remove(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        tree.remove("f1")
        self.assertEqual(0, len(tree.root.subFolders))
    
    def test_config_remove_folder_not_exists(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        try:
            tree.remove("f13")
        except Exception as e:
            self.assertEqual("folder with name f13 not found", e.args[0])

    def test_config_remove_depth_2(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        tree.remove("f11")
        self.assertEqual(0, len(tree.root.subFolders[0].subFolders))

    def test_config_remove_folder_not_exist_error(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        try:
            tree.remove("f12")
            self.fail("test should have failed")
        except Exception as e:
            self.assertEqual("folder with name f12 not found", e.args[0])

    def test_config_fetch(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        self.assertEqual("root/f1/f11", tree.fetch("f11"))
    
    def test_config_fetch_invalid_folder(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        self.assertIsNone(tree.fetch("f12"))

    def test_update_name(self):
        name = "root"
        tree = Config(name)
        tree.add(name, "f1")
        tree.add("root/f1", "f11")
        tree.update("f11", "f111")
        self.assertIsNone(tree.fetch("f11"))
        self.assertEquals("root/f1/f111",tree.fetch("f111"))


if __name__ == '__main__':
    unittest.main()