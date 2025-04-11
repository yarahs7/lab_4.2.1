# from flaskr.backend import Backend

# from unittest.mock import MagicMock, Mock, patch

# import pytest


# @pytest.fixture
# def page_bucket(blob):
#     return make_bucket(blob)


# @pytest.fixture
# def login_bucket(blob):
#     return make_bucket(blob)


# @pytest.fixture
# def backend(page_bucket, login_bucket):
#     storage_client = MagicMock()
#     storage_client.bucket = Mock()
#     storage_client.bucket.side_effect = [page_bucket, login_bucket]
#     return Backend(storage_client=storage_client)


# # 1 Point
# def test_get_wiki_page_success(backend, page_bucket, file_stream):
#     file_stream.read.return_value = "test worked"

#     value = backend.get_wiki_page("test")

#     page_bucket.get_blob.assert_called_with("test")
#     assert value == "test worked"


# # 1 Point
# def test_get_wiki_page_failure(backend, page_bucket):
#     page_bucket.get_blob.return_value = None

#     value = backend.get_wiki_page("test")

#     assert value == "No page exists with this name"


# # 1 Point
# def test_get_all_pages(backend, page_bucket):
#     blobs = [MagicMock() for _ in range(5)]
#     blobs[0].name = "test0"
#     blobs[1].name = "test1.png"
#     blobs[2].name = "test2.jpg"
#     blobs[3].name = "test3"
#     blobs[4].name = "test4.jpeg"
#     page_bucket.list_blobs.return_value = iter(blobs)

#     value = [name for name in backend.get_all_page_names()]

#     page_bucket.list_blobs.assert_called_with()
#     assert value == ["test0", "test3"]


# # 1 Point
# def test_upload_success(backend, page_bucket, blob, file_stream):
#     page_bucket.get_blob.return_value = None

#     backend.upload("test", "test data")

#     page_bucket.blob.assert_called_with("test")
#     blob.open.assert_called_with("wb")
#     file_stream.write.assert_called_with("test data")


# # 1 Point
# def test_upload_failure(backend, page_bucket):
#     try:
#         backend.upload("test", "test data")
#         assert False, "Upload succeeded despite existing blob"
#     except ValueError as v:
#         assert str(v) == "test already exists!"

#     page_bucket.get_blob.assert_called_with("test")


# # 1 Point
# def test_get_image_success(backend, page_bucket, blob, file_stream):
#     file_stream.read.return_value = "test data".encode()

#     value = backend.get_image("test")

#     page_bucket.get_blob.assert_called_with("test")
#     blob.open.assert_called_with("rb")
#     assert value.read() == "test data".encode()


# # 1 Point
# def test_get_image_failure(backend, page_bucket):
#     page_bucket.get_blob.return_value = None

#     value = backend.get_image("test")

#     assert value.read() == "".encode()


# # 1 Point
# @patch('flaskr.backend.sha256', return_value=sha256("test hash"))
# def test_sign_up_success(hash, backend, login_bucket, blob, file_stream):
#     login_bucket.get_blob.return_value = None

#     value = backend.sign_up("test_user", "password")

#     login_bucket.blob.assert_called_with("test_user")
#     blob.open.assert_called_with("w")
#     hash.assert_called_with("password".encode())
#     file_stream.write.assert_called_with("test hash")

#     assert value.name == "test_user"


# # 1 Point
# def test_sign_up_failure(backend, login_bucket, blob, file_stream):
#     try:
#         backend.sign_up("test_user", "password")
#         assert False, "Sign up succeeded despite existing user"
#     except ValueError as v:
#         assert str(v) == "test_user already exists!"

#     login_bucket.get_blob.assert_called_with("test_user")


# # 1 Point
# @patch('flaskr.backend.sha256', return_value=sha256("test hash"))
# def test_sign_in_success(sha, backend, login_bucket, blob, file_stream):
#     file_stream.read.return_value = "test hash"

#     value = backend.sign_in("test_user", "password")

#     login_bucket.get_blob.assert_called_with("test_user")
#     blob.open.assert_called_with()
#     sha.assert_called_with("password".encode())

#     assert value.name == "test_user"


# # 1 Point
# def test_sign_in_no_user(backend, login_bucket, blob, file_stream):
#     login_bucket.get_blob.return_value = None

#     try:
#         backend.sign_in("test_user", "password")
#         assert False, "Sign in succeeded despite no user"
#     except ValueError as v:
#         assert str(v) == "test_user does not exist!"

#     login_bucket.get_blob.assert_called_with("test_user")


# # 1 Point
# @patch('flaskr.backend.sha256', return_value=sha256("bad hash"))
# def test_sign_in_bad_password(sha, backend, login_bucket, blob, file_stream):
#     file_stream.read.return_value = "test hash"

#     try:
#         backend.sign_in("test_user", "bad password")
#         assert False, "Sign in succeeded despite bad password"
#     except ValueError as v:
#         assert str(v) == "Invalid password for test_user."

#     login_bucket.get_blob.assert_called_with("test_user")
#     blob.open.assert_called_with()
#     sha.assert_called_with("bad password".encode())
