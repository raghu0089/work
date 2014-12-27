import requests  
from lxml import html
from urlparse import urlparse


word=(raw_input("Enter your input : "))

urls=[
      'http://www.flipkart.com/mobiles/pr?q='+word+'&as=on&as-show=on&otracker=start&sid=tyy%2C4io&as-pos=1_1_ic_nexus',
      'http://www.amazon.in/s/ref=sr_ex_n_1?rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Ck%3A'+word+'&bbn=1389432031&keywords='+word+'&ie=UTF8&qid=1419634271',
      'http://www.snapdeal.com/search?keyword='+word+'&santizedKeyword=&catId=&categoryId=175&suggested=true&vertical=p&noOfResults=20&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=true&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&catalogID=&dealDetail='
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
        element=parsed_body.xpath('//div[@class="s-item-container"]')
        total = len(parsed_body.xpath('//div[@class="s-item-container"]'))
        print "Amazon : \n" 
        while i< total:
               
            title  = parsed_body.xpath('//div[@class="s-item-container"]/div[@class="a-row a-spacing-mini"]/div/a//h2/text()')[i]
            if word.lower() in title.lower():
                rating  = parsed_body.xpath('//div[@class="s-item-container"]/div[@class="a-row a-spacing-none"]/span/span/a/i/span/text()')[i]                
                check_price= element[i].xpath('.//div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-none"]/a/span[@class="a-size-base a-color-price s-price a-text-bold"]/text()')
                if not check_price:
                    print title+'-'+rating+'- Not Available'
                else:
                    print title+'-'+rating+'-'+check_price[0]
                
            i=i+1
        
    elif domain=='http://www.snapdeal.com/':
        print "\n"
        i=0
        element=parsed_body.xpath('//div[@class="hoverProductWrapper product-txtWrapper  "]')
        total = len(parsed_body.xpath('//div[@class="hoverProductWrapper product-txtWrapper  "]'))
        print "Snapdeal : \n" 
        while i< total:
            title  = parsed_body.xpath('//div[@class="product-title"]/a/text()')[i]
            if word.lower() in title.lower(): 
                price  = parsed_body.xpath('//a[@id="prodDetails"]/div[@class="product-price"]/div/span[@id="price"]/text()')[i]
                check_rating  = element[i].xpath('.//a[@id="prodDetails"]/div[@class="ratingsWrapper"]/div[@class="ratingStarsSmall"]/@ratings')
                if not check_rating:
                    print title.replace('\n','').replace('\t','')+'-'+'Not Available'+'-'+price
                else:
                    print title.replace('\n','').replace('\t','')+'-'+check_rating[0]+'-'+price
               
            i=i+1
                        
                        
        
        

    

    
            

