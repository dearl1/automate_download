
import requests
import selenium
from lxml import html
from bs4 import BeautifulSoup
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import shutil
from shutil import copyfile


# function to output name of variable and what the variable is
def pri(var_name, str_var_name):
    
    print(f"\n\n   {str_var_name} ...")
    print(var_name)


# function to make location directory
def make_location_directory(soup):
    count = 1
    crumb_names = []
    while 1:
        crumb_name = "crumb_" + str(count)
        crumb_element = soup.find("span", attrs={'id': crumb_name})

        if crumb_element == None:
##            print(f"{crumb_name} was not found")
            break
        elif len(crumb_element) == 1:
            contents_0 = crumb_element.contents[0]

            # get rid of white space
            contents_0 = contents_0.split()
            contents_0 = " ".join(contents_0)

            crumb_names.append(contents_0)            
            
        count += 1

##    pri(crumb_names, "crumb_names")

    location_directory = "\\".join(crumb_names)
##    pri(location_directory, "location_directory")

    root_location_directory = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download"
    location_directory = "\\".join([root_location_directory, location_directory])
##    pri(location_directory, "location_directory")

    return location_directory

# end of: function to make location directory


# function to empty the download directory
def empty_download_dir():
    # make a download directory in the computer if it doesn't exist already
    
    location_download = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download\\download"
    
    if os.path.exists(location_download):

        # delete all the files in the directory i.e. empty the directory
        for file_name in os.listdir(location_download):
            path_and_file_name = "\\".join([location_download, file_name])
            os.remove(path_and_file_name)

    else:
        print("Error. You tried to empty a directory which doesn't exist.")

# end of: function to empty the download directory


##############
# list of urls

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


if 1:
    # make a download directory in the computer if it doesn't exist already
    location_download = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download\\download"
    if not os.path.exists(location_download):
        os.makedirs(location_download)


########
# use selenium
if 1:      
    # create a webdriver and set the download directory
    chromeOptions = webdriver.ChromeOptions()
    
    prefs = {"download.default_directory" : location_download}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromedriver = "C:\\Users\danny\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(executable_path = chromedriver, options = chromeOptions)

    driver.get(url) # open the flight dynamics/lecture notes blackboard location

    # put in de219
    inputElement = driver.find_element_by_id("username")
    inputElement.send_keys('de219')
    

    print("\n\nNavigate to the location from which you want to download files.")
    continue_code = input("Now type anything and press enter once to continue: ")

    html = driver.page_source # get the html so we can find the names and hrefs of the files that need to be downloaded


##    url_now = driver.current_url
##    pri(url_now, "url_now")
##
##    continue_code = input("\n\nNavigate to a new location if you want.\nThen type anything and press enter to continue: ")
##    url_now = driver.current_url
##    pri(url_now, "url_now")

##    pri(html, "html")

# end of: seleneium


# save and load html variable
if 0:
    import pickle

    # write to file
    ##with open('html_data.pickle', 'wb') as my_file:
    ##	pickle.dump([html], my_file)

    # read from file
    with open('html_of_lctn__flightDyn_lecNotes.pickle', 'rb') as my_file:
        [html] = pickle.load(my_file)

    ##print("\n   html ...")
    ##print(html)


# get hrefs of files in current blackboard location
if 1:
    files = []

    soup = BeautifulSoup(html, 'html.parser')

    anchor_tags = soup.find_all("a")

    for index in range(len(anchor_tags)):
        anchor = anchor_tags[index]

        # try to get href
        try:
            href = anchor["href"]
        except:
            href = None

        contents_0 = anchor.contents[0]

        # try to get text of contents
        try:
            text = anchor.contents[0].text
        except:
            text = None

        # add the current anchor tag to the files list if it's a file
        if href != None:
            if "xid" in href: # It's a file
                if text == None: # It's of the phugoid type
                    files.append([href, contents_0])
                else: # It's not of the phugoid type
                    files.append([href, text])

##    pri(files, "files")


# check if file types (e.g. ".mp4") are in the file names
if 1:
##    print("\n\n   Checking if there is a dot in each of the file names ...")
    
    for file in files:
        if "." not in file[1]:
##            print(f"{file[1]} does not have a dot")
            # put ".pdf" on the end of file names that don't have a dot
            file[1] = "".join([file[1], ".pdf"])


    
if 1:
    # make sure hrefs have the correct base
    
    base_href = "https://bb.imperial.ac.uk"

    for index in files:
        if base_href not in index[0]:
            index[0] = "".join([base_href, index[0]])


    # Outputting the list of files that will be downloaded to the shell
    print("\n\n   Outputting the list of files that will be downloaded if you want ...\n")
    
    max_length = max( [len(name)
                       for (href, name) in files] )
    
    for i in files:
        print(f"{i[1]}{' '*(max_length - len(i[1]))}   {i[0]}")


    # output where in the computer the files will be downloaded to
    location_directory = make_location_directory(soup)
    print(f"\n\n   These files will be downloaded to ...\n{location_directory}")


if 1:
    # make a directory in the computer if it doesn't exist already
    if not os.path.exists(location_directory):
        os.makedirs(location_directory)


##    # set download directory in the webdriver
##    chromeOptions = webdriver.ChromeOptions()
##    prefs = {"download.default_directory" : location_directory}
##    chromeOptions.add_experimental_option("prefs",prefs)
##    chromedriver = "C:\\Users\danny\Downloads\chromedriver_win32\chromedriver.exe"
##    driver = webdriver.Chrome(executable_path = chromedriver, options = chromeOptions)
##
##    driver.get(url) # open the flight dynamics/lecture notes blackboard location again
##
##    continue_code = input("\n\n Type anything and press enter once you have entered your credentials to continue: ")

# download the files in the current blackboard location
if 1:
    print("\n\n   Starting: download files")

    for file_count in [1]:

        file = files[file_count]

        file_name = file[1]
        file_href = file[0]

        # empty the download directory because we want to work from a clean slate
        empty_download_dir()        
        
        # open the file
        driver.get(file_href)

        # see if the number of files in the download directory has increased from 0 to 1
        num_of_files = len( [ name for name in os.listdir(location_download) ] )
        pri(num_of_files, "num_of_files")

        if num_of_files == 1: # we need to move this file which is in the download directory into the correct directory with all the other files
            download_file_name = os.listdir(location_download)
            download_file_name = download_file_name[0]
            download_file_name_split = download_file_name.split(".")

            # get just the name of the file which blackboard gives this file (don't include the file extension)
            just_name = file_name.replace(".pdf", "")

            just_name_count = just_name

            count = 1
            while 1:
                if not os.path.exists( f"{location_directory}\\{just_name_count}.{download_file_name_split[1]}" ): # If the file doesn't already exist then:
                    # Move the file which is in the download directory into the correct directory.
                        # But change the name to what blackboard gives the file while keeping the file extension the same as what it was when it was in the download
                        # directory.

##                    os.rename(f"{location_download}\\{download_file_name}", f"{location_directory}\\{just_name_count}.{download_file_name_split[1]}")
                    copyfile(f"{location_download}\\{download_file_name}", f"{location_directory}\\{just_name_count}.{download_file_name_split[1]}")
                    break
                else:
                    # Append a number to the file name if there is already a version of the file present.
                    just_name_count = f"{just_name} ({count})"
                    count += 1
                    
        else: # nothing went into the download directory so we need to get the url and download manually to the correct directory
        
            url_now = driver.current_url # get the url
            r = requests.get(url_now, allow_redirects=True)

            file_name_split = file_name.split(".")
            just_file_name = file_name_split[0]
            
            just_file_name_count = just_file_name
            file_extension = file_name_split[1]

            count = 1
            while 1:
                if not os.path.exists( f"{location_directory}\\{just_file_name_count}.{file_extension}" ): # If the file doesn't already exist then:
                    # Download the file to the correct directory
                    open(f"{location_directory}\\{just_file_name_count}.{file_extension}", 'wb').write(r.content)
                    break
                else:
                    # Append a number to the file name if there is already a version of the file present.
                    just_file_name_count = f"{just_file_name} ({count})"
                    count += 1
                    

    # close the webdriver
##    driver.quit()

    print("\n\n   Finished: downloading files")









