from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import subprocess
import os

username = 'simon.ochotnicky@esas.autocont.sk'
password = 'Heslo123'
SP_SITE_URL = "https://servisac.sharepoint.com/sites/dev01/"

auth_cookie = Office365('https://servisac.sharepoint.com', username='simon.ochotnicky@esas.autocont.sk', password='Heslo123').GetCookies()
site = Site('https://servisac.sharepoint.com/sites/dev01',version=Version.v365, authcookie=auth_cookie)

x="JobsSchedules"

#os.system("C:\Users\polnikr\source\PycharmProjects\motivation\main.exe\main\main.exe")

# get all names
def get_names_of_folders(list_name):
    new_list = site.List(list_name)
    data = new_list.get_list_items(fields=['Name'])
    nazvy_suborov=[]
    for x in data:
        nazvy_suborov.append(x['Name'])

    return nazvy_suborov


# downloadnes to jobs directory
def download_and_create(nazvy_suborov):
    for x in nazvy_suborov:
        folder = site.Folder("JobsSchedules/"+x)
        allfiles = folder.files
        file = folder.get_file(allfiles[0]["Name"])
        with open("Jobs/"+allfiles[0]["Name"], "wb") as fh:
            fh.write(file)

# prejdes vsetky nazvy suborov .exe a spustis ich
def execute():
    for filename in os.scandir("Jobs"):
        print(filename.path)
        if filename.is_file():
            subprocess.run(rf"{filename.path}")

#execute()

#vymaz subor exe zo zoznamu
def vymaz_subor():
    new_list = site.List("JobsSchedules")
    data = new_list.get_list_items(fields=['Name'])

    for x in data:
        folder = site.Folder("JobsSchedules/" + x["Name"])
        allfiles = folder.files
        for y in allfiles:
            print(y["Name"])
            folder.delete_folder("JobsSchedules/" + x["Name"])
        #print(allfiles)


vymaz_subor()