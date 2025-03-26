![Alt text](/img/icon.png?raw=true "Falcon Sandbox API Icon")

# VxWebService Python API Connector
This tool is a fork of the master repository VxAPI, designed to parse API responses efficiently. It requires users to provide:
- A valid API key
- A text file containing a list of hashes

After scanning the hashes, the tool processes the results and saves them in a structured JSON file for facilitate analysis and integration.

## How to Use
### Requirements

- [Python](http://www.python.org) >= 3.4.0

> To install the required python modules, please run `pip install -r requirements.txt`
> Using Debian/Ubuntu OS, this can be done by calling `sudo apt-get install python3-pip`. It will then be available via `pip3`
> Using Windows, this can be done automatically when installing `python` (proper checkbox on the installer has to be checked). It should be available via `pip` 

### Example
Below command is an example of execution the tool:
```
python.exe .\run.py -f .\hash.txt -k <API Key>
```
### License

Licensed  GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
see https://github.com/PayloadSecurity/VxAPI/blob/master/LICENSE.md
