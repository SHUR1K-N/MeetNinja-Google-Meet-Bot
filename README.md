# MeetNinja: The Google Meet Bot

## Description
A super dope tool that attends your Google Meet(s) for you on autopilot while you sleep or work on something else. MeetNinja flawlessly handles multiple Meet sessions, background activity, scheduling, and also disables your Meet camera & microphone in-Meet! It is also equipped with color-coded, concise activity logging (verbose) with timestamps of all joining & ending activities for each Meet session (to assure you—upon your return—that your Meets were *indeed* successfully attended).

<div align="center">
<img src="https://github.com/SHUR1K-N/MeetNinja-Google-Meet-Bot/blob/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for the fellow comrades and homies.

## Features
- Mulitple Meet sessions supported, according to the user-defined Meet schedule
- Works even with the display on sleep (and does not wake it up either)
- Works even in the background while you do other work (as long as you do not *explicitly* "Minimize" the Chrome window MeetNinja generates; just keep it open in the background, beneath your current open window(s))
- Automatically disables camera & microphone in-Meet
- Color-coded & concise activity logging (verbose) with timestamps of all activities

## Usage
1. Clone / Download this repository or its content (mainly **MeetNinja.py** and the **chromedriver** file for your OS)

2. PIP-install all the packages mentioned under the [last subheading](https://github.com/SHUR1K-N/MeetNinja-Google-Meet-Bot#dependencies-to-pip-install "last subheading") on this page

3. Do not run MeetNinja.py just yet. First, open it using any editor, and substitute your inputs (Google Meet URLs, their start times, duration of all Meets, Google username, and password) into the dummy values in the following section of the code (highlighted):

<div align="center">
<img src="https://github.com/SHUR1K-N/MeetNinja-Google-Meet-Bot/blob/master/Images/Substitute.png" >
<p>Values to Substitute</p>
</div>

4. Save your changes, and run the program (either by double-clicking MeetNinja.py, or executing it via a terminal window if you are feeling particularly geeky today)

5. Take the chillest of pills (figuratively) and abandon all your worries; MeetNinja's got your back

### What MeetNinja Does
Upon execution, MeetNinja generates a new Google Chrome window in Developer Mode, and this new window stays idle until it is time to join your first Meet (according to your schedule). Once it is time, MeetNinja automatically logs you into your Google account, navigates to the first Meet URL, disables your camera & microphone, joins the Meet session, and then waits until the duration specified (60 minutes by default) before ending the call and repeating the same for the *next* Meet session (whenever it may be) and so on, until your schedule has exhausted *(phew)* — all this with just a single (double) click!

## Tip(s) for CyberJedi-like Usage
### Wake-on-LAN
You may use MeetNinja paired with Wake-on-LAN / Magic Packet (if your motherboard and network adapter support it) for the optimal, ultimate "Away From Keyboard" automation experience.

You would be surprised by how common a feature WoL is in most modern *and* semi-modern systems. Hence, definitely *do* check it out. It is super cool, convenient, easy, helpful, and—importantly—native.

I highly recommend [**this Android app**](https://play.google.com/store/apps/details?id=co.uk.mrwebb.wakeonlan "this Android app") (ad-free, free, light, simple) for sending WoL packets to your computer system over the air and triggering a wake-up from the Hibernation / Sleep state without even touching the system (ironic how you would wake your system up so you could sleep, hah!).

### Chrome Remote Desktop / Microsoft's RD Client
You may also need or use the above remote desktop client(s) if you need to mid-sleep-check on your progress or if your computer system has a login password you may need to enter remotely after a Wake-on-LAN.

## Note
1. Make sure you do not close the generated Chrome window until all your Meets are attended

2. Make sure you do not input the start time with leading zeros like `08 30` (Eight Thirty AM). The correct format is simply `8 30`. This, however, does not apply to zero by itself, so `8 0` (Eight AM) would work just fine

3. You may abort the process at any stage or time by pressing CTRL + C from within the MeetNinja console / terminal window

## Dependencies to PIP-Install
- **selenium** (for Chrome-based automation)
- **datetime** (for scheduling & timestamps)
- **pause** (for scheduling)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
