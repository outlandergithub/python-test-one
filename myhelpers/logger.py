import logging
import traceback

print("First output from logger.py file")

logger = logging.getLogger(__name__)
logger.error("ERROR from misc logger ----------------------------------------")

try:
    a = [1,2,3]
    val = a[3]
    print("TRY from misc logger ----------------------------------------")
except:
    logging.error("The error is %s", traceback.format_exc())

print("Last output from logger.py file")