import json
data = [{
"name": "G", "parents": ["ZZZ"]}, {
"name": "TH", "parents": ["ZZZ"]}, {
"name": "G", "parents": ["ZY"]}, {
"name": "G", "parents": ["F"]}, {
"name": "A", "parents": []}, {
"name": "B", "parents": ["A"]}, {
"name": "C", "parents": ["A"]}, {
"name": "D", "parents": ["B", "C"]}, {
"name": "E", "parents": ["D"]}, {
"name": "F", "parents": ["D"]}, {
"name": "X", "parents": []}, {
"name": "Y", "parents": ["X", "A"]}, {
"name": "Z", "parents": ["X"]}, {
"name": "V", "parents": ["Z", "Y"]}, {
"name": "W", "parents": ["V"]}]

data_json = json.dumps(data)
source = json.loads(data_json)
class_set  = set()
result_dict = {}

def json_to_dict(source):
    """convert json data to dict {parent: child}"""
    result = {}
    for key in source:
        result[key["name"]] = key["parents"]
    return result

def child_dict(class_dict):
    """ """
    child_count_dict = {}
    for key, value in class_dict.items():
        result_dict[key] = 1
        for item in value:
            if item not in child_count_dict:
                child_count_dict[item] = [key]
            else:
                child_count_dict[item].append(key)
    # print("child_count_dict", "\n", child_count_dict)
    return child_count_dict

def set_maker(dict):
    for key, value in child_count_dict.items():
        recursive(key, value)
        if key not in class_set:
            class_set.add(key)
        result_dict[key] = len(class_set)
        class_set.clear()

def recursive(key, value):            
    for item in value:
        class_set.add(item)
        if item in child_count_dict:
            value = child_count_dict[item]
            recursive(key, value)

class_dict = json_to_dict(source)
child_count_dict = child_dict(class_dict)
set_maker(child_count_dict)
for key, value in sorted(result_dict.items()):
    print(key, ":", value)
