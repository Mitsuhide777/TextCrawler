import bs4
from bs4 import BeautifulSoup
import requests

ellis_url = 'http://morning.computer/'

for i in range(34, 31, -1):
    source_code = requests.get(ellis_url + 'page/' + str(i))
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    do_not_touch = []
    for entry in soup.findAll('div', {'class' : 'sharedaddy sd-sharing-enabled'}):
        do_not_touch.append(entry)
    for entry in soup.findAll('div', {'class' : 'center-block entry-content'}):
        for child in entry.children:
            if type(child) is not bs4.Tag:
                continue

            if (do_not_touch.__contains__(child)):
                continue

            content = child.text;
            if child.name == 'ul':
                content = ''
                for in_child in child.children:
                    if type(in_child) is not bs4.Tag:
                        continue

                    content += '- ' + in_child.text + '\n'

            if (child.name == 'blockquote'):
                content = '\"' + content + '\"'


            print(content)

    print('\n\n\n')