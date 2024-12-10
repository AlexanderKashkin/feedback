from fastapi import FastAPI, status
from loguru import logger

from backend.captcha import verify_captcha
from backend.models import Feedback, SignForm
from db.client import PostgresSqlClient
from redis_client.client import RedisClient

from config.load_conf import config

app = FastAPI()

logger.add('log.txt')
logger.info('start app')

redis = RedisClient(config.redis)
db = PostgresSqlClient(config.database)
db.migrations()


@app.post("/feedback", status_code=status.HTTP_201_CREATED)
async def feedback(request_feedback: Feedback):
    logger.info(f'get request {feedback.__name__}, body: {request_feedback}')
    verify_captcha(request_feedback.token)
    redis.publish(request_feedback)
    db.insert_feedback(request_feedback)
    logger.info('end')
    return {}


@app.post("/sign-form", status_code=status.HTTP_201_CREATED)
async def sign_form(request_sign_form: SignForm):
    logger.info(f'get request {sign_form.__name__}, body: {request_sign_form}')
    verify_captcha(request_sign_form.token)
    redis.publish(request_sign_form)
    db.insert_sign_form(request_sign_form)
    logger.info('end')
    return {}
