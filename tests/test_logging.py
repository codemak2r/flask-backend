import unittest
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from app import create_app 


class TestLogging(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        app = create_app("dev")
        app.config['TESTING'] = True
        self.app = app

    def test_console_log(self) -> None:
        self.app.logger.info("Hello Flask")
        self.app.logger.error("Error!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
