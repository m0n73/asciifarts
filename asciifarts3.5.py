#!/usr/bin/env python3

import time
import sys
import json
import requests
import re
import html
from requests.exceptions import HTTPError

def get_random_ascii():
    """This function raises an HTTPError if it gets a 4** or 5**.
    If you're adding this to your bot, don't forget to catch it.
    """
    response = requests.get("http://www.asciiartfarts.com/random.cgi")
    response.raise_for_status()
    rawscii = response.text.split('<pre>')[2].split('</pre>')[0]
    return html.unescape(rawscii)

if __name__ == "__main__":
    timestr = time.strftime("[%b %d %Y] %H:%M:%S")
    try:
        print("{}".format(get_random_ascii()))
    except HTTPError as err:
        sys.exit("{0} [ERROR] HTTP: {1}".format(timestr, err))
    except Exception as err:
        sys.exit("{0} [ERROR] GEN: {1}".format(timestr, err))


