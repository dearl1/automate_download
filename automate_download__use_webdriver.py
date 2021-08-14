import requests
import selenium
from lxml import html

##url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2050170_1'

# flight dynamics location
##url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'

# handwritten notes
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4435255?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=7D4WUes2X7NMv9rbNz4Dg%2Fl1r6TNCIWBIWzfEcI0je4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520notes.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=73b50d4b8526ae88884c8e72f3c0648bcf3a173d850e764e71a20d4f0e18bbb7'

# all flight dyn notes
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4546262?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=1qtS10B28NfSGAbyo397yy8RSTKoMRBmB4Eamq0Yca4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520%2526%2520Control%2520-%25202020-21%25282%2529.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=0b3f5766567effd8b7194bb73cf9b029e04af2c86b83120ae114a7fdb07c2f39'


##print("   r ...")
##print(r)
##
##print("\n   *******\n")
##print("   r.headers.get ...")
##print(r.headers.get('content-type'))
##
##print("\n   *******\n")
##print("   r.text ...")
##print(r.text)


# saving files
##open('filename', 'wb').write(r.content)

##open('handwritten notes.pdf', 'wb').write(r.content)


########
# use selenium

##from selenium import webdriver
##import time
##
##driver = webdriver.Chrome(executable_path=r'C:\Users\danny\Downloads\chromedriver_win32\chromedriver.exe')
####url = 'https://bb.imperial.ac.uk/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'
##url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'
##driver.get(url)
##
####time.sleep(15)
##continue_code = input("\n\n Type anything and press enter once you have entered your credentials to continue: ")
##
##driver.get(url)
##
####time.sleep(2)
##
##html = driver.page_source

# end of: seleneium


# save and load html variable
import pickle

# write to file
##with open('html_data.pickle', 'wb') as my_file:
##	pickle.dump([html], my_file)

# read from file
with open('html_data.pickle', 'rb') as my_file:
    [html] = pickle.load(my_file)

##print("\n   html ...")
##print(html)


##r = requests.get(url, allow_redirects=True)
##
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
##print("\n\n   Using beautiful soup...")
##print(soup.prettify())

print("\n\n   soup.find_all ...")
##print(soup.find_all("a"))

anchor_tags = soup.find_all("a")

##for i in anchor_tags:
##    print(i)
##    print()


anchor_tags__no_class = soup.find_all("a", attrs={'class': None})

# compare lengths of anchor_tags and anchor_tags__no_class
print(f"anchor_tags has length of: {len(anchor_tags)}")
print(f"anchor_tags__no_class has length of: {len(anchor_tags__no_class)}")

print("\n   Output anchor_tags__no_class ... \n")
# output anchor_tags__no_class
##for i in anchor_tags__no_class:
##    print(i)
##    print()


##anchor_tags__filtered = soup.find_all( "a", attrs={'class': None, 'onclick': True} )
##for i in anchor_tags__filtered:
##    print(i)
##    print()


anchor_tags__filtered = soup.find_all( "a", attrs={'class': False, 'onclick': True, 'id': False} )
for i in anchor_tags__filtered:
    print(i)
    print()


# compare lengths of anchor_tags and anchor_tags__no_class
print(f"anchor_tags has length of: {len(anchor_tags)}")
print(f"anchor_tags__no_class has length of: {len(anchor_tags__no_class)}")
print(f"anchor_tags__filtered has length of: {len(anchor_tags__filtered)}")



# how to connect the extracted url to the base url of blackboard
##https://bb.imperial.ac.uk/bbcswebdav/pid-2071661-dt-content-rid-8358309_1/xid-8358309_1











