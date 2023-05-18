from bs4 import BeautifulSoup as bs
import time
import os


ENCODING = "utf-8"
folder_name = 'name dictionary'
female_list = []
unisex_list = []
male_list = []

def create_list(input, mylist):
    string = ""
    soup = bs(open(input, 'r', encoding= ENCODING).read(), 'html.parser')
    table_item = list(soup.find("div" , {"class" : "ülkeler"}).find_all("table" , {"class" : "kisiler-tablo"}))[1]
    for i in list(table_item.find_all("tr"))[2:]:
        string += list(i.find_all("td"))[1].text + "\n"
    string = string.strip("\n")
    mylist = string.split("\n")
    return mylist


def beautify_string(string):
    name = ""
    string = string.lower()
    string = string.replace(chr(231), "c").replace(chr(252), "u").replace(chr(305), "i")
    string = string.replace(chr(351), "s").replace(chr(287), "g").replace(chr(246), "o")
    string = string.replace(chr(226), "a").replace(chr(251), "u").replace(chr(238), "i")
    string = string.replace("ş", "s").replace("ü", "u")
    for char in string:
        if ord(char) in range(128):
            name += char
    
    return name

def write_to_file(path, mylist):
    out_file = open(path, "w", encoding=ENCODING)
    for name in mylist[:-1]:
        name = name.lower()
        # test(name)
        name = beautify_string(name)
        out_file.write(name.lower() + "\n")
    name = beautify_string(name.lower())
    out_file.write(name)



mylist1 = []
mylist2 = []

def test(myname):
    for char in myname:
        if ord(char) not in range(128) and char not in mylist2:
            mylist1.append(ord(char))
            mylist2.append(char)


file_name = os.path.join(folder_name, 'female.html')
female_list = create_list(file_name, female_list)

file_name = os.path.join(folder_name, 'male.html')
male_list = create_list(file_name, male_list)

unisex_list = list(set(male_list) & set(female_list)) # find the intersection
for name in unisex_list:
    male_list.remove(name)
    female_list.remove(name)


## FEMALE ##

write_path = folder_name + "/female_name.txt"
write_to_file(write_path, female_list)

## MALE ##

write_path = folder_name + "/male_name.txt"
write_to_file(write_path, male_list)

## UNISEX ##

write_path = folder_name + "/us_name.txt"
write_to_file(write_path, unisex_list)
