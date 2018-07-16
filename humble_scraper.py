# source venv/bin/activate
# makes it show the dependencies of the virtual environment/packages just within venv
#will be using python requests library

# code-along with https://www.youtube.com/watch?v=7SWVXPYZLJM


import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/linux-geek-books"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

#bundle tiers
#class="dd-header-headline"

tiers = soup.select(".dd-game-row")

tier_dict={}

for tier in tiers:
    if tier.select('.dd-header-headline'):
        tiername = tier.select('.dd-header-headline')[0].text.strip()
            # will only have one, so need to specify index
    #grab tier product product_names
        product_names = tier.select(".dd-image-box-caption")
        product_names = [prodname.text.strip() for prodname in product_names]

        #add one product tier to our data structure
        tier_dict[tiername] = {"products": product_names }



tier_headlines = soup.select('.dd-header-headline')
stripped_tiernames = [tier.text.strip() for tier in tier_headlines]
#for tier in tier_headlines:
#    print(tier.text.strip())


# product names
# soup.select(".dd-image-box-caption")
#get the titles, then neext to get the index, then text, then stripped_tiernames
product_names = soup.select(".dd-image-box-caption")
stripped_product_names = [prodname.text.strip() for prodname in product_names]

# what is success going to look like?
# tier name, price. Will each have product 1, product 2, etc
#     - which data structure would map? A LIST
"""
new_tiers = []
for tier in tier_headlines:
    new_Tiers.append(tier.text.strip())
"""



"""
tiers = {
    "tier 1": {
        "price": 500,
        "products": [
            "name1"
            "name2"
        ]
    }
    "tier 2": {
        "price": 600,
        "products": [
            "name1"
            "name2"
        ]
    }
"""
# we care about the status/markup
# r.status_code
# r.text returns the HTML

# parsing - going to take a python library that understands HTML, parse it into a data structure that we can work with
# parsing with beautifulSoup (bs4)

# using pip3 install -r requirements.txt will automatically install the packages that it need

for tiername, tierinfo in tier_dict.items():
    # .items auto assigns indicies
    print (tiername)
#    print ('priced at', tierinfo['price'])
    print(", ".join(tierinfo['products']))
    print("\n\n")
