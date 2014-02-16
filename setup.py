from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['tornado',
            'CherryPy', # If you want serve Tornado through CherryPy
           ]

setup(name='YourAppName', version='1.0',
      description='OpenShift Python-3.3 / Tornado Web Server based application',
      author='Your Name', author_email='admin@example.org',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
     )
