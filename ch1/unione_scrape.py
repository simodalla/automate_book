from __future__ import print_function
import requests

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

req = requests.get('http://www.unionerenolavinosamoggia.bo.it/index.php/'
                   '495-organi-istituzionali/consiglio/317-il-consiglio'
                   '-dellunione')
# print(req)

soup_s = BeautifulSoup(req.content, "lxml")



first_hr = soup_s.select_one("article.item-page hr")
for element in first_hr.next_siblings:
    if element.find('br') and isinstance(element, Tag):
        for child in element.children:
            # print("** ", child, type(child), child.string)
            if not isinstance(child, Tag) and len(child.string.strip()) > 0:
                print(child.string)
        # print(element.find_all('p'))#[0].string)
        # print(element.getText())
        # print(element.select(':not(strong)'))

# for hr in soup_s.select_one("article.item-page hr"):
#
#     print(hr.previous_elements)
#     # print[repr(e) for e in hr.previous_elements]


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
        credential_dir, 'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url)

    spreadsheet_id = '1a_UjLtIlQ1aO66AMfoYm4jvtutxXoyoZX0Rim5h5U_o'
    # spreadsheet_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    range_name = 'Amministratori!A2:H'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        print(values)
        # for row in values:
        #     # Print columns A and E, which correspond to indices 0 and 4.
        #     print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()