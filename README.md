Tornado Web Server and Python 3 on Openshift
============================================

This git repository helps you get up and run quickly Tornado Web Server on Openshift. 

Running on Openshift
--------------------

Create an account at http://openshift.redhat.com/

Install the RHC client tools if you have not already done so:

     sudo gem install rhc

Create a python-3.3 application

     rhc app create tornadopy3 python-3.3

Add this upstream repo

     cd tornadopy3
     git remote add upstream -m master git://github.com/rancavil/tornado-openshift-quickstart.git
     git pull -s recursive -X theirs upstream master

Then push the repo upstream

     git push

That's it. You can now checkout your application at:

     http://tornadopy3-$youtnamespace.rhcloud.com

The structure of directories created are:

     tornadopy3/
          wsgi.py
          .gitignore
          README.md
          setup.py
          requirements.txt
          data/
          libs/
          .openshift/
               action_hooks/
               cron/
               markers/
          wsgi/
               application
               openshift.py
               static/
               templates/
                    index.html

The main file is openshift.py, this contains the definitions of the handlers. You can change it the name, but you must be sure to change the import statement in application file.

     import tornado.web
     import os

     class MainHandler(tornado.web.RequestHandler):
          def get(self):
               self.render('index.html')

     # Put here yours handlers.

     handlers = [(r'/',MainHandler),]

Openshift uses WSGI to deploy the python applications. In the application file we will define.

     application = tornado.wsgi.WSGIApplication(handlers, **settings)

application will be invoked by app.py to run the application on wsgi. If CherryPy is not installed will be used wsgiref.
