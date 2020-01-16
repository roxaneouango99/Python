import requests # module to make http/htpps 
import html5lib # small parser package for html-5
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/HP-Touchscreen-Computer-Quard-Core-802-11ac/dp/B082PZVZB7/ref=sr_1_1_sspa?crid=23S4A884JAUMR&keywords=laptop&qid=1579030350&sprefix=lapt%2Caps%2C139&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4WlI5OUYxNVdWRlEmZW5jcnlwdGVkSWQ9QTAzNjIwMzUxTVZPSzFJTlZFTERKJmVuY3J5cHRlZEFkSWQ9QTA1MDAxMDAxRkMyWkZMM0lWMzhNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"

agent_header = {
    "User_Agent": agent

}
amazon_page = requests.get(amazon_url, headers=agent_header)

print(type(amazon_page.content))
soup = BeautifulSoup(amazon_page.content, "html5lib")
#print(soup.prettify())
#search a specific id
price_span= str(soup.find(id="priceblock_ourprice"))
print(price_span)

price = ""
for char in price_span:
    if char.isdgit() is True:
        price += char
    if char == ".":
        price += char
print(price)        

price = float(price)
max_price = 800
if price <= max_price:
    print("its all yours.")
else:
    print("oups, Anna got it.")