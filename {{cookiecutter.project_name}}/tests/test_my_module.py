from unittest import TestCase
from {{cookiecutter.pkg_name}} import my_module


class TestMyModule(TestCase):
    def test_run(self):
        self.assertEqual("hello world", my_module.run())
