from datetime import datetime, timezone
from uuid import uuid4

import psycopg2 as pg2
from fastapi import HTTPException, status

from backend.models import Feedback, SignForm
from backend.routes import logger
from config.load_conf import config


class PostgresSqlClient:
    def __init__(self):
        self.user = config.database.user
        self.password = config.database.password
        self.host = config.database.host
        self.port = config.database.port

    logger.info('start db')

    def _connection(self):
        logger.info('connect to db')
        try:
            connection_db = pg2.connect(user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port)
            connection_db.autocommit = True  # autosave commit in db
            return connection_db
        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='failed to connect to db')

    def _insert_row(self, row):
        with self._connection().cursor() as connection:
            try:
                connection.execute(query=row['query'], vars=row['vars'])
            except Exception as e:
                logger.error(e)
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

    def insert_feedback(self, feedback: Feedback):
        logger.info('start insert feedback')
        self._insert_row(
            {
                'query': 'insert INTO feedback (id, timestamp, phone, email, message, name, status_publish_msg_in_redis) values (%(id)s, %(timestamp)s, %(phone)s, %(email)s, %(message)s, %(name)s, %(status_publish_msg_in_redis)s)',
                'vars': {'id': str(uuid4()),
                         'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f'),
                         'phone': feedback.phone,
                         'email': feedback.email,
                         'message': feedback.msg,
                         'name': feedback.name,
                         'status_publish_msg_in_redis': feedback.status_publish_msg
                         }
            }
        )
        logger.info('end insert feedback')

    def insert_sign_form(self, sign_form: SignForm):
        logger.info('start insert sign_form')
        self._insert_row(
            {
                'query': 'insert INTO sign_form (id, timestamp, name, phone, status_publish_msg_redis) values (%(id)s, %(timestamp)s, %(name)s, %(phone)s, %(status_publish_msg_redis)s)',
                'vars': {'id': str(uuid4()),
                         'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f'),
                         'name': sign_form.name,
                         'phone': sign_form.phone,
                         'status_publish_msg_redis': sign_form.status_publish_msg}
            }
        )
        logger.info('end insert sign_form')


def insert_feedback_to_db(feedback: Feedback):
    return PostgresSqlClient().insert_feedback(feedback)


def insert_sign_form_to_db(sign_form: SignForm):
    return PostgresSqlClient().insert_sign_form(sign_form)
