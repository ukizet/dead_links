import requests
from tkinter import *
from bs4 import BeautifulSoup
import sqlite3 as sq

root = Tk()

# creating function that will recieve link from user jj

def pass_link(event):
    # creating a global variable that will keep a url entered by user
    global main_url
    main_url = e1.get()
    root.quit()

# making "GUI" of the program

Label(root, text="Enter URL").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

# binding enter to call pass_link function

root.bind('<Return>', pass_link)

mainloop()

# getting smth from url.. maybe getting html code..

page = requests.get(main_url)

# parsing page

soup = BeautifulSoup(page.text, 'html.parser')

# searching all links that page have

links = soup.find_all('a')

# creating log string for.. logs.. But with sqlite we don't really need this, i should delete it

log = ()

# starting cycle that will check all links for malfunction

for link in links:
    try:
        # receiving links from href arguments

        link_url = link.get('href')

        # checking if link_url varible is not empty

        if link_url is None:
            continue
        if link_url == '':
            continue

        # checking if link_url varible dont starts with '/'

        if link_url[0] == '/':
            full_link_url = main_url + link_url[1:]

        # checking if link_url varible dont starts with '#'

        elif link_url[0] == '#':
            full_link_url = main_url + link_url
        else:
            full_link_url = link_url

        # getting site status code

        response = requests.get(full_link_url)
        if response.status_code == 404:
            link_status = 'Link is not working'
            log += ((full_link_url, link_status),)
            print('Link is not working:', full_link_url)
        else:
            link_status = 'Link is working'
            log += ((full_link_url, link_status),)
            print('Link is working:', full_link_url)

    # working with possible exceptions

    except NameError:
        print(f'NameError: {full_link_url}, {link_url}')
        print('\n')
    except IndexError:
        print(f'IndexError: {full_link_url}, {link_url}')
        print('\n')
    except requests.exceptions.InvalidSchema:
        print(
            f'requests.exceptions.InvalidSchema: {full_link_url}, {link_url}')
        print('\n')
    except TypeError:
        print(f'TypeError: {full_link_url}, {link_url}')
        print('\n')
    except requests.exceptions.MissingSchema:
        print(
            f'requests.exceptions.MissingSchema: {full_link_url}, {link_url}')
        print('\n')

# making log db file

with sq.connect("dead_links/log.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS links")
    cur.execute("""CREATE TABLE IF NOT EXISTS links (
        link_id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        link_status TEXT
        )""")

    cur.executemany("INSERT INTO links VALUES(NULL, ?, ?)", log)

print('\nEND')
