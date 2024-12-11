from fastapi import HTTPException, status
from redis import Redis

from backend.models import Feedback, SignForm
from backend.routes import logger
from redis_client.models import SignEvent, ReviewEvent


class RedisClient:
    def __init__(self, cfg):
        self.cfg = cfg
        self.client = Redis(host=self.cfg.host, port=self.cfg.port, db=self.cfg.db)

    logger.info('start redis client')

    def _publish(self, msg):
        logger.info(f'start publish {str(msg)}')
        try:
            self.client.publish(channel=self.cfg.topic, message=str(msg))
            return True
        except Exception as e:
            logger.error(f'publish msg is failed, ex {e}')
            return False

    def notify_feedback(self, feedback: Feedback):
        result = self._publish(ReviewEvent(feedback).msg)
        feedback.status_publish_msg = result

    def notify_review(self, sign_form: SignForm):
        result = self._publish(SignEvent(sign_form).msg)
        sign_form.status_publish_msg = result