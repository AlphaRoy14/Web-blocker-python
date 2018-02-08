import time
from datetime import datetime as dt
host_path="/etc/hosts"
host_temp="hosts.txt"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,13) : #we are comparing dt objects as we cannot compare time directly
        print("Working hours")
        with open(host_path,'r+') as file: #r+ appends , had we only put 'r' then it would write from the beginning in the empty file
            content=file.read()
            for website in website_list:       #to check if the website already exist in the host time , if it does we dont do anything
                if website in content:
                    pass
                else:
                    file.write(redirect+' ' + website + '\n')
    else:
        print("Fun hours")
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0) #sets the file poointer to the beginning of the file
            for line in content:

                if not any(website in line for website in website_list ) : #ya python is english

                    file.write(line)
            file.truncate() #deletes the file or the rest of the file from the current position
                                        #can use file.tell() to find out the current position

    time.sleep(5)
