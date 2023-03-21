# myapp.py
import logging
import mylib

def main():

    # Loggin Standar
    # logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.basicConfig(filename='myapp.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

    ## Loggin send variables
    logging.warning('%s before you %s', 'Look', 'leap!')

    ## Cambiar formato a los logs
    
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.warning('And this, too')


    ## Logger 
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logger.info("logger info")


if __name__ == '__main__':
    main()