import psycopg2 as pg2
from fastapi import HTTPException, status

from backend.models import Feedback, SignForm
from backend.routes import logger


class PostgresSqlClient:
    def __init__(self):
        self.user = 'postgres'
        self.password = 'secret'
        self.host = 'localhost'
        self.port = '5432'

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
                connection.execute(row)
            except Exception as e:
                logger.error(e)
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

    def insert_feedback(self, feedback: Feedback):
        logger.info('start insert feedback')
        self._insert_row(
            f"insert INTO feedback values (uuid_generate_v4(), now(), '{feedback.phone}', '{feedback.email}', '{feedback.msg}', '{feedback.name}', {feedback.status_publish_msg})")
        logger.info('end insert feedback')

    def insert_sign_form(self, sign_form: SignForm):
        logger.info('start insert sign_form')
        self._insert_row(
            f"insert INTO sign_form values (uuid_generate_v4(), now(), '{sign_form.name}', '{sign_form.phone}', {sign_form.status_publish_msg})")
        logger.info('end insert sign_form')


def insert_feedback_to_db(feedback: Feedback):
    return PostgresSqlClient().insert_feedback(feedback)


def insert_sign_form_to_db(sign_form: SignForm):
    return PostgresSqlClient().insert_sign_form(sign_form)
