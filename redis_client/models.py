from datetime import datetime, timezone
from uuid import uuid4

from backend.models import Feedback, SignForm


class SignEvent:
    def __init__(self, sign_form):
        self.sign_form = sign_form
        self.event = 'sign'

    def get_data(self):
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

    def get_data(self):
        return {
            'event': self.event,
            'message': {
                'name': self.review_form.name,
                'phone': self.review_form.phone,
                'email': self.review_form.email,
                'message': self.review_form.message
            }
        }


class BaseMessage:
    def __init__(self, obj):
        if type(obj) is Feedback:
            self.data = ReviewEvent(obj).get_data()
        elif type(obj) is SignForm:
            self.data = SignEvent(obj).get_data()

    def create_msg(self):
        return {
            "service": 'docfedorov',
            "source": 'be',
            "env": 'prod',
            "c_ts": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f'),
            "idempkey": str(uuid4()),
            "data": self.data
        }
