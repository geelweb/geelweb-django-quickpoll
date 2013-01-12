# Django QuickPoll Application

## Features

 * Manage poll, questions and choices
 * Manage rules between questions (display the question C and D if the choice B
   to the question A is selected)
 * Works on non-django frontend

## Installation

From source:

    python setup.py build
    python setup.py install

## Dependences

 * [Django REST framework](http://django-rest-framework.org/)


## Configuration

### settings.py

Edit your settings.py file and add the following line into your INSTALLED_APPS

    'geelweb.django.quickpoll'

### urls.py

Edit your urls.py and add the following line

    url(r'^quickpoll/', include('geelweb.django.quickpoll.urls')),


### Database

Sync the database (you need to configure it in your settings)

    python manage.py syncdb

### Static files

Do not forget to collect the statics (depends of your settings)

    python manage.py collectstatic

## Backend

Enable the django admin and go to /admin/quickpoll/ to start creating polls

## Frontend

Add the following code to your templates to display the poll ribbon.

    <link href="{{ STATIC_URL }}quickpoll/css/main.css" rel="stylesheet" media="screen" />
    <script data-main="{{ STATIC_URL }}quickpoll/js/main.js" src="{{ STATIC_URL }}quickpoll/js/lib/vendor/require.js"></script>

## Todo

 * Improve admin
 * Display poll results when the poll has been posted
 * Remember a user has already voted
