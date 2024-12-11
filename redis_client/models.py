from datetime import datetime, timezone
from uuid import uuid4


class Envelop:
    body = {
        "service": 'docfedorov',
        "source": 'be',
        "env": 'prod',
        "c_ts": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f'),
        "idempkey": str(uuid4()),
        "data": dict()
    }

    def set_data(self, data):
        self.body['data'] = data
        return self.body


class SignEvent:
    def __init__(self, sign_form):
        self.sign_form = sign_form
        self.event = 'sign'
        self.msg = Envelop().set_data(self._get_data())

    def _get_data(self):
        return {
            'event': self.event,
            'person': {
                'name': self.sign_form.name,
                'phone': self.sign_form.phone
            }
        }


class ReviewEvent:
    def __init__(self, review_form):
        self.event = 'review'
        self.review_form = review_form
        self.msg = Envelop().set_data(self._get_data())

    def _get_data(self):
        return {
            'event': self.event,
            'message': {
                'name': self.review_form.name,
                'phone': self.review_form.phone,
                'email': self.review_form.email,
                'message': self.review_form.msg
            }
        }
