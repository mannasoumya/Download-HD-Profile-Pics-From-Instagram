import json
import requests
from bs4 import BeautifulSoup
import re

def get_insta_id(script_tags):
    if(script_tags[3].text.find("logging_page_id\":\"profilePage_")==-1):
        js_need_str=script_tags[4].text
        index=js_need_str.find("logging_page_id\":\"profilePage_")
        id_insta=js_need_str[index+25:index+50]
        id_insta= re.sub('\D', '', id_insta)
        return id_insta
    else:
        js_need_str=script_tags[3].text
        index=js_need_str.find("logging_page_id\":\"profilePage_")
        id_insta=js_need_str[index+25:index+50]
        id_insta= re.sub('\D', '', id_insta)
        return id_insta
print()
print("This script can only download profile photos from \"Instagram Profiles\"")
url=input("\nEnter Instagram Profile URL  :- ")
print("Parsing URL ... Please Wait .. 25%")
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
all_script_tags=soup.find_all('script')
print("Finding ID ... Please Wait .. 50%")
id_insta=get_insta_id(all_script_tags)
api_url="https://i.instagram.com/api/v1/users/"+id_insta+"/info/"
print("Calling API ... Please Wait .. 75%")
r_api=requests.get(api_url)
hd_pic_arr=r_api.json()["user"]["hd_profile_pic_versions"]
if(len(hd_pic_arr)>1):
    hd_pic_url=hd_pic_arr[1]["url"]
else:
    hd_pic_url=hd_pic_arr[0]["url"]
    print("HD pic may not be avaiable for this user")
print("Done .. 100%")
f = open(id_insta+"_hd_pic"+".jpg",'wb')
f.write(requests.get(hd_pic_url).content)
f.close()
print()
print("Your pic is downloaded in the directory this script is running on with name \""+id_insta+"_hd_pic.jpg\"")
