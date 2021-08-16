
# use crumb_1, 2 and 3 from html to know where in the tree the user is at in the webdriver.

import requests
import selenium
from lxml import html
from bs4 import BeautifulSoup


# function to output name of variable and what the variable is
def pri(var_name, str_var_name):
    
    print(f"\n\n   {str_var_name} ...")
    print(var_name)


# main blackboard page
##url = "https://bb.imperial.ac.uk/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1"

##url = "https://bb.imperial.ac.uk/bbcswebdav/pid-2071661-dt-content-rid-8358309_1/xid-8358309_1"
##r = requests.get(url, allow_redirects=True)
##pri(r, "r")

# flight dynamics/lecture notes
url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2050170_1'

# flight dynamics/lecture notes/in-class notes
##url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'

# handwritten notes pdf
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4435255?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=7D4WUes2X7NMv9rbNz4Dg%2Fl1r6TNCIWBIWzfEcI0je4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520notes.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=73b50d4b8526ae88884c8e72f3c0648bcf3a173d850e764e71a20d4f0e18bbb7'

# handwritten notes pdf url opened at approx 2021_08_14
##https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4435255?X-Blackboard-Expiration=1628964000000&X-Blackboard-Signature=%2Fh%2B4AvXcIycUGWBAWZhUlysvJSjO1o5%2F0PDViphN5fA%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520notes.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210814T120000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210814%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=8cb7bc2773bfb72d61fd7f35059f6a0e2bed88de46d154b0ec8be77763d01a34
# Ch 1-7 - Annotated pdf url opened at approx 2021_08_14
##https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4521639?X-Blackboard-Expiration=1628964000000&X-Blackboard-Signature=iSZupkWaThoJ%2B9BFI8LEI1swYKzucDS%2Fx3WhJVs2fZs%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520%2526%2520Control%2520-%25202021%2520-%2520ch%25201-7%2520annotated.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210814T120000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210814%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=be8faa624168fbdb53a9b5788259a00bf12be87c51f2d69eabec3529fb7a612f


# all flight dyn notes pdf
##url = 'https://learn-eu-central-1-prod-fleet01-xythos.content.blackboardcdn.com/60faa9080242d/4546262?X-Blackboard-Expiration=1628726400000&X-Blackboard-Signature=1qtS10B28NfSGAbyo397yy8RSTKoMRBmB4Eamq0Yca4%3D&X-Blackboard-Client-Id=309628&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Flight%2520Dynamics%2520%2526%2520Control%2520-%25202020-21%25282%2529.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210811T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20210811%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=0b3f5766567effd8b7194bb73cf9b029e04af2c86b83120ae114a7fdb07c2f39'


########
# use selenium
if 0:
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path=r'C:\Users\danny\Downloads\chromedriver_win32\chromedriver.exe')

    # flight dynamics/lecture notes/in-class notes
##    url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'

    #url = "https://bb.imperial.ac.uk/bbcswebdav/pid-2071661-dt-content-rid-8358309_1/xid-8358309_1"

    driver.get(url)

    continue_code = input("\n\n Type anything and press enter once you have entered your credentials to continue: ")

    html = driver.page_source

##    url_now = driver.current_url
##    pri(url_now, "url_now")
##
##    continue_code = input("\n\nNavigate to a new location if you want.\nThen type anything and press enter to continue: ")
##    url_now = driver.current_url
##    pri(url_now, "url_now")

##    pri(html, "html")

# end of: seleneium


# save and load html variable
if 1:
    import pickle

    # write to file
    ##with open('html_data.pickle', 'wb') as my_file:
    ##	pickle.dump([html], my_file)

    # read from file
    with open('html_of_lctn__flightDyn_lecNotes.pickle', 'rb') as my_file:
        [html] = pickle.load(my_file)

    ##print("\n   html ...")
    ##print(html)


# test get tree location of current location in blackboard using crumbs
if 1:

##    soup = BeautifulSoup(r.content, 'html.parser')
    
    soup = BeautifulSoup(html, 'html.parser')
    anchor_tags = soup.find_all("a")
    
##    for i in anchor_tags:
##        print(i)
##        print()

    crumb_1 = soup.find_all("span", attrs={'id': "crumb_1"})
    crumb_1_length = len(crumb_1)
    pri(crumb_1_length, "crumb_1_length")
    pri(crumb_1, "crumb_1")

    contents_0 = crumb_1[0].contents[0]
    pri(contents_0, "contents_0")

    length = len(contents_0)
    pri(length, "length")

    length = len("AERO50002 - Flight Dynamics and Control 2020-2021")
    pri(length, "length")

    contents_0 = contents_0.split()
    pri(contents_0, "contents_0")

    contents_0 = " ".join(contents_0)
    pri(contents_0, "contents_0")
        
# end getting crumbs


if 0:

    soup = BeautifulSoup(html, 'html.parser')
    ##print("\n\n   Using beautiful soup...")
    ##print(soup.prettify())

    ##print("\n\n   soup.find_all ...")
    ##print(soup.find_all("a"))

    anchor_tags = soup.find_all("a")

    ##for i in anchor_tags:
    ##    print(i)
    ##    print()


    anchor_tags__no_class = soup.find_all("a", attrs={'class': None})

    ##print("\n   Output anchor_tags__no_class ... \n")
    # output anchor_tags__no_class
    ##for i in anchor_tags__no_class:
    ##    print(i)
    ##    print()


    ##anchor_tags__filtered = soup.find_all( "a", attrs={'class': None, 'onclick': True} )
    ##for i in anchor_tags__filtered:
    ##    print(i)
    ##    print()


    print("\n   Output anchor_tags__filtered ... \n")
    anchor_tags__filtered = soup.find_all( "a", attrs={'class': False, 'onclick': True, 'id': False} )
    for i in anchor_tags__filtered:
        print(i)
        print()


    # compare lengths of different extractions of anchor tags
    print()
    print(f"anchor_tags has length of: {len(anchor_tags)}")
    print(f"anchor_tags__no_class has length of: {len(anchor_tags__no_class)}")
    print(f"anchor_tags__filtered has length of: {len(anchor_tags__filtered)}")


    base_href = "https://bb.imperial.ac.uk"

    print("\n\n   Starting: download files")
    # get all the hrefs in a loop
    for element in anchor_tags__filtered:
##        print()
        
        # get href
        href = element["href"]
##        print("\n\n   Output the href we have found ...")
##        print(href)

        total_href = base_href + href
##        pri(total_href, "total_href")

##        first_file = anchor_tags__filtered[0]
##        pri(first_file, "first_file")

        file_name = element.contents[0].text
##        pri(file_name, "file_name")


        # download the file
        driver.get(total_href) # open the file
        url_now = driver.current_url # get the url
        
##        pri(url_now, "url_now")

        r = requests.get(url_now, allow_redirects=True)
##        pri(r, "r")

        root_location = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download\\"
        open(root_location + file_name + ".pdf", 'wb').write(r.content)

    driver.quit()

    print("\n\n   Finished: downloading files")








