import requests
import re
source_link = input()
source_get = requests.get(source_link)
source_content = str(source_get.content)

patt1 = r"<a.+?href.+?>"
patt2 = r"[^<>]+[a href=\".+|<a href=\'.+]?"
#link_list = []
#for line in source_content:

link_list = re.findall(patt1, source_content)
# print(match)


#link_list = re.findall(patt2, source_content)
# print(link_list)
site_list = []
for item in link_list:
    # print(item)
    pat1 = r"\w+\.\w+\.\w+|\w+\.\w+"
    pat2 = r"(\w+[\.\-]\w+[\.\-]?)+\w+"
    # extracted_link = re.search(pat1, item)
    extracted_link = re.search(pat2, item)
    if extracted_link:
        # print(extracted_link.group())
        if extracted_link.group() not in site_list:
            site_list.append(extracted_link.group())
for item in sorted(site_list): print(item)


enemy_pat = r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)"
# # linkToHTMLFile = "https://stepic.org/media/attachments/lesson/24471/01"
# linkToHTMLFile = input()
# response = requests.get(linkToHTMLFile)
# if response.status_code == 200:
#     data = response.text

# result = []
# for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", data):
#     domain = link[8]
#     if domain not in result:
#         result.append(domain)

# result.sort()

# for domain in result:
#     print(domain)