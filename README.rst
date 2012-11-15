django-cookie-message
=====================

A simple middleware that uses the django messages framework to add a notification regarding the EU cookie directive.

If it can't detect a cookie about cookies, sets it and displays a message.


Installation
------------

Install from pypi. ::

    pip install django-cookie-message

In your settings: ::

* Ensure the django messages framework is installed.
* Add ``'cookie_message'`` to ``INSTALLED_APPS``.
* Add ``'cookie_message.middleware.CookieMessageMiddleware'`` to ``MIDDLEWARE_CLASSES``.

Configuration
-------------

**The message** can be changed by overriding the ``cookies/message.py`` template.

**The cookie** can be changed by defining ``COOKIE_MESSAGE_KWARGS`` in your
``settings.py``. The default is: ::

    COOKIE_MESSAGE_KWARGS = {
        'key': 'cookie_message',
        'value': '',
        'max_age': 365 * 24 * 60 * 60, # One year.
        'expires': None,
        'path': '/',
        'domain': None,
        'secure': None,
        'httponly': False,
    }

These are the arguments sent to `set_cookie() <https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.set_cookie>`_.
