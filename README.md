# MeetNinja: Google Meet Bot

## Description
A super dope tool that attends your Google Meet(s) for you on autopilot while you sleep or work on something else. MeetNinja flawlessly handles multiple Meet sessions, background activity, scheduling, and also disables your Meet camera and microphone in-Meet! It is also equipped with color-coded, concise activity logging (verbose) with timestamps of all joining and ending activities for each Meet session (to assure you—upon your return—that your Meets were *indeed* successfully attended). Supports Google Chrome and Mozilla Firefox, on Linux, Mac, and Windows.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/MeetNinja-Google-Meet-Bot/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for the fellow comrades and homies.

## Features
- Multiple Meet sessions supported, according to the user-defined Meet schedule
- Works even with the display on sleep (and will not wake it up either)
- Works even in the background while you do other work (as long as you do not *explicitly* "Minimize" the browser window MeetNinja generates; just keep it open in the background, beneath your current open window(s))
- Automatically disables camera and microphone in-Meet
- Color-coded and concise activity logging (verbose) with timestamps of all activities
- Supported web browsers: Google Chrome and Mozilla Firefox
- Supported platforms: Linux, Mac, and Windows
- Automatically checks for a newer MeetNinja version upon every execution

## Usage
1. Clone this repository or download it as a ZIP file (and extract its contents)

2. PIP-install all the packages mentioned under the [last subheading](https://github.com/SHUR1K-N/MeetNinja-Google-Meet-Bot#dependencies-to-pip-install "last subheading") on this page, either automatically via running the `pip install -r requirements.txt` command, or manually via separate `pip install` commands for each package

3. Do not run MeetNinja.py just yet. First, open it using any editor, and substitute your inputs (Google Meet URLs, their start times, duration of all Meets, Google username, password, path to the web driver file of your respective browser and OS) into the dummy values in the following section of the code (highlighted):

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/MeetNinja-Google-Meet-Bot/master/Images/Substitute.png" >
<p>Values to Substitute</p>
</div>

4. Save your changes, and run the program (either by double-clicking MeetNinja.py, or executing it via a terminal window if you are feeling particularly geeky today)

5. Take the chillest of pills (figuratively) and abandon all your worries; MeetNinja's got your back

### What MeetNinja Does
Upon execution, MeetNinja generates a new Google Chrome / Mozilla Firefox window in Developer Mode, and this new window stays idle until it is time to join your first Meet (according to your schedule). Once it is time, MeetNinja automatically logs you into your Google account, navigates to the first Meet URL, disables your camera and microphone, joins the Meet session, and then waits until the duration specified (60 minutes by default) before ending the call and repeating the same for the *next* Meet session (whenever it may be) and so on, until your schedule has exhausted *(phew)* — all this with just a single (double) click!

## Tip(s) for CyberJedi-like Usage
### Wake-on-LAN
You may use MeetNinja paired with Wake-on-LAN / Magic Packet (if your motherboard and network adapter support it) for the optimal, ultimate "Away From Keyboard" automation experience.

You would be surprised by how common a feature WoL is in most modern *and* semi-modern systems. Hence, definitely *do* check it out. It is super cool, convenient, easy, helpful, and—importantly—native.

I highly recommend [**this Android app**](https://play.google.com/store/apps/details?id=co.uk.mrwebb.wakeonlan "this Android app") (ad-free, free, light, simple) for sending WoL packets to your computer system over the air and triggering a wake-up from the Hibernation / Sleep state without even touching the system (ironic how you would wake your system up so you could sleep, hah!).

### Chrome Remote Desktop / Microsoft's RD Client
You may also need or use the above remote desktop client(s) if you need to mid-sleep-check on your progress or if your computer system has a login password you may need to enter remotely after a Wake-on-LAN.

## Note
1. MeetNinja works even in the background while you do other work on other windows, as long as you **do not *explicitly* "Minimize" MeetNinja's generated browser window**; just keep it open in the background, beneath your current open window(s)

2. There is *deliberately* no Headless Mode (at the moment) due to potential complications arising from exiting MeetNinja while a Meet is still active (such as the Meet not relatively "naturally" ending and you being a part of the Meet unknowingly till the end of time)

3. Although you may abort the process at any stage or time by pressing CTRL + C from within the MeetNinja console / terminal window, it is not advised to do so from within an active Meet (for reasons similar to the previous point)

4. There is *deliberately* no audio output muting due to potential situations such as roll-calls or surprise questions for which you may need to intervene unexpectedly. Besides, you can either mute the tab manually if you are working on something else; or just entirely mute your system if you are planning on sleeping anyway

## Dependencies to PIP-Install
- **selenium** (for web browser-based automation)
- **requests** (for automatic update checks)
- **datetime** (for scheduling & timestamps)
- **pause** (for scheduling)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
