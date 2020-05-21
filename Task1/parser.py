from Task1.url import page
import json


soup_json = json.loads(page.text)

# if soup_json is None:
#     print('Не получилось ничего вытащить с сайта')
# else:
#     print(soup_json)



