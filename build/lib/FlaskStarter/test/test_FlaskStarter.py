import unittest
from FlaskStarter import create_flask_project
from deleter import delete_folder_contents
import os


class TestFlaskStarter(unittest.TestCase):
    # Test if the Flask project is created
    def test_create_flask_project(self):
        create_flask_project(root_dir='./run_test', execute_batch=False)
        self.assertTrue(os.path.exists('./run_test/templates'))
        self.assertTrue(os.path.exists('./run_test/static'))
        self.assertTrue(os.path.exists('./run_test/.venv'))
        self.assertTrue(os.path.exists('./run_test/.gitignore'))
        self.assertTrue(os.path.exists('./run_test/app.py'))

    # Test if the Flask project is deleted
    def test_delete_folder_contents(self):
        delete_folder_contents('./run_test')
        self.assertFalse(os.path.exists('./run_test/templates'))
        self.assertFalse(os.path.exists('./run_test/static'))
        self.assertFalse(os.path.exists('./run_test/.venv'))
        self.assertFalse(os.path.exists('./run_test/.gitignore'))
        self.assertFalse(os.path.exists('./run_test/app.py'))

        # Delete the run_test folder
        os.rmdir('./run_test')


if __name__ == '__main__':
    unittest.main()
