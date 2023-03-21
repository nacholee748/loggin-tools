""" Logs Manager Module
"""
import logging
from logging.handlers import SysLogHandler

_GENERAL_LOGGING_FORMAT = '[%(levelname)s] [%(asctime)s] %(message)s'
_DEFAULT_LOGGING_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
_DEFAULT_LOGGING_LEVEL = 'DEBUG'

class LogHandler(object):
    """
    Class for logs handling through the logging Python module

    Attributes:
        __logger: logging.Logger
    """
    def __init__(self,  logs_level: str = _DEFAULT_LOGGING_LEVEL) -> None:
        """
        This constructor method creates a logger object and sets its level to the value passed as parameter

        Args:
          logs_level (str): DEBUG, INFO, WARNING, ERROR, CRITICAL. Defaults to _DEFAULT_LOGGING_LEVEL
        """
        logging.basicConfig() # create StreamHandler for root logger
        self.__logger = logging.getLogger() # get root logger
        # set formatting on the root logger to modify AWS Cloudwatch default configuration
        self.__logger.handlers[0].setFormatter(logging.Formatter(fmt=_GENERAL_LOGGING_FORMAT, datefmt=_DEFAULT_LOGGING_DATE_FORMAT))
        self.__logger.setLevel(logs_level) # set the effective level of the logger
        self.__logger.info(f"logger configured; logs level has been set to {logs_level}")

    @property
    def logger(self) -> logging.Logger:
        """ __logger property """
        return self.__logger

    @classmethod
    def create_handler(cls, type: str, **args) -> logging.Handler:
        """
        This class method creates a logging handler of a specified type with the given arguments

        Args:
          type (str): The type of handler to create.

        Returns:
          A handler object.
        """
        handler = None
        if type == "FileHandler": handler = logging.FileHandler(filename=args["file_path"])
        elif type == "SysLogHandler": handler = SysLogHandler(address=args["socket"])
        return handler

    def add_handler(self, handler: logging.Handler, handler_logs_level: str = _DEFAULT_LOGGING_LEVEL, format: str = _GENERAL_LOGGING_FORMAT, 
                    date_format: str = _DEFAULT_LOGGING_DATE_FORMAT) -> bool:
        """
        It adds a handler to the logger object; furthermore, it sets the logging level, format, and date format for the handler

        Args:
          handler (logging.Handler): The handler to add to the logger.
          handler_logs_level (str): The level of logs for the handler. Defaults to _DEFAULT_LOGGING_LEVEL
          format (str): the format if the logs for this handler. Defaults to _GENERAL_LOGGING_FORMAT
          date_format (str): the format of the logging date. Defaults to _DEFAULT_LOGGING_DATE_FORMAT

        Returns:
          A boolean value that indicates whether the procedure was successfull.
        """
        try:
            handler.setFormatter(logging.Formatter(fmt=format, datefmt=date_format))
            handler.setLevel(handler_logs_level)
            self.__logger.addHandler(handler)
            self.__logger.info(f"handler has been added to logger; handler level -> {handler_logs_level}")
            return True
        except Exception as e:
            self.__logger.error(f"something went wrong while setting logging handler -> {e}")
            return False

# End LogHandler Class
