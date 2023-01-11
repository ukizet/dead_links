import requests
from tkinter import *
from bs4 import BeautifulSoup
import sqlite3 as sq

root = Tk()

def pass_link(event):
    global main_url
    main_url = e1.get()
    root.quit()

Label(root, text="Enter URL").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

root.bind('<Return>', pass_link)

mainloop()


page = requests.get(main_url)

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')

log = ()

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
            print('Link is working:', full_link_url)
    except NameError:
        print(f'NameError: {full_link_url}, {link_url}')
        print('\n')
    except IndexError:
        print(f'IndexError: {full_link_url}, {link_url}')
        print('\n')
    except requests.exceptions.InvalidSchema:
        print(f'requests.exceptions.InvalidSchema: {full_link_url}, {link_url}')
        print('\n')
    except TypeError:
        print(f'TypeError: {full_link_url}, {link_url}')
        print('\n')
    except requests.exceptions.MissingSchema:
        print(f'requests.exceptions.MissingSchema: {full_link_url}, {link_url}')
        print('\n')

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


