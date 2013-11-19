from counter.views import log_request
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.gzip import gzip_page
from lxml import etree

import re
import requests


@gzip_page
def process(request, parameters, template):
    """Processes a request that needs to be sent to Kiln."""
    # constructs the path to the Kiln server
    path = re.sub(r'^.*?' + settings.KILN_CONTEXT_PATH, '/', request.path)
    query_string = request.META.get('QUERY_STRING')
    query_string = '?' + query_string if query_string else ''
    url = settings.KILN_BASE_URL + path + query_string

    # sends the request to Kiln
    r = requests.get(url)
    response = r.text
    # creates a new XML tree from the response
    root = etree.fromstring(response)

    # element names that are expected in the response
    element_names = ['title', 'css', 'js', 'header', 'breadcrumbs', 'content']

    # parameters dictionary to be passed to the template
    params = {}

    # title of the page to log the request
    title = '*empty*'

    for element_name in element_names:
        params[element_name] = ''
        element = root.find(element_name)
        if len(element):
            for child in element:
                params[element_name] += etree.tostring(child)
        elif element.text:
            params[element_name] = element.text

        if element_name == 'title':
            title = element.text

    # logs the request
    log_request(request, title)

    return render_to_response(template, params,
                              context_instance=RequestContext(request))
