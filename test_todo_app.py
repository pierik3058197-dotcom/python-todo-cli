import tempfile
import unittest
from pathlib import Path

from todo_app import add_todo, complete_todo, delete_todo, load_todos, renumber_todos


class TodoAppTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "todos.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_todo(self):
        todo = add_todo("学习 Python", self.file_path)
        self.assertEqual(todo["id"], 1)
        self.assertEqual(load_todos(self.file_path)[0]["title"], "学习 Python")

    def test_complete_todo(self):
        add_todo("写测试", self.file_path)
        self.assertTrue(complete_todo(1, self.file_path))
        self.assertTrue(load_todos(self.file_path)[0]["completed"])

    def test_delete_todo(self):
        add_todo("删除我", self.file_path)
        self.assertTrue(delete_todo(1, self.file_path))
        self.assertEqual(load_todos(self.file_path), [])

    def test_renumber_todos(self):
        add_todo("第一项", self.file_path)
        add_todo("第二项", self.file_path)
        delete_todo(1, self.file_path)
        todos = renumber_todos(self.file_path)
        self.assertEqual(todos[0]["id"], 1)
        self.assertEqual(todos[0]["title"], "第二项")


if __name__ == "__main__":
    unittest.main()
