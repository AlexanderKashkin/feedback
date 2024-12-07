from fastapi import HTTPException, status
from redis import Redis

from backend.routes import logger
from redis_client.models import BaseMessage


class RedisClient:
    host: str = 'localhost'
    port: int = 6379
    topic = 'test'

    logger.info('start redis client')
    client = Redis(host=host, port=port, db=0)

    def publish(self, obj):
        logger.info(f'start publish {str(obj)}')
        msg = BaseMessage(obj=obj).create_msg()
        try:
            self.client.publish(channel=self.topic, message=str(msg))
            obj.status_publish_msg = True
        except Exception as e:
            logger.error(f'publish msg is failed, ex {e}')
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
