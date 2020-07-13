# Created by Gourav Ranjan Dutta. Updated by Jordan Leich on 7/13/2020
# REQUIREMENTS - requests (pip install requests) and colored (pip install colored)

# Imports
import hashlib
import os
import time
import requests
from colored import fg, attr

# Colors used
good_color = fg('green')
bad_color = fg('red')
reset = attr('reset')

file_list = list()
root_dir = input("Enter the directory location where you want to search for viruses: ")
print()
time.sleep(1)


def scan():
    for i in range(5):
        print(". ")
        time.sleep(0.500)

    infected_list = []
    for f in file_list:
        vdef = open("viruses.txt", "r")
        file_not_read = False
        print(good_color + "\n scanning... : {}".format(f))
        hs = hashlib.sha256()
        try:
            with open(f, "rb") as file:
                try:
                    buf = file.read()
                    file_not_read = True
                    hs.update(buf)
                    file_hashed = format(hs.hexdigest())
                    print(good_color + "File scanned successfully :{}".format(file_hashed))
                    apikey = "9d38604e105e8682bdb7b4d4f30fdfa19ad3df7f32a15146122ec21f32e7e0ec"

                    url = 'https://www.virustotal.com/vtapi/v2/file/report'

                    params = {'apikey': apikey, 'resource': file_hashed}

                    response = requests.get(url, params=params)
                    #                     print(response.json())
                    res_json = response.json()

                    if res_json['positives'] >= 5:
                        print()
                        print(bad_color + "Malware Detected --> file name: {}".format(f), '\n')
                        infected_list.append(f)
                except Exception as e:
                    print(bad_color + " Oops!! Could not read the file: {}".format(e))
        except:
            pass
    if len(infected_list) == 0:
        print(good_color + "Your folder is clear...")
    else:
        print(bad_color + "Infected files found : {}".format(infected_list))
        de = str(input("Would you like to delete the infected files (yes or no) "))
        print()
        if de.lower() == 'yes' or de.lower() == 'y':
            for infected in infected_list:
                os.remove(infected)
                print(good_color + "file removed : {}".format(infected))
            print()
            print(good_color + "Your folder is now clean!\n")
            time.sleep(2)
            print(good_color + "Thank you for using this Antivirus!\n")
            time.sleep(2)
            quit()
        else:
            print(good_color + "Thank you for using this Antivirus!\n")
            time.sleep(2)
            quit()


print(good_color + "Starting Scan", end="")
for i in range(5):
    print(".", end="")
    time.sleep(0.500)
print()
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # file_path=subdir + os.sep+file
        file_path = os.path.join(subdir, file)
        print(file_path)
        if file_path.endswith(".exe") or file_path.endswith(".dll") or file_path.endswith(".com")\
                or file_path.endswith(".zip"):
            file_list.append(file_path)

if len(file_list) == 0:
    print()
    print(good_color + "Your folder is clean!\n")
    time.sleep(2)
    quit()

else:
    print()
    print(bad_color + "We found some files that could be a virus!\n")
    time.sleep(2)
    print(good_color + "Starting file scan...")
    time.sleep(2)
    scan()
