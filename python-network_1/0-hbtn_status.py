#!/usr/bin/python3
"""Script that fetches a status URL"""

import urllib.request
import sys

if __name__ == "__main__":
    # Use command line argument if provided, otherwise use default
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://alx-intranet.hbtn.io/status"
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
