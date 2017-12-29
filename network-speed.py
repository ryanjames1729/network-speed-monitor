import pyspeedtest, config, time
from O365 import Message
from robobrowser import RoboBrowser

def message(incoming):
        # Basic variables for authorization:
    user = "Ryan" # For shits and giggles...
    email = "rjames@altamontschool.org"
    pwd = "RJalta2017"
    auth = (email, pwd)
    # Message object:
    m = Message(auth=auth)
    # Recipients
    m.setRecipients('ryanjames1729@gmail.com')
    # Subject:
    m.setSubject('Network Speed Test')
    # Body:
    m.setBody('Good morning, Ryan.\n\n' + incoming + '\n\n -Ava')
    # Send:
    m.sendMessage()
    print("Message sent")

def formSubmit(latency, download, upload):
    br = RoboBrowser()
    br.open("https://goo.gl/forms/pZYg0m9FTfQZMNHw2")
    form = br.get_form()
    form["entry.1180755644"] = latency
    form['entry.1058068687'] = download
    form['entry.744325475'] = upload
    br.submit_form(form)

fail = 0
connect = 0

while True:
    try:
        test = pyspeedtest.SpeedTest()
        ping = test.ping()
        dl = format(test.download() / 1000000, '.2f')
        ul = format(test.upload() / 1000000, '.2f')
        formSubmit(ping, dl, ul)
        print("{}, Latency: {} s, Download: {} Mbps, Upload: {} Mbps".format(time.ctime(), ping, dl, ul))
        if float(dl) < 5 and fail < 2:
            fail += 1
        elif float(dl) < 5 and fail >= 2:
            fail = 0
            message("Latency: {} s, Download: {} Mbps, Upload: {} Mbps".format(ping, dl, ul))
            time.sleep(60*15)
        else:
            fail = 0
            time.sleep(60*15)
    except:
        print("No Connection")
        connect += 1
        if connect >= 2:
            connect = 0
            message("Could not get a connection. Trying again in 15 minutes.")
