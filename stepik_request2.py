import requests
import re
with open("sample3.html", "r") as sample:
   
    # print(source_content)
# source_link = str(input())
# source_content = requests.get(source_link).content

#source_content = """<a href="http://stepic.org/courses"><a href='https://www.stepic.org'><a href="http://www.cnews.ru/cgi-bin/redirect.cgi?http://gift.cnews.ru">"""
    patt1 = r"<a.+?href.+?>"
    patt2 = r"[^<>]+[a href=\".+|<a href=\'.+]?"
    link_list = []
    for line in sample:
        line = line.rstrip()
        match = re.findall(patt1, line)
        # print(match)
        if match != []:
            link_list.append(match[0])

#link_list = re.findall(patt2, source_content)
# print(link_list)
site_list = []
for item in link_list:
    # print(item)
    pat1 = r"\w+\.\w+\.\w+|\w+\.\w+"
    pat2 = r"(\w+\.\w+\.?)+\w+"
    # extracted_link = re.search(pat1, item)
    extracted_link = re.search(pat2, item)
    if extracted_link:
        # print(extracted_link.group())
        if extracted_link.group() not in site_list:
            site_list.append(extracted_link.group())
for item in sorted(site_list): print(item)
