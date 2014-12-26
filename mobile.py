import requests  
from lxml import html
from urlparse import urlparse
import re

word=(raw_input("Enter your input : "))

urls=['http://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&ref=db931487-4b7b-496a-95f5-088473113c0c',
      'http://www.amazon.in/s/ref=sr_nr_n_1/275-7664783-0000827?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_n_operating_system_browse-bin%3A1485077031%2Cn%3A1805560031&bbn=1389432031&ie=UTF8&qid=1419456185&rnid=1389432031',
      'http://www.snapdeal.com/products/mobiles-mobile-phones'
      ]
for link in urls:
    response = requests.get(link)
    
    parsed_uri = urlparse(response.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    parsed_body = html.fromstring(response.text)

    if domain=='http://www.flipkart.com/':
        print "\n"
        print "Flipkart : \n"
        i=0
        total = len(parsed_body.xpath('//div[@class="pu-details lastUnit"]'))
        while i< total:
            title  = parsed_body.xpath('//div[@class="pu-details lastUnit"]/div/a/@title')[i]
            if word.lower() in title.lower():
                price  = parsed_body.xpath('//div[@class="pu-details lastUnit"]/div[@class="pu-price"]/div/div/span/text()')[i]
                rating = parsed_body.xpath('//div[@class="pu-details lastUnit"]/div[@class="pu-rating"]/div/@title')[i]
                print title+'-'+rating+'-'+price
            i=i+1
        
    elif domain=='http://www.amazon.in/':
        print "\n"
        i=0
        total = len(parsed_body.xpath('//div[@class="s-item-container"]'))
        print "Amazon : \n" 
        while i< total:
            title  = parsed_body.xpath('//div[@class="s-item-container"]/div[@class="a-row a-spacing-mini"]/div/a//h2/text()')[i]
            if word.lower() in title.lower():
                rating  = parsed_body.xpath('//div[@class="s-item-container"]/div[@class="a-row a-spacing-none"]/span/span/a/i/span/text()')[i]
                price = parsed_body.xpath('//div[@class="s-item-container"]/div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-none"]/a/span[@class="a-size-base a-color-price s-price a-text-bold"]/text()')[i]
                print title+'-'+rating+'-'+price
            i=i+1
        
    elif domain=='http://www.snapdeal.com/':
        print "\n"
        i=0
        total = len(parsed_body.xpath('//div[@class="product_listing_cont"]'))
        print "Snapdeal : \n" 
        while i< total:
            title  = parsed_body.xpath('//div[@class="product_listing_heading"]/a/text()')[i]
            if word.lower() in title.lower(): 
                price  = parsed_body.xpath('//div[@class="product_listing_price_outer"]/div/span/text()')[i]
                price=re.findall(r'\d+', price)[0]
                print title.replace('\n','').replace('\t','')+'- Cannot scrape rating- Rs-'+price
            i=i+1
                        
                        
        
        

    

    
            

