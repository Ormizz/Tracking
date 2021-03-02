"""
Auteur     :  Nucleus
Version    :  1.0
Date        :  02-03-2021
Description :  
"""

import urllib.request
import json
import time
import socket
from datetime import datetime
def main(IPaddress="127.0.0.1"):
    conn = False
    last_ip=IPaddress
    while True:
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            conn=True
            ip = socket.gethostbyname(socket.gethostname())
            if(ip!= last_ip):
                last_ip=ip
                date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print("|------Nouvelle connexion------|")
                get_data(ip,date)
                
            else : print("connecté au meme reseau ip : "+ip)
        except:
            conn=False
            link = "http://ip-api.com/json"
            response = urllib.request.urlopen(link)
            print(json.loads(response.read()))
            print("aucune connexion")
        time.sleep(1)
        

def get_data(ip,date):
    
    link = "http://ip-api.com/json"
    response = urllib.request.urlopen(link)
    data = json.loads(response.read())
    print(date)
    data['ip']=ip
    data['date']=date
    
    if(len(data)>1):
        print("Date : "+data["date"])
        print("Status : "+data["status"])
        print("Query : "+data["query"])
        print("ip du reseau : "+data["ip"])
        print("Ville : "+data["city"])
        print("Pays : "+data["country"])
        print("Region : "+data["regionName"])
        print("Internet Service Provider : "+data["isp"])
        print("as : "+data["as"])
        print("Coordonnées : "+str(data["lat"])+","+str(data["lon"]))
        print("Organisation : "+data["org"])
        print("\n")
        write_in_file(data)
    else : print("aucune info")

def write_in_file(data):
    with open("data.info",'a') as f :
        f.write("|------Nouvelle connexion------|\n")
        f.write("Date : "+data["date"]+"\n")
        f.write("Status : "+data["status"]+"\n")
        f.write("Query : "+data["query"]+"\n")
        f.write("ip du reseau : "+data["ip"]+"\n")
        f.write("Ville : "+data["city"]+"\n")
        f.write("Pays : "+data["country"]+"\n")
        f.write("Region : "+data["regionName"]+"\n")
        f.write("Internet Service Provider : "+data["isp"]+"\n")
        f.write("as : "+data["as"]+"\n")
        f.write("Coordonnées : "+str(data["lat"])+","+str(data["lon"])+"\n")
        f.write("Organisation : "+data["org"]+"\n")
        f.write("\n")
    print("info sauvegardé avec succes")
if __name__=="__main__":
	main()
