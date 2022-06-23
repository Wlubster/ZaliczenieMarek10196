import datetime
import json
import webbrowser
import time

import requests
import base64
from urllib.parse import urlencode

from selenium import webdriver





client_id = '62aadb1a5ed64823bd2ea0367892d4e4'
client_secret = 'e1f07508bbd94178807802e75d647489'


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must pass client_id or client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        return{
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return{
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_header()
        r = requests.post(token_url, data=token_data, headers=token_header)
        if r.status_code not in range(200, 299):
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True


spotify = SpotifyAPI(client_id, client_secret)
spotify.perform_auth()
access_token = spotify.access_token
headers = {
    "Authorization": f"Bearer {access_token}"
}
r1 = requests.get("https://api.spotify.com/v1/artists/1oxn6cQ37twQ7yGnlE3ETd", headers=headers)
#print(r1.text)
#print("------------------------------------------------")
endpoint = "https://api.spotify.com/v1/search"
print("""Co chcesz wyszukać?: 
1. Album
2. Artist
3. Track
""")
choice = int(input("Podaj cyfre: "))

if choice == 1:
    query = input("Name of the album: ")
    q1 = "Album"
if choice == 2:
    query = input("Name of the Artist: ")
    q1 = "Artist"
if choice == 3:
    query = input("Name of the track: ")
    q1 = "Track"

#query = input("artysta")
#print(query.title())

data = urlencode({"q": query, "type": q1.lower()})
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url, headers=headers)

f = open("test.json", "w")
f.write(r.text)
f.close()

f = open("test.json", "r")
f.close()
json_file_path = "test.json"

my_list = [+1]
musicNumber = 0

with open("test.json", "r") as j:

    try:

        contents = json.load(j)

        for i in range(len("test.json")):

            if contents[q1.lower()+"s"]["items"][i]["name"] == query.title():
                print(i)
                print("Name: " + contents[q1.lower()+"s"]["items"][i]["name"])

                if q1.lower()+"s" == "artists":
                    print(contents[q1.lower() + "s"]["items"][i]["genres"])
                    print(contents[q1.lower() + "s"]["items"][i]["popularity"])

                if q1.lower()+"s" == "tracks":
                    #print(list(contents.keys()))
                    print("Type: " + contents[q1.lower() + "s"]["items"][i]["type"])
                    print("Author: " + contents[q1.lower() + "s"]["items"][i]["album"]["artists"][0]["name"])

                    try:
                        my_list.append(contents[q1.lower() + "s"]["items"][i]["preview_url"])
                        print("Preview url: " + contents[q1.lower() + "s"]["items"][i]["preview_url"])
                    except TypeError:
                        print("Nie ma podglądu!")

                    finally:
                        musicNumber += 1
                        print("Music Number: " + str(musicNumber))
                    #print("Preview url: " + contents[q1.lower() + "s"]["items"][i]["preview_url"])
                    print("Popularity: " + str(contents[q1.lower()+"s"]["items"][i]["popularity"]))


                print(contents[q1.lower()+"s"]["items"][i]["uri"])
                print("[--------------------------------------]")


    except IndexError:
        print("")

    finally:
        j.close()

if q1 == "Track":
    musicP = int(input("która nuta?: "))
    #webbrowser.open(my_list[musicP])
    driver = webdriver.Chrome()
    driver.get(my_list[musicP])



#testGit
#json_object = json.loads("test.json")
#print(json_object["name"])

#print(r.json()['name'])
#j = r.json()
#json_object = json.loads(j)
#print(json_object["name"])