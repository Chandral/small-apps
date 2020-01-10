from datetime import datetime as dt
import time

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
site_list = ["www.twitter.com", "www.facebook.com"]

while True:
    if (dt.now().hour >= 10) and (dt.now().hour <= 18):
        print("Working")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in site_list:
                if site in content:
                    continue
                else:
                    file.write(redirect + ' ' + site + '\n')
    else:
        print("Happy Hours")
    time.sleep(5)
