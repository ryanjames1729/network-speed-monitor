# network-speed-monitor

After getting tired of monitoring my intermittent Internet service through ATT, I wrote this Python script to monitor it for me.

It collects the latency, download speed, and upload speed every 15 minutes and logs the data in an Google Sheets document via Google Forms and Robobrowser. If the program can't connect to the network or does not get a sufficient speed 3 times in a row (with no wait period), the program will send me an e-mail to notify me.
