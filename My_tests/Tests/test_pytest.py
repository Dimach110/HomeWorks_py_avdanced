import unittest
from app import show_document_info, add_new_doc, check_document_existance, delete_doc
from unittest.mock import patch

class TestMyFunc(unittest.TestCase):

    def setUp(self) -> None:
        return print("Start")

    def test_show_document_info(self):
        document = {"type": "passport", "number": "333444", "name": "name"}
        result = show_document_info(document)
        etalon = ('passport', '333444', 'name')
        self.assertEqual(result, etalon)


    @patch("app.input", return_value="A")
    def test_add_new_doc(self, mock_input):
        res = add_new_doc()
        eq = "A"
        self.assertEqual(res, eq)

    def test_check_document_existance(self):
        res = check_document_existance("10006")
        self.assertTrue(res)

    @patch("app.input", return_value="11-2")
    def test_delete_doc(self, mock_input):
        res = delete_doc()
        self.assertTrue(res)


    def tearDown(self) -> None:
        return print("Stop")



        # class TestCache(unittest.TestCase):
        #     @patch("utils.sample.input", return_value='a')
        #     def test_take_input(self, mock_input):
        #         ans = take_input()
        #         self.assertEqual(ans, 'Correct')