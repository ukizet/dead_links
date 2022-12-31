import requests
from bs4 import BeautifulSoup

main_url = 'https://www.seoptimer.com/blog/broken-links/'

page = requests.get(main_url)

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    try:
        link_url = link.get('href')
        response = requests.get(link_url)
    except:
        print('\nNot link:', link)

if response.status_code == 404:
    print('\nLink is not working:', link_url)
else:
    print('\nLink is working:', link_url)

print('\nEND')






# import requests

# links = ()

# for b in range(10):
#     url = 'https://www.seoptimer.com/blog/broken-links/soldzw/'
#     req = requests.get(url)
    
#     if req.status_code == 200:
#         stat = 'ok'
    
#     stat = 'notOk'

#     links_and_results = (url, stat)
#     links += (links_and_results,)

# print(links)


# import requests

# links = ()

# for b in range(10):
#     l = 'https://www.seoptimer.com/blog/broken-links/soldzw/'
#     req = requests.get(l)
    
#     links_and_results = (l, req.status_code)
#     links += (links_and_results,)

# print(links)







# import requests
# from concurrent.futures import ThreadPoolExecutor

# links = ()

# def get_link_status(url):
#     req = requests.get(url)
#     return (url, req.status_code)

# with ThreadPoolExecutor(max_workers=10) as executor:
#     for link in range(10):
#         l = 'https://www.seoptimer.com/blog/broken-links/soldzw/'
#         links += executor.submit(get_link_status, l).result()

# print(links)





# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)