from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time; import pause; import pyautogui
import os; from datetime import datetime
from termcolor import colored
import colorama; import re

colorama.init()

CHROMEDRIVER = "chromedriver.exe"
xButton = "Buttons/xButton.png"
joinButton = "Buttons/joinButton.png"
endButton = "Buttons/endButton.png"

##################################################################
#                        Meets                 Yr  M D  Hr min sec
MEETS = {"https://meet.google.com/meetURL1": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL2": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL3": "2020 9 16 14 16 0",
         }
DURATION = 60 # Duration of each Meet in minutes
USERNAME = "emailaddress@gmail.com"
PASSWORD = "passw0rd"
##################################################################

BANNER1 = colored('''
                     ███▄ ▄███▓▓█████ ▓█████▄▄▄█████▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                    ▓██▒▀█▀ ██▒▓█   ▀ ▓█   ▀▓  ██▒ ▓▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ▓██    ▓██░▒███   ▒███  ▒ ▓██░ ▒░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ▒██    ▒██ ▒▓█  ▄ ▒▓█  ▄░ ▓██▓ ░ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ▒██▒   ░██▒░▒████▒░▒████▒ ▒██▒ ░ ▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                    ░ ▒░   ░  ░░░ ▒░ ░░░ ▒░ ░ ▒ ░░   ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                    ░  ░      ░ ░ ░  ░ ░ ░  ░   ░    ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                    ░      ░      ░      ░    ░         ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                           ░      ░  ░   ░  ░                 ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                                         MeetNinja: The Google Meet Bot''', 'red')
BANNER3 = colored('''                                        --------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


def timeStamp():
    timeNow = datetime.now()
    timeString = str(timeNow)
    timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeString)
    return(timeRegEx[0])


def initBrowser():
    print("\nInitializing browser...", end="")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--window-size=800,800")
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                    "profile.default_content_setting_values.media_stream_camera": 2,
                                                    "profile.default_content_setting_values.notifications": 2
                                                    })
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=chromeOptions)
    print(colored(" Success!", "green"))
    return(driver)


def login():
    print("Logging into Google account...", end="")
    driver.get('https://accounts.google.com/signin')

    username = driver.find_element_by_id("identifierId")
    username.send_keys(USERNAME)

    nextButton = driver.find_element_by_id("identifierNext")
    nextButton.click()
    time.sleep(3)

    password = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(PASSWORD)

    signInButton = driver.find_element_by_id("passwordNext")
    signInButton.click()
    time.sleep(3)
    print(colored(" Success!", "green"))


def attendMeet():
    print(f"\n\nNavigating to Google Meet #{meetIndex}...", end="")
    driver.get(URL)
    print(colored(" Success!", "green"))
    print(f"Entering Google Meet #{meetIndex}... ", end="")
    time.sleep(3)

    try:
        buttonX, buttonY = pyautogui.locateCenterOnScreen(xButton)
        pyautogui.click(buttonX, buttonY)
        time.sleep(2)
    except:
        pass

    buttonX, buttonY = pyautogui.locateCenterOnScreen(joinButton)
    pyautogui.click(buttonX, buttonY)
    print(colored(" Success!", "green"))
    time.sleep(1.5)
    print(colored(f"Now attending Google Meet #{meetIndex} @{timeStamp()}", "green"), end="")


def endMeet():
    buttonX, buttonY = pyautogui.locateCenterOnScreen(endButton)
    pyautogui.click(buttonX, buttonY)
    print(colored(f"\nSuccessfully ended Google Meet #{meetIndex} @{timeStamp()}", "red"), end="")


def genericError():
    clrscr()
    print("\nSomething went wrong. Possible fixes:\n")
    print("1. Check your inputs and run MeetNinja again")
    print("2. Make sure the developer browser is always open while MeetNinja is working")
    print("3. Make sure \"chromedriver.exe\" is of the latest stable build (https://chromedriver.chromium.org/)")
    print("4. Make sure the small \"time.sleep\" delays in the functions are comfortable for your internet speed")
    print("\nPress Enter to exit.")
    input()


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:
        DURATION *= 60
        driver = initBrowser()
        print("Waiting until Meet start time...", end="")
        for meetIndex, (URL, startTime) in enumerate(MEETS.items(), start=1):
            startTime = list(map(int, startTime.split()))
            pause.until(datetime(*startTime))
            if (meetIndex <= 1):
                print(colored(" Started!", "green"))
                login()
            attendMeet()
            time.sleep(DURATION)
            endMeet()
    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
    except:
        genericError()
    print("\n\nAll Meets completed successfully.")
    print("Press Enter to exit.")
    input()
