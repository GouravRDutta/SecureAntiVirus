import hashlib
import os
import time

import requests

file_list = list()
root_dir = input("Enter the directory location where you want to search for viruses \n")


def scan():
    for i in range(5):
        print(". ")
        time.sleep(0.500)

    infected_list = []
    for f in file_list:
        vdef = open("viruses.txt", "r")
        file_not_read = False
        print("\n scanning... : {}".format(f))
        hs = hashlib.sha256()
        try:
            with open(f, "rb") as file:
                try:
                    buf = file.read()
                    file_not_read = True
                    hs.update(buf)
                    file_hashed = format(hs.hexdigest())
                    print("file md5 Done:{}".format(file_hashed))
                    apikey = "9d38604e105e8682bdb7b4d4f30fdfa19ad3df7f32a15146122ec21f32e7e0ec"

                    url = 'https://www.virustotal.com/vtapi/v2/file/report'

                    params = {'apikey': apikey, 'resource': file_hashed}

                    response = requests.get(url, params=params)
                    #                     print(response.json())
                    res_json = response.json()

                    if res_json['positives'] >= 5:
                        print("Malware Detected --> file name: {}".format(f))
                        infected_list.append(f)
                except Exception as e:
                    print(" Oops!! Could not read the file: {}".format(e))
        except:
            pass
    if len(infected_list) == 0:
        print(" Your folder is clear ...")
    else:
        print("Infected files found : {}".format(infected_list))
        de = str(input("would you like to delete the infected files(y/n) "))
        if de.upper() == 'Y':
            for infected in infected_list:
                os.remove(infected)
                print("file removed : {}".format(infected))
            print("Your folder is clean ")
            print("Thank you for using this Antivirus ")
        else:
            print("Thank you for using this Antivirus ")
            os.system("PAUSE")


print("Starting Scan", end="")
for i in range(5):
    print(".", end="")
    time.sleep(0.500)
print()
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # file_path=subdir + os.sep+file
        file_path = os.path.join(subdir, file)
        print(file_path)
        if (file_path.endswith(".exe") or file_path.endswith(".dll") or file_path.endswith(".com")):
            file_list.append(file_path)
if len(file_list) == 0:
    print("Your folder is clean ")
    os.system("PAUSE")
else:

    print("We found some files that could be virus ")
    print("Starting file scan")

    scan()
