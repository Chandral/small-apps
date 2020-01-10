from datetime import datetime as dt
import time

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
site_list = ["www.twitter.com", "www.facebook.com"]

while True:
    if (dt.now().hour >= 10) and (dt.now().hour <= 18):
        print("Working")
    else:
        print("Happy Hours")
    time.sleep(5)
