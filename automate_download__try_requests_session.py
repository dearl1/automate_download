import requests
from bs4 import BeautifulSoup


# flight dynamics location
url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'

# handwritten notes
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4435255?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=7D4WUes2X7NMv9rbNz4Dg%2Fl1r6TNCIWBIWzfEcI0je4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520notes.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=73b50d4b8526ae88884c8e72f3c0648bcf3a173d850e764e71a20d4f0e18bbb7'

# all flight dyn notes
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4546262?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=1qtS10B28NfSGAbyo397yy8RSTKoMRBmB4Eamq0Yca4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520%2526%2520Control%2520-%25202020-21%25282%2529.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=0b3f5766567effd8b7194bb73cf9b029e04af2c86b83120ae114a7fdb07c2f39'


##r = requests.get(url, allow_redirects=True)

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



##print("\n\n   Using beautiful soup...")
##soup = BeautifulSoup(r.content, 'html.parser')
##print(soup.prettify())
##
##print("\n   soup.find_all ...")
##print(soup.find_all("a"))

################################

session = requests.session()

##login_data = {
##    'username': ,
##    'csrfmiddlewaretoken': ,
##    'password': ,
##    'next': '/course/2021573/french-1-145/garden/speed_review/?source_element=ms_mode&source_screen=eos_ms'
##}

r = session.get(url) #this will redirect you and it might load some initial cookies info

##r = session.post('https://<theurl>/login.py', login_data)

print("   r ...")
print(r)


print("\n\n   Using beautiful soup...")
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

print("\n   soup.find_all ...")
print(soup.find_all("a"))


##if r.status_code == 200: #if accepted the request
##    res = session.get(url)
##    soup = BeautifulSoup(res.text, 'html.parser')
##    ## (...) your scraping code


