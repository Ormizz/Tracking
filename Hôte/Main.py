"""
Auteur     :
Version    :
Date        :
Description :
"""

#importation des modules
import urllib.request
import json
import time
import socket
from datetime import datetime
from notifypy import Notify


#boucle infini qui surveille la connexion du user
def main():
   
    lu= True

    while True:
        try:
            urllib.request.urlopen('http://google.com')
           
            # ip = socket.gethostbyname(socket.gethostname()) #get ip de la connexion 
            
            
            if lu :
                notifier() 
                time.sleep(2)
                lecture()
                lu  = False
        except:
            # conn=False
            print("aucune connexion")
        time.sleep(1)

def lecture ():
  
    recup = open(r"C:\Users\DELL\Desktop\Python\Tracking\Victime\data.info", "r")

    print(recup.read())
    #lu = False

def notifier ():
    notification = Notify()
    notification.title = "Nouvelle connexion"
    notification.message = Date + ip
    notification.send()


recup = open(r"C:\Users\DELL\Desktop\Python\Tracking\Victime\data.info", "r")
ok = False
while not ok :
    lire = recup.readline()
    if lire.startswith("Date"):
        Date = lire
    elif lire.startswith("ip du reseau"):
        ip = lire
    elif lire.startswith("Organisation"):
        ok = True
    


if __name__=="__main__":
	main()



