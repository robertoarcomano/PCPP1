"""
1 root logger -> getLogger
2 Several calls to the getLogger function with the same name will always return the same object.
3 Levels:
    3.1 CRITICAL	50
    3.2 ERROR	40
    3.3 WARNING	30
    3.4 INFO	20
    3.5 DEBUG	10
    3.6 NOTSET	0
    3.7 You can also define your own level,
4 The root logger has the logging level set to WARNING.
  This means that messages at the INFO or DEBUG levels aren't processed.
5 basicConfig for basic config
6 setLevel, level is inherited
7 basicConfig(level, filename)
8 Changing the format:
    8.1 %(name)s – this pattern will be replaced by the name of the logger that calls the logging method. In our case, it's the root logger;
    8.2 %(levelname)s – this pattern will be replaced with the set login level. In our case, this is the CRITICAL level;
    8.3 %(asctime)s – this pattern will be replaced with a human-readable date format that indicates when the LogRecord object was created. The decimal value is expressed in milliseconds;
    8.4 %(message)s – this pattern will be replaced by the defined message. In our case, it's 'Your CRITICAL message'.
8 FileHandler class for specifying a file log
9 Handlers can save to a file or send to an external service
10 Creating and adding a new Formatter
"""
import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, filename="log", format=FORMAT)
logger = logging.getLogger()
print("logger.level:", logger.level)
logger.setLevel(logging.DEBUG)
logger.critical("My critical message")
logger.info("My info message")
new = logging.getLogger("New")
print("new.level:", new.level)

handler = logging.FileHandler("log1")
formatter = logging.Formatter('%(name)s:%(levelname)s:%(asctime)s:%(message)s')
handler.setFormatter(formatter)
logger1 = logging.getLogger("logger1")
logger1.addHandler(handler)

logger1.setLevel(logging.CRITICAL)
logger1.info("info")
logger1.critical("critical")

