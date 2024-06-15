import logging
import os
from datetime import datetime
from pathlib import Path

# Ensure logs directory exists
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Define log file name with current timestamp (using valid characters for Windows filenames)
log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
log_file_path = os.path.join(logs_dir, log_file)

# Configure logging to write to the log file
logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started and finall coding has started")
