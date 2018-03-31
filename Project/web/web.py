from bottle import abort, default_app

from .manager import WebInterfaceManager

site = default_app()
manager = WebInterfaceManager()


# @site.hook("after_request")
# def
@site.route("/")
def index():
    abort(503)
