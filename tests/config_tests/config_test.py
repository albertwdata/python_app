import unittest
from config import config as cfg


class ConfigTestCase(unittest.TestCase):

    def test_config(self):

        config_hello_str = cfg.config['hello']['hello_str']

        self.assertEqual(config_hello_str, 'Hello from config.toml!')


if __name__ == '__main__':
    unittest.main()
