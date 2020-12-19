import json


def read_files(name):
    file_json = 'json'
    file_xml = 'xml'
    if file_json in name:
        with open(name, encoding='utf-8') as datafile:
            json_data = json.load(datafile)
            description_text = ''
            for items in json_data['rss']['channel']['items']:
                description_text += ' ' + items['description']
        return description_text
    elif file_xml in name:
        import xml.etree.ElementTree as ET
        tree = ET.parse("newsafr.xml")
        root = tree.getroot()
        xml_items = root.findall("./channel/item/description")
        description_text = ''
        for items in xml_items:
            description_text = description_text + items.text
        return description_text


def count(description_text):
    number = int(input('Введите кол-во символов : '))
    list_split = description_text.split(' ')
    word_value = {}
    for word in list_split:
        if len(word) > number:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value


def sort_top(word_value):
    top = int(input('Введите кол-во топов : '))
    dict_sort = lambda dict_word_value: (dict_word_value[1], dict_word_value[1])
    sort_list = sorted(word_value.items(), key=dict_sort, reverse=True)
    count = 1
    top_10 = {}

    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == top:
            break

    for top_10 in top_10.values():
        print('  ', top_10[1], ': ', top_10[0])
    return top_10


def main_menu():
    name = input('Введите имя файла json или xml : ')
    sort_top(count(read_files(name)))


main_menu()

