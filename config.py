TOKEN = "6570865512:AAH2wn9P-e1iXg2yMG6ieAMjrKydzOUoulw"
IAM_TOKEN = 't1.9euelZqJjMeTj8uNisqNjYuLl8vNne3rnpWazMjHm57Nx4ubjZuWiZOVnIzl8_c2DG5N-e8DdEQt_t3z93Y6a0357wN0RC3-zef1656VmpKOlMmQmseQl8mal5aek8aX7_zF656VmpKOlMmQmseQl8mal5aek8aXveuelZqQkMeLnpeUlI-clpSbypCdibXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.IqRbneUlW9Hyjc2O-rcSBQEILwVwiugw9mkOHJhoIMCfmig44UuLXlX-RH-YOJnf6sJO9Apsk_FVfNLKJ9j1Dw'
FOLDER_ID = 'b1gshjrk2cqqlcr257qj'
MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 4

HOME_DIR = '/home/student/pythonProject8'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token

MAX_USER_STT_BLOCKS = 20
MAX_USER_TTS_SYMBOLS = 8_000
MAX_USER_GPT_TOKENS = 8_000

LOGS = 'logs.txt'
DB_FILE = 'messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]