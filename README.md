# Phase 1 - Uploading the Plugin 

1.	Install an Environment ActiveGate (Windows)

2.	Install Python on the ActiveGate host
    - https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
    - Ensure you have selected to `Add python 3.6 to PATH` during install 
    - Verify the install worked, and that pip is installed by typing `pip` into the command line 
    
3.	Install the Dynatrace Plugin SDK
    -	https://www.dynatrace.com/support/help/extend-dynatrace/plugins/activegate-plugins/development/activegate-plugin-sdk-overview/
    
4.	Create a new folder within the SDK and call it something like `Live Plugins`

5.	Create a folder in your new folder called NYSE Plugin 
	- Versioning is important, you cannot update a plugin with the same version name, so you may want to include the version in this folder name. Check the JSON file in this repository for the version.

6.	Move the Python and JSON files from this repository into that folder 

7.	Right click and open the Python file using IDLE and see if it runs (it wont) 
    -	Install the dependencies via the windows command prompt, use https://pypi.org/ to find the install commands. Take note of what you have installed, you will need to reference these later. An 
    -	`Yfinance`
    -  `pandas==1.0.1`
    -	Run the python file, it should now work. Do not proceed if the plugin does not run in IDLE 
    
8.	In the windows CLI, navigate to the folder where the JSON and Python are 

9.	Run the following command as Admin to build the plugin and push the files to the correct directory on the ActiveGate and the Dynatrace tenant 
    -	`Plugin_sdk build_plugin`
    
10.	Enter ‘n’ when asked if you have a token file, then enter your API token
    - If you have not done so already, create an API token and esure you have the correct permissions to push the plugin to the cluster 
	
11.	Check the response to see if the plugin has been uploaded successfully, if this was successful you will be able to see the plugin in the Dynatrace UI via Settings - Monitored Technologies - Custom Extentions

12.	Click on the Plugin in the Dynatrace UI and try to connect to the ActiveGate Endpoint. If this does not work, you will see an errror message, and you will need to troubleshoot by looking in the logs to see what went wrong. 
	- Logs can be found in `C:\ProgramData\dynatrace\remotepluginmodule\log\remoteplugin`
	- Look for the `ruxitagent_remotepluginagent_[PID].0.log` for the word `severe`

13.    If this was successfull you will be able to see metrics via the Technologies tab, look out for one called CustomPluginTechnology 

# Phase 2 - Reviewing what we have done 





# Phase 3 - Cleaning up the Plugin 




