"""Facade that simplifies interacting with Backend data.

Contains methods useful for a wiki implementation. One can replace an
instance of this object with another to change the backend. Eg. one
can create a sql version of this backend if they so choose.

Example Usage:

backend = Backend()
page_content=backend.get_wiki_page("test")

"""
from io import BytesIO

import os


class Backend:
    """Backend provides access to page data for wikis.

    Attributes:
        pages: A dictionary mapping page name to the filename for wiki entries.
        img_filenames: The list containing filenames for images.
    """

    def __init__(self):
        """
        Args:
            storage_client: By default this is Google's Storage Client.
        """
        self.pages = {f.split('.')[0]: f for f in os.listdir("flaskr/static/data/")}
        self.images = {f.split('.')[0]:f for f in os.listdir("flaskr/static/img/")}

    def get_wiki_page(self, name):
        """ Returns the content (string) for a page if it exists.

        If a page does not exist, returns a string with an error message instead.

        Args:
            name: The key for a page stored in the page_bucket.
        """
        if name not in self.pages:
            return "No page exists with this name"
        filepath = "flaskr/static/data/" + self.pages[name]
        with open(filepath, 'r') as file:
            return file.read()

    def get_all_page_names(self):
        """Returns an iterator for all of the pages."""
        return self.pages.keys()

    def get_image(self, name):
        """ Returns an image if it exists.

        Args:
            name: The name of the image (including '.).
        """
        if name not in self.images:
            return BytesIO()
        filepath = "flaskr/static/img/" + self.images[name]
        with open(filepath, 'rb') as f:
            output = f.read()
            return BytesIO(output)
