# Import necessary libraries: os, sys, and logging.
import os
import sys
import logging

# Define a logging format string (logging_str) in a specific format that includes the date, time, log level, module, and log message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Set the log directory (log_dir) to "logs". Create the directory if it does not exist using os.makedirs(log_dir, exist_ok=True).
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system using logging.basicConfig():
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    # Specify two handlers for the logs:
    handlers=[
        # This handler writes the logs to the specified file.
        logging.FileHandler(log_filepath),
        # This handler writes the logs to the standard output (stdout).
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance (logger) with the name "cnnClassifierLogger". This logger instance will be used to write logs throughout the program.
logger = logging.getLogger("cnnClassifierLogger")
