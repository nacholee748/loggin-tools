import logging
#import mylib

def main():
    FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(filename='myapp.log', level=logging.INFO, format=FORMAT)
    
    logging.info('Started')
    #mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
    
    
import logging
import sys

logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.error("This is the first error")    

LOGGIN

https://docs.fluentd.org/language-bindings/python

https://hub.docker.com/r/fluent/fluentd/

https://www.fluentd.org/guides/recipes/docker-logging
https://docs.fluentd.org/output/s3

https://betterprogramming.pub/application-logging-best-practices-a-support-engineers-perspective-b17d0ef1c5df

https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/

https://stackoverflow.com/questions/13414899/python-logging-overview-of-currently-installed-loggers-handlers

Sentry
https://sentry.io/welcome/?utm_source=google&utm_medium=cpc&utm_campaign=9575834316&utm_content=g&utm_term=sentry&device=c&gclid=CjwKCAjwiJqWBhBdEiwAtESPaA0frYufEg7-JJGu91CVUVnpKtui3JGFoc65Noc4gT8hMYmTs-TBwRoCSLcQAvD_BwE&gclid=CjwKCAjwiJqWBhBdEiwAtESPaA0frYufEg7-JJGu91CVUVnpKtui3JGFoc65Noc4gT8hMYmTs-TBwRoCSLcQAvD_BwE