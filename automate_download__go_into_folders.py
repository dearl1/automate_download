import requests
import selenium
from lxml import html


# function to output name of variable and what the variable is
def pri(var_name, str_var_name):
    
    print(f"\n\n   {str_var_name} ...")
    print(var_name)


# flight dynamics/lecture notes
url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2050170_1'

# flight dynamics/lecture notes/in-class notes
##url = 'https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1'


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

##    pri(html, "html")

# end of: seleneium


# save and load html variable
if 1:
    import pickle

    # write to file
##    with open('html_data.pickle', 'wb') as my_file:
##    	pickle.dump([html], my_file)

    # read from file
    with open('html_data.pickle', 'rb') as my_file:
        [html] = pickle.load(my_file)

    ##print("\n   html ...")
    ##print(html)


if 1:

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    ##print("\n\n   Using beautiful soup...")
    ##print(soup.prettify())

    ##print("\n\n   soup.find_all ...")
    ##print(soup.find_all("a"))

    anchor_tags = soup.find_all("a")


    # I can find the file and folder anchor tags by finding where len(i.contents[0].text) > 0 and where the target attribute==None
    # I think I can find the phugoid, SPPO, dutch roll anchor tags by finding where len(i.contents[0]) > 1 and where the target attribute==_blank
        # and id attribute==None and title attribute==None
    # I think I can find the anchor tags that are folders and only folders which have this '/webapps/blackboard/content/listContent.jsp?course_id=' in their href
        # and title attribute==None and target attribute==None.
        # The variable 'text' is the name of the folder.
    # I think I can find all anchor tags which are files (incl phugoid type files) by searching for xid in the href.
        # The variable 'text' is the name of the file but if text==None then the name of the file is i.contents[0].
    
        # Announcements is count = 16
        # lecture notes is count = 27
        # introductory slides is count = 29
        # Body Fixed to Earth axes script is count = 31
        # in-class notes is count = 33

        # Phugoid-sync.mp4 is count = 35
        # SPPO-sync.mp4 is count = 38
        # dutch roll - sync.mp4 is count = 41

        # [16, 27, 29, 31, 33, 35, 38, 41]

    files = []
    folders = []
    
    print("\n\n   Extracting anchor tags...\n")
    count = 0
    while count < len(anchor_tags):
        if 1: # if count in [16, 33]: # if count in [16, 27, 29, 31, 33, 35, 38, 41]:
        
            i = anchor_tags[count]
            href = i["href"]

            contents_0 = i.contents[0]


            # try to get text of contents
            try:
                text = i.contents[0].text
            except:
                text = None


            # try to get target attribute
            try:
                target = i["target"]
            except:
                target = None


            # try to get id attribute
            try:
                id_attrib = i["id"]
            except:
                id_attrib = None


            # try to get title attribute
            try:
                title = i["title"]
            except:
                title = None


            # add the current anchor tag to the files list if it's a file
            if "xid" in href: # It's a file
                if text == None: # It's of the phugoid type
                    files.append([href, contents_0])
                else: # It's not of the phugoid type
                    files.append([href, text])

            # add the current anchor tag to the folders list if it's a folder
            if "/webapps/blackboard/content/listContent.jsp?course_id=" in href and title == None and target == None: # It's a folder
                folders.append([href, text])
            

##            print(f"count: {count}")
##            
##            print(i)
##            
##            print("\n   contents[0] of anchor tag ...")
##            print(i.contents[0])
##            
##            print("\n   href of anchor tag ...")
##            print(href)
##
##            pri(text, "text")
##            pri(target, "target")


##            if len(i.contents[0]) > 1 and target == "_blank" and id_attrib == None and title == None:
##
##                print(f"count: {count}")
##                print(f"len(i.contents[0]): {len(i.contents[0])}")
##                
##                print("\nWe have extracted this anchor ...")
##                print(f"contents_0: {contents_0}")
##                print("\n   **********************\n")

##            print("\n   **********************\n")
            
        count += 1

    print("\n\n   Outputting just the anchor tags that are files ...\n")

    max_length = max( [len(name)
                       for (href, name) in files] )
    
##    print( [len(name) for (href, name) in files] )
##    pri(max_length, "max_length")
##    print()
    
    for i in files:
        print(f"{i[1]}{' '*(max_length - len(i[1]))}   href: {i[0]}")

    print("\n\n   Outputting just the anchor tags that are folders ...\n")

    max_length = max( [len(name)
                       for (href, name) in folders] )
    
    for i in folders:
        print(f"{i[1]}{' '*(max_length - len(i[1]))}   href: {i[0]}")
    # https://bb.imperial.ac.uk
    # /webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1
    # https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_23856_1&content_id=_2071657_1

##    print("\n\n   Try to get text of contents of all anchor tags...")
##    for i in anchor_tags:
##
##        print("\n   Try to get text of contents from anchor tag ...")
##        try:
##            text = i.contents[0].text
##            print(text)
##        except:
##            print("Unable to get text from contents")
##
##        print()
##            
##        print(i.contents[0])
####        print(i.contents[0].text)
##        print()


##    anchor_tags__no_class = soup.find_all("a", attrs={'class': None})

    ##print("\n   Output anchor_tags__no_class ... \n")
    # output anchor_tags__no_class
    ##for i in anchor_tags__no_class:
    ##    print(i)
    ##    print()


    ##anchor_tags__filtered = soup.find_all( "a", attrs={'class': None, 'onclick': True} )
    ##for i in anchor_tags__filtered:
    ##    print(i)
    ##    print()


##    print("\n   Output anchor_tags__filtered ... \n")
##    anchor_tags__filtered = soup.find_all( "a", attrs={'class': False, 'onclick': True, 'id': False} )
##    for i in anchor_tags__filtered:
##        print(i)
##        print()


    # compare lengths of different extractions of anchor tags
##    print()
##    print(f"anchor_tags has length of: {len(anchor_tags)}")
##    print(f"anchor_tags__no_class has length of: {len(anchor_tags__no_class)}")
##    print(f"anchor_tags__filtered has length of: {len(anchor_tags__filtered)}")


    # download the files
##    print("\n\n   Starting: download files")
##    
##    base_href = "https://bb.imperial.ac.uk"
##
##    for element in anchor_tags__filtered:
####        print()
##        
##        # get href
##        href = element["href"]
####        print("\n\n   Output the href we have found ...")
####        print(href)
##
##        total_href = base_href + href
####        pri(total_href, "total_href")
##
####        first_file = anchor_tags__filtered[0]
####        pri(first_file, "first_file")
##
##        file_name = element.contents[0].text
####        pri(file_name, "file_name")
##
##
##        # download the file
##        driver.get(total_href) # open the file
##        url_now = driver.current_url # get the url
##        
####        pri(url_now, "url_now")
##
##        r = requests.get(url_now, allow_redirects=True)
####        pri(r, "r")
##
##        root_location = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download\\"
##        open(root_location + file_name + ".pdf", 'wb').write(r.content)
##
##    driver.quit()
##
##    print("\n\n   Finished: downloading files")







