import os
import unittest
import json

from flaskr import create_app
from models import setup_db, Book


class BookTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "student", "student", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_book = {"title": "Anansi", "author": "NGaiman", "rating": 9}
        self.search = {'title': 'Anansi'}

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_paginated_books(self):
        res = self.client().get("/books")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_books"])
        self.assertTrue(len(data["books"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/books/page/1000", json={"rating": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "ressource Not found")

    # update book test
    def test_update_book_rating(self):
        res = self.client().patch("/books/18", json={"rating": 1})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 18).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(book.format()["rating"], 1)
        
    # search_book_test  
    def test_search_book(self):
        res = self.client().post('/books/search', json=self.search)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["books"]))
        self.assertTrue(data["count"])

    def test_400_for_failed_update(self):
        res = self.client().patch("/books/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad request")
        
    # create book test
    def test_create_new_book(self):
        res = self.client().post("/books", json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["books"]))

    # def test_405_if_book_creation_not_allowed(self):
    #     res = self.client().post("/books/45", json=self.new_book)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "method not allowed")
        
    # Delete a different book in each attempt
    def test_delete_book(self):
        res = self.client().delete("/books/16")
        data = json.loads(res.data)

        book = Book.query.filter(Book.id == 16).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 16)
        self.assertTrue(data["total_books"])
        self.assertTrue(len(data["books"]))
        self.assertEqual(book, None)

    def test_422_if_book_does_not_exist(self):
        res = self.client().delete("/books/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()