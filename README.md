# Youtube Downloader
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![License](https://img.shields.io/github/license/daniel071/Youtube_Downloader)

## The Open Source Youtube Downloader!

### Screenshots:
#### How the current GUI looks:
![Screenshot 1](https://raw.githubusercontent.com/daniel071/images-for-readme/master/Screenshot%20from%202020-02-03%2019-10-01.png)
#### Debug commands are outputted to the command line:
![Screenshot 2](https://raw.githubusercontent.com/daniel071/images-for-readme/master/Screenshot%20from%202020-02-03%2019-10-33.png)

### Why I made this:
Most online Youtube to MP3 converters are filled with intrusive advertisements and popups, some even contain malware. I made this using the youtube_dl python package to download videos from online.

### How you can help:
 There are 3 easy steps to contributing to this project:
 1. Create a fork of this project
 1. Make modifications to the fork
 1. Open a pull request in this repository, with your new fork selected

Find this in more detail [here](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork)

### How to install:
This application is able to be used on multiple operating systems, find the installation instructions for your operating system here:
###### **Please note:** I've only tested this on Windows 10 and Linux! Other operating systems such as MacOS and FreeBSD should work, but compatibility is not guaranteed
#### On Windows 7/8.1/10
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg" alt="Windows 10 Logo" width="150"/> <img src="https://upload.wikimedia.org/wikipedia/en/1/14/Windows_logo_-_2006.svg" alt="Windows 7 Logo" width="150"/>  
Youtube Downloader uses a virtual environment so all the packages come pre-installed,
the following steps are:

1. Go to releases and download the latest version of Youtube Downloader
   Found here: https://github.com/daniel071/Youtube_Downloader/releases
   
2. Extract the zipped folder
  
3. Open up the BAT file named 'StartGUI.bat' to start the GUI interface for this program. If you only want command-line, you can open 'StartProgram.bat'

4. Input the URL link to the youtube video, any metadata for it and where you'd like to save it (The program will create a file inside the directory you chose)
---
#### On Unix based operating systems (Linux, MacOS, FreeBSD)
<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" alt="Linux Logo" width="150"/> <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/MacOS_logo_%282017%29.svg" alt="MacOS Logo" width="150"/>
##### Automated installation:
1. Go into your terminal and cd into the git directory

2. Run
```bash
source _StartGUI.sh
```

###### **Note:** This command requires root permissions as the command `sudo pip3 install -r requirements.txt --upgrade` requires root permissions!

3. Enjoy!

##### Manual installation
1. Go into your terminal and cd into the git directory

2. Run the following commands
```bash
# Initialises the virtualenv
source /venv/bin/activate

# Installs required dependacies
sudo pip3 install -r requirements.txt --upgrade

# Runs the program
python3 "Youtube Downloader GUI.py"
```

### Troubleshooting

#### Dependency issues
If the python program is failing to start due to packages not being installed try the following:
1. Make sure you are in the virtual environment  
 #### On Windows:
  Open command promt in the git directory and run  
  ```CALL venv\Scripts\activate.bat```
  
 #### On Linux/MacOS/FreeBSD:
  Open terminal in the git directory and run  
  ```source /venv/bin/activate```
  
<br></br>
2. Install required dependacies
 For both Windows and Linux/MacOS/FreeBSD, try running this in your terminal/command prompt: <br></br>
 ```sudo pip3 install -r requirements.txt --upgrade```
<br></br>
If it still doesn't work, feel free to open up an issue


> Contributed by Daniel Pavela
