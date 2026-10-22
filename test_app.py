
import unittest
from urllib.request import urlopen
import json


class TestDevOpsApp(unittest.TestCase):

    def test_health_endpoint(self):
        with urlopen("http://127.0.0.1:8000/health") as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read().decode())

        self.assertEqual(data["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
