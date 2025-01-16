import os
import webbrowser

from env import WEB_URL

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

if os.name == 'nt':
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
else:
    chrome_path = '/usr/bin/google-chrome %s'


class Web:
    def __init__(self):
        self.url = WEB_URL
        self.chrome = chrome_path

    def open(self):
        webbrowser.get(self.chrome).open(self.url)