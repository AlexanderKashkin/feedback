from datetime import datetime, timezone, tzinfo
from uuid import uuid4

from backend.models import Feedback, SignForm


class SignEvent:
    def __init__(self, sign_form):
        self.event = 'sign'
        self.name = sign_form.name
        self.phone = sign_form.phone

    def get_data(self):
        return {
            'event': self.event,
            'person': {
                'name': self.name,
                'phone': self.phone
            }
        }


class ReviewEvent:
    def __init__(self, review_form):
        self.event = 'review'
        self.name = review_form.name
        self.phone = review_form.phone
        self.email = review_form.email
        self.message = review_form.msg

    def get_data(self):
        return {
            'event': self.event,
            'message': {
                'name': self.name,
                'phone': self.phone,
                'email': self.email,
                'message': self.message
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
