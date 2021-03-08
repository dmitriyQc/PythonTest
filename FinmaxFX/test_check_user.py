import requests
import json


def test_api():
    with open('params.json', 'r', encoding='utf-8') as params:
        text = json.load(params)
        print()
    for user_request in text['email']:
        try:
            print(user_request)
            user_request = requests.post("https://finmaxfx.com/api/checkEmail.php", data={'email': user_request})

        # Запись ответа:
        # with open('response_result.json', 'wb') as fd:
        #     for chunk in user_request.iter_content(chunk_size=128):
        #          fd.write(chunk)
        #
        # Проверка аффилиат ID
            user = user_request.json()
            assert user['a_aid'] == '970'
            print(user_request.status_code, user_request.json(), " - Success")
        except:
            print(user_request.status_code, user_request.json(), ' - Failed')
