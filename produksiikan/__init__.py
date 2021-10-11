
import requests
from bs4 import BeautifulSoup


def data_extraction():
    try:
        content = requests.get('http://pipp.djpt.kkp.go.id/produksi_harga')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.string)  # pakai string supaya tag nya hilang
        result = soup.find('table', {'class', 'table table-striped'})
        result = result.findChildren('td')

        i = 0

        for res in result:
            print(i, res)
            if i == 0:
                tf1 = res.text
            elif i == 1:
                pr1 = res.text
            elif i == 2:
                tf2 = res.text
            elif i == 3:
                pr2 = res.text
            elif i == 4:
                tf3 = res.text
            elif i == 5:
                pr3 = res.text
            elif i == 6:
                tf4 = res.text
            elif i == 7:
                pr4 = res.text
            elif i == 8:
                tf5 = res.text
            elif i == 9:
                pr5 = res.text
            elif i == 10:
                tf6 = res.text
            elif i == 11:
                pr6 = res.text
            elif i == 12:
                tf7 = res.text
            elif i == 13:
                pr7 = res.text
            elif i == 14:
                tf8 = res.text
            elif i == 15:
                pr8 = res.text
            elif i == 16:
                tf9 = res.text
            elif i == 17:
                pr9 = res.text
            elif i == 18:
                tf10 = res.text
            elif i == 19:
                pr10 = res.text
            i = i + 1

        hasil = dict()
        hasil['type_fish1'] = tf1
        hasil['production1'] = pr1
        hasil['type_fish2'] = tf2
        hasil['production2'] = pr2
        hasil['type_fish3'] = tf3
        hasil['production3'] = pr3
        hasil['type_fish4'] = tf4
        hasil['production4'] = pr4
        hasil['type_fish5'] = tf5
        hasil['production5'] = pr5
        hasil['type_fish6'] = tf6
        hasil['production6'] = pr6
        hasil['type_fish7'] = tf7
        hasil['production7'] = pr7
        hasil['type_fish8'] = tf8
        hasil['production8'] = pr8
        hasil['type_fish9'] = tf9
        hasil['production9'] = pr9
        hasil['type_fish10'] = tf10
        hasil['production10'] = pr10
        return hasil
    else:
        return None

# import json
# result = json.dumps(result)
# print(type(result))


def show_data(result):
    if result is None:
        print('Tidak bisa menemukan data')

    print('Fish type and total production in 2021')
    print(result['type_fish1'], result['production1'])
    print(result['type_fish2'], result['production2'])
    print(result['type_fish3'], result['production3'])
    print(result['type_fish4'], result['production4'])
    print(result['type_fish5'], result['production5'])
    print(result['type_fish6'], result['production6'])
    print(result['type_fish7'], result['production7'])
    print(result['type_fish8'], result['production8'])
    print(result['type_fish9'], result['production9'])
    print(result['type_fish10'], result['production10'])
