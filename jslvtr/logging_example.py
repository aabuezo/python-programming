import logging
"""
DEBUG - lowest level (for developing)
INFO
WARNING
ERROR
CRITICAL - highest level
"""

# logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

# logger = logging.getLogger(__name__)
logger = logging.getLogger('books')

logger.info('This will not show up by default.')
logger.warning('This will')
logger.debug('This is a debug message.')
logger.critical('A critical error occurred.')


logger = logging.getLogger('books.database')    # child logger
