
# change the user_name variable that is inputted to the webdriver
# change the root_location_directory
# change the location_download in 2 places if you want to but it's only used temporarily and released at the end of the code so you don't need to change this

import requests
import selenium
from lxml import html
from bs4 import BeautifulSoup
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import shutil
from shutil import copyfile

import time


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
##    print("\n starting function: empty_download_dir")
    # make a download directory in the computer if it doesn't exist already
    
    location_download = "C:\\Users\\danny\\Documents\\1 - Not backed up to external hard drive yet\\automate_download\\download"
    
    if os.path.exists(location_download):

        # delete all the files in the directory i.e. empty the directory
        for file_name in os.listdir(location_download):
            path_and_file_name = "\\".join([location_download, file_name])
            os.remove(path_and_file_name)

    else:
        print("Error. You tried to empty a directory which doesn't exist.")

##    print("\n finished function: empty_download_dir")

# end of: function to empty the download directory


# function that checks if "tmp" extension no longer exists on a file which is downloading
def wait_for_download(location_download):
    download_file_name_extension = "tmp"
    
    while download_file_name_extension == "tmp" or download_file_name_extension == "crdownload":
        download_file_name = os.listdir(location_download)

        if len(download_file_name) == 0:
            continue # wait a bit for the download to actually start
        
        download_file_name = download_file_name[0]
        
        download_file_name_split = download_file_name.split(".")

        download_file_name_extension = download_file_name_split[-1]

    return (download_file_name, download_file_name_split)

# end of: function that checks if "tmp" extension no longer exists on a file which is downloading


##############
# list of urls

# main blackboard page
url = "https://bb.imperial.ac.uk/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1"

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

    driver.get(url) # open the blackboard location

    # enter user_name to the webpage
    user_name = 'de219'
    inputElement = driver.find_element_by_id("username")
    inputElement.send_keys(user_name)

    # click into password box
    inputElement = driver.find_element_by_id("password")
    inputElement.click()


# run the code forever until the user quits
user_location = None
while 1:

    if user_location != None:
        driver.get(user_location) # go back to the location in blackboard where the user last was
    
    # allow the user to go to the place they want to download files from
    print("\n\nNavigate to the location from which you want to download files.")

    while 1:
        while 1:
            try:
                continue_code = str(input("Type d to download or type quit: "))
                break
            except:
                print("There was an error")
                continue
        
        if continue_code not in ["d", "quit"]:
            print("\nBad input")
        else:
            break

    if continue_code == "quit":
        print("\nExiting the program")
        break

    html = driver.page_source # get the html so we can find the names and hrefs of the files that need to be downloaded

    user_location = driver.current_url # save where the user has navigated to


    # get hrefs of files in current blackboard location
    if 1:
        files = []

        soup = BeautifulSoup(html, 'html.parser')

        anchor_tags = soup.find_all("a")

        for index in range(len(anchor_tags)): # for index in range(len(anchor_tags)):
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
                if len(text) == 0:
                    text = anchor.contents[1]
            except:
                text = None

            # add the current anchor tag to the files list if it's a file
            if href != None:
                if "xid" in href: # It's a file
    ##                pri(anchor_tags[index], "anchor_tags[index]")
    ##                print()
                    
                    if text == None: # It's of the phugoid type
    ##                    print("\n check 1")
                        files.append([href, contents_0])
    ##                    pri(index, "index")
    ##                    pri([href, contents_0], "[href, contents_0]")
                        
                    elif text != None:
    ##                    print("\n check 2")
    ##                    pri(text, "text")
    ##                    print(f"text: {text}")
    ##                    pri([href, str(text)], "[href, str(text)]")
                        
    ##                    test_list = [""]
    ##                    test_list[0] = text
    ##                    pri(test_list, "test_list")
    ##                    pri(test_list[0], "test_list[0]")
                        
                        files.append([href, text])
    ##                    pri(index, "index")
    ##                    pri([href, text], "[href, text]")
    ##                    pri(text, "text")
                        
                    else: # It's not of the phugoid type
    ##                    print("\n check 3")
                        files.append([href, text])
    ##                    pri(index, "index")
    ##                    pri(contents_0, "contents_0")                
    ##                    pri([href, text], "[href, text]")
    ##
    ##                    pri(anchor.contents[1], "anchor.contents[1]")

    ##    pri(files, "files")

    ##    print("\n\n Outputting what files we have found")
    ##    for index in range(len(files)):
    ##        print(f"   index: {index}")
    ##        print(files[index])
    ##        print()

    ##    print(files[9][1])




    # check if file types (e.g. ".mp4") are in the file names
    if 1:
    ##    print("\n\n   Checking if there is a dot in each of the file names ...")
        
        for file in files:
            if "." not in file[1]:
                # put ".pdf" on the end of file names that don't have a dot
                file[1] = "".join([file[1], ".pdf"])

            if ".pdf" in file[1]:
                continue # if there is a pdf extension then we can go to the next file instance
                
            if file[1].count(".") > 1:
                # ask the user if we should add a .pdf extension
                while 1:
                    try:
                        print(f"\nType y or n to choose whether we should add a \".pdf\" extension to this file name: {file[1]}")
                        add_extension = input("Type y or n: ")
                        add_extension = add_extension.upper()
                        
                        if add_extension in ["Y", "N"]:
                            # the user entered a valid choice so we can exit the while loop
                            break
                        else:
                            print("\nWhat you typed was invalid")
                    except:
                        print("\nAn error of some kind ocurred. Please try again.")

                if add_extension == "Y":
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


    # download the files in the current blackboard location
    if 1:
        print("\n\n   Starting: download files")

        for file_count in range(len(files)): # for file_count in [1]: # for file_count in range(len(files)):

            file = files[file_count]

            file_name = file[1]
            file_href = file[0]

            pri(file_name, "file_name")


            file_name_split = file_name.split(".")
    ##        pri(file_name_split, "file_name_split")

            just_file_name = file_name_split[0]
            # join the split up name except for the last bit which is the file extension
            for bit in range(len(file_name_split)-2):
                # add back in the dots which are in the file name
                just_file_name = f"{just_file_name}.{file_name_split[bit+1]}"
            
            just_file_name_count = just_file_name
            file_extension = file_name_split[-1]
            

            # empty the download directory because we want to work from a clean slate
            empty_download_dir()
            
            # open the file
            driver.get(file_href)

            # see if the number of files in the download directory has increased from 0 to 1
            num_of_files = len( [ name for name in os.listdir(location_download) ] )
    ##        pri(num_of_files, "num_of_files")

            if num_of_files == 1: # we need to move this file which is in the download directory into the working directory with all the other files
                # We need to wait for the file to fully download i.e. for the file extension to stop being .tmp
    ##            print("\n check 2")
                (download_file_name, download_file_name_split) = wait_for_download(location_download)
    ##            print("\n finished waiting for download")
                
    ##            pri(download_file_name, "download_file_name")
    ##            pri(download_file_name_split, "download_file_name_split")
                

                count = 1
                while 1:
                    if not os.path.exists( f"{location_directory}\\{just_file_name_count}.{download_file_name_split[-1]}" ): # If the file doesn't already exist then:
                        # Move the file which is in the download directory into the working directory.
                            # But change the name to what blackboard gives the file while keeping the file extension the same as what it was when it was in the download
                            # directory.

                        os.rename(f"{location_download}\\{download_file_name}", f"{location_directory}\\{just_file_name_count}.{download_file_name_split[-1]}")
    ##                    copyfile(f"{location_download}\\{download_file_name}", f"{location_directory}\\{just_name_count}.{download_file_name_split[1]}")
                        break
                    else:
                        # Append a number to the file name if there is already a version of the file present.
                        just_file_name_count = f"{just_file_name} ({count})"
                        count += 1
                        
            else: # nothing went into the download directory so we need to get the url and download manually to the working directory
            
                url_now = driver.current_url # get the url
                r = requests.get(url_now, allow_redirects=True)

                count = 1
                while 1:
                    if not os.path.exists( f"{location_directory}\\{just_file_name_count}.{file_extension}" ): # If the file doesn't already exist then:
                        # Download the file to the working directory
                        open(f"{location_directory}\\{just_file_name_count}.{file_extension}", 'wb').write(r.content)
                        break
                    else:
                        # Append a number to the file name if there is already a version of the file present.
                        just_file_name_count = f"{just_file_name} ({count})"
                        count += 1
                        

        print("\n\n   Finished: downloading files")

# close the webdriver
driver.quit()









