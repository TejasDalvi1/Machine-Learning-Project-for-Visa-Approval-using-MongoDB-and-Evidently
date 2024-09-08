from visa_approval.logger import logging
from visa_approval.exception import USvisaException
import sys

logging.info("Welcome to Custom Log(For Testing purpose).")

try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)

