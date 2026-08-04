## real world example multithreading for I/O Bound Task scenario: web scraping 

'''https://www.geeksforgeeks.org/explore?page=1


https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-langchain/


https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''



import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://www.geeksforgeeks.org/explore?page=1'\

'https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-langchain/'

'https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    print(f'fetched{(len(soup.text))} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fartched")