__author__ = 'Drew'

import logging
import webapp2
import sys
import os
import re
import jinja2

import hashlib
import MySQLdb

from pages import base_handler


class signout(base_handler.BaseHandler):

    def get(self, key):
        myDB = MySQLdb.connect(host="engr-cpanel-mysql.engr.illinois.edu", port=3306, db="akkowal2_survivor",
                               user="akkowal2_drew", passwd="cs411sp14")
        cur = myDB.cursor()
        cur.execute("""UPDATE User SET SessionKey=%s WHERE SessionKey=%s""", ('NULL', key))
        myDB.commit()
        self.response.delete_cookie('auth')
        self.redirect('/home')