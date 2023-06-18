#leetcode
"""
import requests
from bs4 import BeautifulSoup
import csv

with open("leetcode.csv")as f1:
    data=list(csv.reader(f1))
    data=data[1:]
res=[]
for d in data:
    # Making a GET request
    r = requests.get(d[-1])

    # check status code for response received
    # success code - 200
    if r.status_code==200:

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        s = soup.find('div', class_='text-[24px] font-medium text-label-1 dark:text-dark-label-1')
        print(s.text)
        rr=[s.text,d[0]]
    else:
        rr=["link wrong",d[0]]
    res.append(rr)
    r=[]
    
"""
"""
#Hackerrank
from bs4 import BeautifulSoup
import requests

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
url = 'https://www.hackerrank.com/sudhirrr?hr_r=1'
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
s = soup.find_all('div', class_='hacker-badge')
for k in s:
    s1 = k.find('text', class_='badge-title')
    s1s = k.find_all('svg', class_='badge-star')
    print(s1.text,len(s1s))

"""

#GFG
"""
from bs4 import BeautifulSoup
import requests

r = requests.get('https://auth.geeksforgeeks.org/user/sudhirreddy/practice/')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find_all('span', class_='score_card_value')
print(s[1].text)
"""

#Codechef

from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.codechef.com/users/sudhirreddy')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('section', class_='rating-data-section problems-solved')
s = soup.find_all('h5', class_='')
res=s[0].text.split('(')
res=res[1].split(')')
print(res[0])





















