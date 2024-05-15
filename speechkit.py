import requests
from creds import get_creds
IAM_TOKEN, FOLDER_ID = get_creds()
def speech_to_text(data):
    iam_token = 't1.9euelZqJjMeTj8uNisqNjYuLl8vNne3rnpWazMjHm57Nx4ubjZuWiZOVnIzl8_c2DG5N-e8DdEQt_t3z93Y6a0357wN0RC3-zef1656VmpKOlMmQmseQl8mal5aek8aX7_zF656VmpKOlMmQmseQl8mal5aek8aXveuelZqQkMeLnpeUlI-clpSbypCdibXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.IqRbneUlW9Hyjc2O-rcSBQEILwVwiugw9mkOHJhoIMCfmig44UuLXlX-RH-YOJnf6sJO9Apsk_FVfNLKJ9j1Dw'
    folder_id = 'b1gshjrk2cqqlcr257qj'
    params = "&".join([
        "topic=general",
        f"folderId={folder_id}",
        "lang=ru-RU"
    ])


    headers = {
        'Authorization': f'Bearer {iam_token}',
    }


    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )


    decoded_data = response.json()
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")
    else:
        return False, "При запросе в SpeechKit возникла ошибка"

def text_to_speech(text):
    iam_token = 't1.9euelZqJjMeTj8uNisqNjYuLl8vNne3rnpWazMjHm57Nx4ubjZuWiZOVnIzl8_c2DG5N-e8DdEQt_t3z93Y6a0357wN0RC3-zef1656VmpKOlMmQmseQl8mal5aek8aX7_zF656VmpKOlMmQmseQl8mal5aek8aXveuelZqQkMeLnpeUlI-clpSbypCdibXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.IqRbneUlW9Hyjc2O-rcSBQEILwVwiugw9mkOHJhoIMCfmig44UuLXlX-RH-YOJnf6sJO9Apsk_FVfNLKJ9j1Dw'
    folder_id = 'b1gshjrk2cqqlcr257qj'
    headers = {'Authorization': f'Bearer {iam_token}'}
    data = {
        'text': text,
        'folderId': folder_id,
        'lang': 'ru-RU'
    }
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"