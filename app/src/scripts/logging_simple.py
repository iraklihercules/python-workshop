import logging

logging.basicConfig(
    # filename='output.log',  # Logging to a File
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.critical("My message 1")
# 2024-05-09 00:00:00,000 - CRITICAL - My message 1

logging.disable(logging.CRITICAL)
logging.critical("My message 2")  # Silenced
