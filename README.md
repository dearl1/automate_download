# automate_download  

This code uses selenium to open a webdriver instance of the blackboard homepage.  
You can change the user_name variable to your username because the code is able to find the username input box on the webpage and already input it for you.  
But you will need to manually enter your password for security reasons.  

After entering your password click ok on the cookies pop-up.
Then navigate to the module folder in blackboard from which you want to download the folders.  
Then type d for download in the python shell.  

The variable root_location_directory defines whereabouts in your computer the files will be downloaded to.  
You can navigate to another location in your blackboard site and download more files or type quit.