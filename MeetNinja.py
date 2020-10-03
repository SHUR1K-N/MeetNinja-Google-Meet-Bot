from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
import pause; import os; import re
import time; from datetime import datetime
import colorama; from termcolor import colored

colorama.init()

###################################################################
#                        Meets                 Yr  M D  Hr min sec
MEETS = {"https://meet.google.com/meetURL1": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL2": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL3": "2020 9 16 14 16 0",
         }
DURATION = 60 # Duration of each Meet in minutes
USERNAME = "emailaddress@gmail.com"
PASSWORD = "passw0rd"
BROWSER_DRIVER = "Browser Driver Path Goes Here (options below)"

#                   Google Chrome
#           Linux: "ChromeDrivers/linux64/chromedriver"
#             Mac: "ChromeDrivers/mac64/chromedriver"
#         Windows: "ChromeDrivers/win32/chromedriver.exe"

#                   Mozilla Firefox
#     Linux (x32): "FirefoxDrivers/linux32/geckodriver"
#     Linux (x64): "FirefoxDrivers/linux64/geckodriver"
#             Mac: "FirefoxDrivers/mac64/geckodriver"
#   Windows (x32): "FirefoxDrivers/win32/geckodriver.exe"
#   Windows (x64): "FirefoxDrivers/win64/geckodriver.exe"
###################################################################

# All interactive field / button locators (In rare cases in the future, you may have to change these locators in case Google updates them internally)
usernameFieldPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
nextButtonPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
passwordFieldPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
dismissButtonPath = "/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span/span"
xButtonPath = "#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.B2Jb7d.Up8vH.hFEqNb.J9Nfi.iWO5td > div.R6Lfte.es33Kc.TNczib.X1clqd > div.bZWIgd > div > span > span > svg"
joinButtonPath = "//span[contains(text(), 'Join now')]"
endButtonPath = "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div"

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
    timeNow = str(datetime.now())
    timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeNow)
    return(timeRegEx[0])


def initBrowser():
    print("\nInitializing browser...", end="")
    if BROWSER_DRIVER.lower().startswith("chrome"):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--disable-infobars")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--window-size=800,800")
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                        "profile.default_content_setting_values.media_stream_camera": 2,
                                                        "profile.default_content_setting_values.notifications": 2
                                                        })
        driver = webdriver.Chrome(executable_path=BROWSER_DRIVER, options=chromeOptions)

    elif BROWSER_DRIVER.lower().startswith("firefox"):
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument("--width=800"), firefoxOptions.add_argument("--height=800")
        # firefoxOptions.headless = True
        firefoxOptions.set_preference("layers.acceleration.disabled", True)
        firefoxOptions.set_preference("browser.privatebrowsing.autostart", True)
        firefoxOptions.set_preference("permissions.default.microphone", 2)
        firefoxOptions.set_preference("permissions.default.camera", 2)
        driver = webdriver.Firefox(executable_path=BROWSER_DRIVER, options=firefoxOptions)
    print(colored(" Success!", "green"))
    return(driver)


def login():
    print("Logging into Google account...", end="")
    driver.get('https://accounts.google.com/signin')

    username = wait.until(when.element_to_be_clickable((by.XPATH, usernameFieldPath)))
    time.sleep(1)
    username.send_keys(USERNAME)

    nextButton = wait.until(when.element_to_be_clickable((by.XPATH, nextButtonPath)))
    nextButton.click()

    password = wait.until(when.element_to_be_clickable((by.XPATH, passwordFieldPath)))
    time.sleep(1)
    password.send_keys(PASSWORD)

    nextButton = wait.until(when.element_to_be_clickable((by.XPATH, nextButtonPath)))
    nextButton.click()
    time.sleep(3)
    print(colored(" Success!", "green"))


def attendMeet():
    print(f"\n\nNavigating to Google Meet #{meetIndex}...", end="")
    driver.get(URL)
    print(colored(" Success!", "green"))
    print(f"Entering Google Meet #{meetIndex}...", end="")

    if BROWSER_DRIVER.lower().startswith("chrome"):
        try:
            dismissButton = wait.until(when.element_to_be_clickable((by.XPATH, dismissButtonPath)))
            time.sleep(1)
            dismissButton.click()
            skipFlag = True
        except:
            skipFlag = False
        if (skipFlag is False):
            try:
                xButton = wait.until(when.element_to_be_clickable((by.CSS_SELECTOR, xButtonPath)))
                time.sleep(1)
                xButton.click()
            except:
                pass

    joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButtonPath)))
    time.sleep(1)
    joinButton.click()
    print(colored(" Success!", "green"))
    time.sleep(1)
    print(colored(f"Now attending Google Meet #{meetIndex} @{timeStamp()}", "green"), end="")


def endMeet():
    endButton = driver.find_element_by_xpath(endButtonPath)
    endButton.click()
    print(colored(f"\nSuccessfully ended Google Meet #{meetIndex} @{timeStamp()}\n", "red"), end="")


def genericError():
    # clrscr()
    print(colored(" Failed!", "red"), end="")
    print("\n\nPossible fixes:\n")
    print("1.1 Check your inputs and run MeetNinja again (make sure there are no leading zeros in the Meet start times)")
    print("1.2 And / Or make sure you have chosen the correct webdriver file respective of your web browser and operating system")
    print("2. Make sure the generated web browser is not \"Minimized\" while MeetNinja is working")
    print("3.1. Make sure the webdriver file is of the latest stable build (https://chromedriver.chromium.org/ or https://github.com/mozilla/geckodriver/releases)")
    print("3.2. And / Or make sure your chosen web browser is updated to the latest version")
    print("3.3. And / Or make sure the webdriver file is at least of the same version as your chosen web browser (or lower)")
    print("4. Make sure the small \"time.sleep()\" delays (in seconds) in the functions are comfortable for your internet speed")
    print("5. Make sure your internet connection is stable throughout the process")
    print("\nPress Enter to exit.")
    input()
    try:
        driver.quit()
    except:
        pass


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
        wait = webdriver.support.ui.WebDriverWait(driver, 5)
        for meetIndex, (URL, startTime) in enumerate(MEETS.items(), start=1):
            startTime = list(map(int, startTime.split()))
            if (meetIndex <= 1):
                print(colored(f"Waiting until first Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...", "yellow"), end="")
            else:
                print(colored(f"\n\nWaiting until next Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...", "yellow"), end="")
            pause.until(datetime(*startTime))
            print(colored(" Started!", "green"))
            if (meetIndex <= 1):
                login()
            attendMeet()
            time.sleep(DURATION)
            endMeet()
        print("\n\nAll Meets completed successfully.")
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()

    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()
    except:
        # print(e)
        genericError()
