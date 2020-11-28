def read_files(name):
    import xml.etree.ElementTree as ET
    tree = ET.parse(name)
    root = tree.getroot()
    xml_items = root.findall("./channel/item/description")
    description_text = ''
    for items in xml_items:
        description_text = description_text + items.text
    return description_text


def count(description_text):
    list_split = description_text.split(' ')
    dict_value = {}
    for word in list_split:
        if len(word) > 6:
            if word in dict_value:
                dict_value[word] += 1
            else:
                dict_value[word] = 1
    return dict_value


def sort_top(dict_value):
    lambda_key = lambda dict_word_value: (dict_word_value[1], dict_word_value[1])
    sort_list = sorted(dict_value.items(), key=lambda_key, reverse=True)
    count = 1

    dict_top_10 = {}
    for word in sort_list:
        dict_top_10[count] = word
        count += 1
        if count == 10:
            break

    for top_10 in dict_top_10.values():
        print('  ', top_10[1], ': ', top_10[0])

    return dict_top_10


def main_menu(name):
    sort_top(count(read_files(name)))


main_menu('newsafr.xml')
