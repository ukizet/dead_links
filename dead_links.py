import requests
import sys
from bs4 import BeautifulSoup

main_url = 'https://www.seoptimer.com/blog/broken-links/'

page = requests.get(main_url)

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    try:
        link_url = link.get('href')
        if link_url is None:
            print('link url is None')
            print('\n')
            continue
        if link_url == '':
            print('link url = \'\'')
            print('\n')
            continue
        if link_url[0] == '/':
            print('link_url:', link_url)
            full_link_url = main_url + link_url[1:]
            print('full_link_url:', full_link_url)
            print('\n')
        elif link_url[0] == '#':
            print('link_url:', link_url)
            full_link_url = main_url + link_url
            print('full_link_url:', full_link_url)
            print('\n')
        else: 
            print('link_url[0] != \'/\' or #')
            print('\n')
            full_link_url = link_url
        response = requests.get(full_link_url)

        if response.status_code == 404:
            print('Link is not working:', full_link_url)
        else:
            print('Link is working:', full_link_url)
    except NameError:
        # print('')
        # print('\n')
        print('\nNot link:', link_url)
    except IndexError:
        print('IndexError in link_url=', link_url)
        print('\n')
    except requests.exceptions.InvalidSchema:
        print('InvalidSchema')
        print('\n')
    except TypeError:
        print('\n')

print('\nEND')


