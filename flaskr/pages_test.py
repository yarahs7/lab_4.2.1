from flaskr import create_app, backend

from io import BytesIO
import pytest
from unittest.mock import patch


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_page(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Welcome to the Wiki!\n" in resp.data


def test_about_page(client):
    resp = client.get("/about")
    assert resp.status_code == 200
    assert b"About This Wiki\n" in resp.data


def test_all_pages(client):
    with patch("flaskr.backend.Backend.get_all_page_names",
               return_value=["test.txt", "info.txt"]):
        resp = client.get("/pages")
        assert resp.status_code == 200
        assert b"Wiki Pages\n" in resp.data


@patch("flaskr.backend.Backend.get_wiki_page", return_value=b"Some info.")
def test_get_page(mock_get_wiki_page, client):
    name = "myimportantinfo"
    resp = client.get("/pages/myimportantinfo")
    assert resp.status_code == 200
    assert b"myimportantinfo" in resp.data
    assert b"Some info." in resp.data
    mock_get_wiki_page.assert_called_once_with(name)


@patch("flaskr.backend.Backend.get_image", return_value=BytesIO())
def test_get_image(mock_get_image, client):
    image_name = "my-image"
    resp = client.get("/images/my-image")
    assert resp.status_code == 200
    mock_get_image.assert_called_once_with(image_name)
