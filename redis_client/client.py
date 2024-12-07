from fastapi import HTTPException, status
from redis import Redis

from redis_client.models import BaseMessage
from backend.routes import logger

class RedisClient:
    host: str = 'localhost'
    port: int = 6379
    topic = 'test'

    logger.info('start redis client')
    client = Redis(host=host, port=port, db=0)

    def publish(self, message: str):
        logger.info(f'start publish {message}')
        try:
            self.client.publish(channel=self.topic, message=str(message))
        except Exception as e:
            logger.error(f'publish msg is failed, ex {e}')
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)


def publish_msg(obj):
    msg = BaseMessage(obj=obj).create_msg()
    return RedisClient().publish(msg)
