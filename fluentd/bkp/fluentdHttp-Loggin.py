
import logging 
from fluent_http import FluentHttpHandler

def main():

    logger = logging.getLogger('car.api')
    fluent_http_handler = FluentHttpHandler(url='localhost', port=9880, tag='app.python')
    logger.addHandler(fluent_http_handler)
    logger.setLevel(logging.INFO)

    logger.info("hello world")


if __name__ == '__main__':

    main()