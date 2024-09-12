"""
from visa_approval.logger import logging
from visa_approval.exception import USvisaException
import sys

logging.info("Welcome to Custom Log(For Testing purpose).")

try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)

"""


"""
import os
mongo_db_url=os.getenv('MONGODB_URL')
print(mongo_db_url)
"""

from visa_approval.pipline.training_pipeline import TrainingPipeline

obj=TrainingPipeline()

obj.run_pipeline()