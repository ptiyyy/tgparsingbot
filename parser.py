import requests
from bs4 import BeautifulSoup

def get_anekdot():
   headers = {
       'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.52'
   }
   url = 'https://www.anekdot.ru/random/anekdot/'
   s = requests.Session()
   r = s.get(url=url, headers=headers)

   soup = BeautifulSoup(r.text, 'lxml')
   anekdot = soup.find('div', class_="text").text
   with open("anekdot.txt", "w") as file:
      file.write(anekdot)
