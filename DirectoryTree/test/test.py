import unittest
from  src.main.config import Config

class ConfigTest(unittest.TestCase):
    def test_config_init(self):
        root = Config("root")
        self.assertEquals(6,6)



if __name__ == '__main__':
    unittest.main()