# Creator Josue Lopez

import urllib.request
import urllib.parse
import urllib.error
import json

"""
This script / module is a basic script that makes use of wikipedia's public API.
cquires the information of anything that is searched
using the initial command prompt. This module returns a summary of whatever
was searched using wikipedia.
"""

"""
The use of Wikimedia REST API is solely for personal / education purposes, and
I agree to Wikimedia's general Term's of Use and Private policy.
"""

def main():
    title = input("Search for something on wikipedia: ")

    try:
        url = urllib.request.urlopen("https://en.wikipedia.org/api/rest_v1/page/summary/"+title)
    except urllib.error.HTTPError:
        print('\nSorry. Our wiki_extract module believe this search does not exist.\n')
    else:
        response = url.read().decode(encoding ='utf-8')

        json_data = json.loads(response)

        print('\n' + json_data['displaytitle'] + '\n')
        print(json_data['extract'].encode('ascii', 'ignore').decode('ascii') + '\n')

if __name__ == '__main__':
    main()
