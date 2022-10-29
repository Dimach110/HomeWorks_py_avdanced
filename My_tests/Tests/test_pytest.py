import pytest
from app import show_document_info, add_new_doc, check_document_existance, delete_doc, get_doc_shelf, \
    get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf
from unittest.mock import patch

class TestMyFunc():

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}

    def test_show_document_info(self):
        document = {"type": "passport", "number": "333444", "name": "name"}
        assert show_document_info(document) == ('passport', '333444', 'name')


    @patch("app.input", return_value="123")
    def test_add_new_doc(self, mock_input):
        assert add_new_doc() == "123"

    def test_check_document_existance(self):
        assert check_document_existance("10006") == True

    @patch("app.input", return_value="11-2")
    def test_delete_doc(self, mock_input):
        assert delete_doc() == ("11-2", True)

    @patch("app.input", return_value="10006")
    def test_get_doc_shelf(self, mock_input):
        assert get_doc_shelf() == "2"

    @patch("app.input", return_value="10006")
    def test_get_doc_owner_name(self, mock_input):
        assert get_doc_owner_name() == "Аристарх Павлов"





