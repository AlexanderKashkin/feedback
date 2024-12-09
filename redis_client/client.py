from fastapi import HTTPException, status
from redis import Redis

from backend.routes import logger
from redis_client.models import BaseMessage

from config.load_conf import config

class RedisClient:
    host: str = config.redis.host
    port: int = int(config.redis.port)
    topic: str = config.redis.topic
    db: int = int(config.redis.db)

    logger.info('start redis client')
    client = Redis(host=host, port=port, db=db)

    def publish(self, obj):
        logger.info(f'start publish {str(obj)}')
        msg = BaseMessage(obj=obj).create_msg()
        try:
            self.client.publish(channel=self.topic, message=str(msg))
            obj.status_publish_msg = True
        except Exception as e:
            logger.error(f'publish msg is failed, ex {e}')
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
