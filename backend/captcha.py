import requests
from fastapi import HTTPException, status

from backend.routes import logger
from config.load_conf import config

class CaptchaV3:

    def __init__(self, token: str):
        self.token = token

    __secret = 'gref_not_gay'
    result = None
    timestamp = None
    hostname = None
    status_code = None
    errors = []

    def token_site_verify(self):
        url = 'https://www.google.com/recaptcha/api/siteverify'
        logger.info('start token site verify')
        resp = requests.post(url=url, json={'secret': self.__secret, 'response': self.token})
        logger.info('end token site verify')
        response = resp.json()
        self.result = response.get('success', None)
        self.timestamp = response.get('timestamp', None)  # not required
        self.hostname = response.get('hostname', None)  # not required
        self.errors = response.get('error-codes', None)
        if config.debug:
            return
        if resp.status_code != status.HTTP_200_OK or not self.result:  # status_code not 200 or success = False
            logger.error(
                f'token site verify failed {self.token, self.result, self.timestamp, self.hostname, self.errors}')
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.errors)


def verify_captcha(token: str):
    CaptchaV3(token).token_site_verify()
