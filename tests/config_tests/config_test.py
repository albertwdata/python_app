import unittest
from config import config as cfg


class ConfigTestCase(unittest.TestCase):

    def test_config(self):

        config_hello_str = cfg.config['hello']['hello_str']

        self.assertEqual(config_hello_str, 'Hello from config.toml!')


    def test_config_cotains_logging_info(self):

        config_keys = cfg.config.keys()

        self.assertIn('logging', config_keys)


if __name__ == '__main__':
    unittest.main()
