import logging
import config

operation_lst = []

async def calculate(problem):
    try:
        response = eval(problem)
        return response

    except Exception as e:
        logging.error(e)
