""" All content related endpoints are created here.

Endpoints:
URI             | Method | Description
----------------|--------|-------------
/               | GET    | Returns the home page
/about          | GET    | Returns an about page
/images/<image> | GET    | Returns the image from backend.get_image
/pages          | GET    | Returns all of the pages in a list via backend.get_all_page_names
/pages/<page>   | GET    | Returns the page from backend.get_wiki_page
"""

from flask import render_template, send_file


def make_endpoints(app, backend):
    """Constructs the endpoints that display content for the wiki.

    Args:
        backend: An object allowing our wiki to interact with a database/store.
    """

    @app.route("/")
    def home():
        """Returns the home page."""
        return render_template("main.html",
                               page_name="Wiki Index",
                               page_content="Welcome to the Wiki!")

    @app.route("/about")
    def about():
        """Returns an about page."""
        return render_template("about.html")

    @app.route("/images/<image>")
    def images(image):
        """Returns the image from backend.get_image."""
        return send_file(backend.get_image(image), mimetype='image/jpeg')

    @app.route("/pages")
    def all_pages():
        """Returns all of the pages in a list via backend.get_all_page_names."""
        return render_template("pages.html",
                               page_name="Wiki Index",
                               all_pages=backend.get_all_page_names())

    @app.route("/pages/<name>")
    def pages(name):
        """Returns the page from backend.get_wiki_page"""
        return render_template("main.html",
                               page_name=name,
                               page_content=backend.get_wiki_page(name))
