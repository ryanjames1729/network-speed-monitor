import pyspeedtest
import config.py

def message(incoming):
        # Basic variables for authorization:
    user = "Ryan" # For shits and giggles...
    email = config.CODINGBAT_USERNAME
    pwd = config.OUTLOOK_PASSWORD
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



test = pyspeedtest.SpeedTest()
ping = test.ping()
dl = format(test.download() / 1000000, '.2f')
ul = format(test.upload() / 1000000, '.2f')
print("Latency: {} s, Download: {} Mbps, Upload: {} Mbps".format(ping, dl, ul))
if float(dl) < 20:
    message("Latency: {} s, Download: {} Mbps, Upload: {} Mbps".format(ping, dl, ul))
