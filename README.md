django-kiln
===========

Django application to integrate with Kiln

To use, add kiln to INSTALLED_APPS and set the following variables in `settings.py`:
* `KILN_CONTEXT_PATH`: The context path of the requests to be processed by Kiln. For example, if set to `'k/'`, then all the requests that start with `'k/'` would be processed by Kiln.
* `KILN_BASE_URL`: Base URL of Kiln.

And add the url pattern to the project base `urls.py`:
* `url('^{path}'.format(path=settings.KILN_CONTEXT_PATH), include('kiln.urls'))`
