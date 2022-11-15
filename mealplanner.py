import requests,wikipediaapi,random,datetime,smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage

wikil=wikipediaapi.Wikipedia('en')

breakfast_page=wikil.page("List of breakfast foods")

#section 0 has the foods and not to call section object we have section again
breakfast_food_list=breakfast_page.sections[0].sections
# print(breakfast_food_list)

allbreakfast=[]

#
for sub in breakfast_food_list:
    if '\n' in sub.text:
        for food in sub.text.split('\n'):
            allbreakfast.append(food)
    else:
        allbreakfast.append(sub.text)

# print(allbreakfast)

#lunch food
url='https://www.buzzfeed.com/marietelling/easy-lunch-recipes-make-at-home'
lunch_html=requests.get(url).text
lunch_soup=BeautifulSoup(lunch_html,'html.parser')

all_lunch=[a.text for h2 in lunch_soup.find_all('h2') for a in h2.find_all('a')]
for i in range(0,4):
    del all_lunch[i]

#dinner food
url='https://www.buzzfeed.com/hannahloewentheil/weeknight-30-minute-dinner-recipes'
dinner_html=requests.get(url).text
dinner_soup=BeautifulSoup(dinner_html,'html.parser')

alldinner=[a.text for h2 in dinner_soup.find_all('h2') for a in h2.find_all('a')]
for i in range(0,4):
    del alldinner[i]
    





