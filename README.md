# Phase 1 - Uploading the Plugin 

1.	Install an Environment ActiveGate (Windows)

2.	Install Python on the ActiveGate
    a. https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
    b. Ensure you have selected to `Add python 3.6 to PATH` during install 
    c. Verify the install worked, and that pip is installed by typing `pip` into the command line 
    
3.	Install the Dynatrace Plugin SDK
    a.	https://www.dynatrace.com/support/help/extend-dynatrace/plugins/activegate-plugins/development/activegate-plugin-sdk-overview/
    
4.	Create a new folder within the SDK and call it something like `Live Plugins`

5.	Create a folder in your new folder called NYSE Plugin 

6.	Move the Python and JSON files from this repository into that folder 

7.	Open the Python file using IDLE and see if it runs (it wont) 
    a.	Install the dependencies, and take note of what you installed, you will need these later 
    b.	Yfinance
    c.	logger
    d.  pandas==1.0.1
    e.	Run the python file, it should now work. Do not proceed if the plugin does not run in IDLE. 
    
8.	In the CLI, navigate to the folder where the JSON and Python are

9.	Run the following command to build the plugin and push the files to the correct place on the ActiveGate and the Dynatrace tenant 
    a.	Plugin_sdk build_plugin
    
10.	Enter ‘n’ when asked if you have a token file, then enter your API token

11.	Check the response to see if the plugin has been uploaded successfully, if this was successful you will be able to see the plugin in the Dynatrace UI 

12.	Try and connect to the ActiveGate Endpoint via the Dynatrace UI. If this does not work, you will see an errror message  

# Phase 2 - Reviewing what we have done 





# Phase 3 - Cleaning up the Plugin 




