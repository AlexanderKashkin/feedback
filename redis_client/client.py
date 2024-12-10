from fastapi import HTTPException, status
from redis import Redis

from backend.routes import logger
from redis_client.models import BaseMessage


class RedisClient:
    def __init__(self, cfg):
        self.cfg = cfg
        self.client = Redis(host=self.cfg.host, port=self.cfg.port, db=self.cfg.db)

    logger.info('start redis client')

    def publish(self, obj):
        logger.info(f'start publish {str(obj)}')
        msg = BaseMessage(obj=obj).create_msg()
        try:
            self.client.publish(channel=self.cfg.topic, message=str(msg))
            obj.status_publish_msg = True
        except Exception as e:
            logger.error(f'publish msg is failed, ex {e}')
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
