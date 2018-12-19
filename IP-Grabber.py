#from bs4 import BeautifulSoup
import requests
import socket
import time

print(" Example: TargetSite.com")
target = input("target site: ")

target_full_url = "http://" + target + "/"
print("testing connection to: ", target_full_url)
r = requests.get(target_full_url)

if r.status_code is 200:
    print("\n[*] Connection sucessful\n")

    print("\n [?] Getting Internet protocol address (ip)... ")
    ip = socket.gethostbyname(target)

    print("###############################################")
    print("# Internet protocol address: ", "|", ip, "#")
    print("###############################################")
    print("\n [!] Program finished")
    time.sleep(10)

else:
    print("\n [!] could not connect to: ", target_full_url)
    
    print("\n [!] Program finished")
