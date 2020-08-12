"""
This module is a basic script that searches for a simple summary
of anything using Wikimedia's REST API. It's a basic interface
search tool written in Python 3.6.

When the program is executed, it will run the 'main' function
which handldes the entire module.

The use of Wikimedia REST API is solely for personal / education purposes, and
I agree to Wikimedia's general Term's of Use and Private policy.
"""

# Creator Josue Lopez
# Mon Jul 16 2018 11:50 PM
# Python 3.6

import urllib.request
import urllib.parse
import urllib.error
import json


def main():
    """ Main function that runs the CLI app """
    title = input("Search for a famous name on wikipedia with underscore as spaces (e.j. Barrack_Obama): ")
    status = None
    try:
        print('...')
        wiki_summary_uri = "https://en.wikipedia.org/api/rest_v1/page/summary/"
        url = urllib.request.urlopen(wiki_summary_uri+title)
        status = True
    except urllib.error.HTTPError:
        print("\nSorry, an error occurred. Our wiki_extract module believes \
            this search does not exist in Wikimedia's database.\n")
    else:
        response = url.read().decode(encoding='utf-8')

        json_data = json.loads(response)

        print('\n' + json_data['displaytitle'] + '\n')
        data = json_data['extract'].encode('ascii', 'ignore').decode('ascii')
        print(data + '\n')
    finally:
        if status is True:
            print("Success.")
        else:
            print('Try Again.')
        print("Done.")

if __name__ == '__main__':
    main()
