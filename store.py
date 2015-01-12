#! /usr/bin/env python
# encoding: UTF-8

from __future__ import print_function

"""
Rather simple processing: just take the email address from the form, append it
to a text file and redirect the user to a confirmation / error page. It would
be nice to do something more elaborate, but I don't think the effort is worth
it for a coming-soon website.
"""

import cgi
import time

EMAILS_FILE = 'emails.txt'
OK_URL = './exito.html'
ERROR_URL = './error.html'

def store_address():
    """ Store email address, return False if the field was left empty. """

    form = cgi.FieldStorage()
    address = form.getvalue('email-address')
    if not address:
        return False
    else:
        address = address.strip()
        if not address:
            return False
        with open(EMAILS_FILE, 'at') as fd:
            fd.write("{0} | {1}\n".format(time.ctime(), address))
        return True

def redirect(url):
    """ Redirect the user to the specified URL. """

    html = """Content-type: text/html

<html>
  <head>
     <meta http-equiv="refresh" content="0;url={0}" />
     <title>Redirigiendo...</title>
  </head>

  <body>
     Redirigiendo...
     <a href="{0}">Haz click aqui si no eres redirigido automaticamente</a>
  </body>
</html>

    """

    print(html.format(url))

if __name__ == "__main__":
    if store_address():
        redirect(OK_URL)
    else:
        redirect(ERROR_URL)
