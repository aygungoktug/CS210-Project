from parse_names import beautify_string
from bs4 import BeautifulSoup as bs
import os

count = 0
folder_name = 'assembly html files'
ENCODING = "utf-8"
assembly_no = 1

def sort_key(file_name):
    # Extract the number from the file name
    number = int(file_name[file_name.find("o") + 1 : file_name.find(".")])
    return number

file_list = os.listdir("assembly html files")
# Sort the file list based on the custom key
sorted_file_list = sorted(file_list, key=sort_key)
# print(sorted_file_list)


for filename in sorted_file_list:
    kisi_counter = 0
    soup = bs(open(os.path.join(folder_name, filename), "r", encoding = ENCODING).read(), "html.parser")
    mylist = list(soup.find_all("div", {"class" : "row profile-list"}))
    for profile in mylist:
        kisi_counter += 1
        info = profile.find("strong", {"class" : "isim_soyisim"}).text.strip()
        city = beautify_string(info[info.find("(") + 1:info.find(")")])
        if info.find("*") == -1:
            name = info[:info.find("(") - 1]
        else:
            name = info[:info.find("*") - 1]
        file_name = "{}.txt".format(city)
        # if not os.path.exists(os.path.join("city_info", file_name)):
        out_file = open("city info/raw/" + file_name, "a", encoding=ENCODING)
        out_file.write(str(assembly_no) + " " + beautify_string(name.lower()) + "\n")
    print("Parsed the information about Assembly No {}".format(assembly_no))
    assembly_no += 1



    

    