import requests
import sys
from bs4 import BeautifulSoup

main_url = 'https://www.seoptimer.com/blog/broken-links/'

page = requests.get(main_url)

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')

log = ()

def logWriteClose(log):
    logTxt = open('C:/Users/ukika/Desktop/learnPython3/dead_links/log.txt', 'w')
    logTxt.write(str(log))
    logTxt.close()

for link in links:
    try:
        link_url = link.get('href')
        if link_url is None:
            continue
        if link_url == '':
            continue
        if link_url[0] == '/':
            full_link_url = main_url + link_url[1:]
        elif link_url[0] == '#':
            full_link_url = main_url + link_url
        else: 
            full_link_url = link_url
        

        response = requests.get(full_link_url)
        if response.status_code == 404:
            link_status = 'Link is not working'
            log += ((full_link_url, link_status),)
            print('Link is not working:', full_link_url)
        else:
            link_status = 'Link is working'
            log += ((full_link_url, link_status),)
            logWriteClose(log)
            print('Link is working:', full_link_url)
    except NameError:
        # print('')
        # print('\n')
        print('\nNot link:', link_url)
    except IndexError:
        print('IndexError in link_url=', link_url)
        print('\n')
    except requests.exceptions.InvalidSchema:
        print(f'InvalidSchema: {full_link_url}')
        print('\n')
    except TypeError:
        print('\n')


logWriteClose(log)
print('\nEND')


