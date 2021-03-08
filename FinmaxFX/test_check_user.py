import requests
import json


def test_api():
    with open('params.json', 'r', encoding='utf-8') as params:
        text = json.load(params)
        print()
    for user_request in text['email']:
        print(user_request)
        user_request = requests.post("https://finmaxfx.com/api/checkEmail.php", data={'email': user_request})
        print(user_request.status_code, user_request.json())

        # Запись ответа:
        # with open('response_result.json', 'wb') as fd:
        #     for chunk in user_request.iter_content(chunk_size=128):
        #          fd.write(chunk)
        #
        # Проверка аффилиат ID
        # assert user['a_aid'] == '980', 'Failed'
        # print("Success")
