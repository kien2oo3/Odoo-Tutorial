from werkzeug.utils import redirect

from odoo import http
from odoo.http import request
import json


class MyController(http.Controller):
    @http.route("/hello", auth="user", type="http")
    def say_hello(self):
        return "Hello Odoo"

    @http.route("/hello/<name>", auth="user", type="http")
    def say_hello_name(self, name):
        age = request.params.get("age")
        return f"Hello {name}, your age is {age or '...'}"

    @http.route("/info", auth="user", type="http")
    def say_hello_name(self):
        return json.dumps([
            {
                'name': 'An',
                'age': 21,
                'gender': 'male'
            },
            {
                'name': 'Chi',
                'age': 22,
                'gender': 'female'
            }
        ])

    @http.route("/google", auth="user", type="http")
    def access_google(self):
        return redirect("https://google.com")

    @http.route("/login", auth="user", type="http")
    def login(self):
        return request.render("web.login")
