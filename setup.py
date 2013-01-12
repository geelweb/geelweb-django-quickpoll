#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
django quickpoll setup script
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"
__version__ = "0.1"

import sys
from setuptools import setup, find_packages

author_data = __author__.split(" ")
maintainer = " ".join(author_data[0:-1])
maintainer_email = author_data[-1]
long_desc = open('README.md').read()

if __name__ == "__main__":
    setup(
        name="django quickpoll app",
        version=__version__,
        description="A django app to manage polls",
        long_description=long_desc,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url="https://github.com/geelweb/geelweb-django-quickpoll",
        download_url="https://github.com/geelweb/geelweb-django-contactform/archive/quickpoll_%s.zip" % __version__,
        license='MIT',
        namespace_packages = ['geelweb', 'geelweb.django'],
        packages=find_packages('src'),
        package_dir = {'':'src'},
        package_data = {
            'geelweb.django.quickpoll': [
                'templates/quickpoll/*.html',
                'static/quickpoll/js/*.js',
                'static/quickpoll/js/lib/collection/*.js',
                'static/quickpoll/js/lib/model/*.js',
                'static/quickpoll/js/lib/view/*.js',
                'static/quickpoll/js/lib/vendor/*.js',
                'static/quickpoll/css/*.css',
                ],
        },
        install_requires=['djangorestframework'],
        )

