# -*- coding: utf-8 -*-
import time
import requests,json
import pandas as pd


def scrap_offers():
    data = []
    offset = 0
    print("Scraping offers...")
    while True:
        r = requests.get(f"https://www.olx.pl/api/v1/offers/?offset={offset}&limit=40&category_id=14&region_id=4&city_id=8959&distance=2&filter_refiners=spell_checker&suggest_filters=true&sl=1883fd019c9x585ec624")
        if r.status_code != 200:
            print("end of the loop.")
            break
        else:
            json_data = r.json()
            offers = json_data['data']
            for offer in offers:
                try:
                    district = offer['location']['district']['name']
                except KeyError:
                    pass
                else:
                    params = offer['params']
                    for param in params:
                        if param['key'] == 'rooms':
                            rooms = dict_rooms[param['value']['key']]
                        elif param['key'] == 'm':
                            meters = param['value']['key']
                        elif param['key'] == 'furniture':
                            furniture = True if param['value']['key'] == 'yes' else False
                        elif param['key'] == 'price':
                            price = param['value']['value']

                    row_data = {
                        "district":district,
                        'numberOfRooms':rooms,
                        'meters':meters,
                        'furniture':furniture,
                        'price':price
                    }
                    print("adding new row...")
                    data.append(row_data)

            offset += 40
            time.sleep(1)

    df = pd.DataFrame(data)

    df.to_csv('apartments_offers.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    scrap_offers()


