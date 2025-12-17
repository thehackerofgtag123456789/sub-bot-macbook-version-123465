"""
author : mighty ghost hack - https://www.youtube.com/TTSD3XXY
Note : Modified to work on macOS (MacBook)
"""

import socket
import pyautogui
import time
import subprocess
from _thread import start_new_thread

class SubBot:

    # JavaScript code
    subButton = 'var SubForLogin = document.getElementsByClassName("style-scope ytd-subscribe-button-renderer");'
    subButtonClick = "SubForLogin[1].click();"
    bellButton = 'var Bell = document.getElementsByClassName("style-scope ytd-toggle-button-renderer");'
    bellButtonClick = "Bell[1].click();"

    # Channel URL
    url = "https://www.youtube.com/mightyghosthack"

    # macOS browser launch commands
    listOfBrowser = [
        f'open -a "Google Chrome" {url}',
        f'open -a "Firefox" {url}'
    ]

    # Console shortcut keys per browser
    # Chrome → Cmd + Option + J
    # Firefox → Cmd + Option + K
    listOfCommand = ['j', 'k']

    waitTime = 1
    flag = True
    count = 0

    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

    def enter(self, val):
        time.sleep(self.waitTime)
        pyautogui.press('enter')

    def main(self):
        while self.flag:
            time.sleep(self.waitTime + 4)

            if self.is_connected():
                for i in self.listOfBrowser:
                    start_new_thread(self.enter, (1,))

                    process = subprocess.Popen(
                        i,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True
                    )
                    process.communicate()

                    if process.returncode != 0:
                        self.count += 1
                        if self.count == len(self.listOfBrowser):
                            self.flag = False
                        continue

                    time.sleep(self.waitTime + 5)

                    # Open browser console
                    pyautogui.hotkey('command', 'option',
                        self.listOfCommand[self.listOfBrowser.index(i)]
                    )

                    time.sleep(self.waitTime + 2)

                    pyautogui.typewrite(self.subButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)

                    pyautogui.typewrite(self.subButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)

                    pyautogui.typewrite(self.bellButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)

                    pyautogui.typewrite(self.bellButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)

                    # Quit browser
                    pyautogui.hotkey('command', 'q')
                    time.sleep(self.waitTime)
                    pyautogui.press('enter')

                    self.flag = False
                    break
            else:
                print("Please connect to the Internet")

subBot = SubBot()
subBot.main()
