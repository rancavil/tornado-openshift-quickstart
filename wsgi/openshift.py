#!/usr/bin/env python

import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('index.html')

# Put here yours handlers.

handlers = [(r'/',MainHandler),]
