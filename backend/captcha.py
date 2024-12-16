import requests
from fastapi import HTTPException, status

from backend.routes import logger
from config.load_conf import config


class CaptchaV3:

    def __init__(self, token: str):
        self.token = token
        self.cfg = config.captcha

    result = None
    timestamp = None
    hostname = None
    status_code = None
    errors = []

    def token_site_verify(self):
        url = 'https://www.google.com/recaptcha/api/siteverify'
        logger.info('start token site verify')
        resp = requests.post(url=url, headers={'Content-Type' : 'application/x-www-form-urlencoded'}, data={'secret': self.cfg.secret, 'response': self.token})
        logger.info('end token site verify')
        response = resp.json()
        self.result = response.get('success', None)
        self.timestamp = response.get('timestamp', None)  # not required
        self.hostname = response.get('hostname', None)  # not required
        self.errors = response.get('error-codes', None)
        if resp.status_code != status.HTTP_200_OK or self.result is False:  # status_code not 200 or success = False
            logger.error(
                f'token site verify failed {self.token, self.result, self.timestamp, self.hostname, self.errors}')
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.errors)


def verify_captcha(token: str):
    CaptchaV3(token).token_site_verify()
