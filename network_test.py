import socket
import speedtest
import time
import subprocess
import sys

class Network_Test:
    def __init__(self):
        print("Testing your Network...")
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii")
        results = results.replace("\r","")
        ls = results.split("\n")
        ls = ls[4:]
        ssids = []
        x = 0
        while x < len(ls):
            if x % 5 == 0:
                ssids.append(ls[x])
            x += 1
        print(ssids)
        try:
            self.ip = socket.gethostbyname(socket.gethostname())
            self.speedtester = speedtest.Speedtest()
            self.speedtester.get_best_server()
            self.download_speed = self.speedtester.download()
            self.upload_speed = self.speedtester.upload()
            self.get_results()
        except:
            print("No internet connection")

    def get_results(self):
            print("IP Address: "+self.ip)
            print("Download Speed: "+str(self.download_speed))
            print("Upload Speed: "+str(self.upload_speed))

nt = Network_Test()
k=input("press any key to exit: ")
if k == e:
    sys.exit()
else:
    sys.exit()
