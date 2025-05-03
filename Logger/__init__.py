import os
import sys
import logging
import colorlog
from Model_Configuration.Model_Constants import CONFIG_FILE_PATH
from Utils.utils import read_yaml, create_directories

logging_str="%(log_color)s%(asctime)s: %(levelname)s: %(module)s: %(message)s"

project_name = read_yaml(CONFIG_FILE_PATH).project_details.name
log_dir=f"logs/{project_name}"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
print("logger")


logging.basicConfig(
    level=logging.INFO,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger(f"{project_name}logger")

logger.setLevel(logging.DEBUG)

# Create a console handler
handler = colorlog.StreamHandler()

# Define a colored formatter
formatter = colorlog.ColoredFormatter(
   logging_str,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
)

# Apply formatter to handler
handler.setFormatter(formatter)
logger.addHandler(handler)