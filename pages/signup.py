import logging
import webapp2
import sys
import os
import re
import jinja2

from pages import base_handler

class Sign(base_handler.BaseHandler):

    def get(self):
        questions = ["Name", "Age", "Major"]
        context = {'qList': questions}
        self.render("register.html", **context)

    def post(self):
        if (self.response is not None):
            self.redirect('/register')
        else:
            self.redirect('/home')


        #def post(self):
        #does nothing right now
        #would look like self.render("home.html", stuff we want to put on the page)