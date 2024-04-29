import logging


def giveMeLoggingObject():
    format_str = '%(asctime)s %(message)s'
    file_name  = 'SQA-LOGGER.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('sqa-logger')
    return loggerObj