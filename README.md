# Django QuickPoll Application

## Features

 * Manage poll, questions and choices
 * Manage rules between questions (display the question C and D if the choice B
   to the question A is selected)
 * Works on non-django frontend

## Demo

A demo is available [here](http://django-sandbox.geelweb.org/quickpoll-app)

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

Add attributes to the `script` tag to customize the layout:

 * data-layout: type of layout, "ribbon", "button" or "none". Default to "ribbon"
 * data-container: css selector to defines the elements where append the ribbon. Append to `body` by
   default. All jquery compliant selectors are availables.
 * data-label: the text to display. Default to "Survey"

If data-layout is defined to "none" you have to add the link to open the
quickpoll window yourself. ex:

    <a class="btn-quickpoll open-poll" href="#">Survey</a>

## Todo

 * Improve admin
 * Display poll results when the poll has been posted
 * Remember a user has already voted
