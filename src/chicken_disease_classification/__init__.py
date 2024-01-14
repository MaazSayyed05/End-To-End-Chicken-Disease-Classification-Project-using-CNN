import os
import sys
import logging
from datetime import datetime

log_file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" #NAme of log file (date_month_year_hours_minutes_seconds)


logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'


log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, log_file_name)

logging.basicConfig( 
    level=logging.INFO, 
    format=logging_str,
    handlers = [
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)  ## print log in terminal
    ]
)

logger = logging.getLogger('chicken_disease_classifier_logger')




