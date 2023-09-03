"""
Tesheen Singh, September 2, 2023 Week 2 - Project 2

Purpose: Illustrate the built-in statistics module. """

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# Import from Python Standard Library

import statistics
import sys

# univariant data (one variable, many readings)

age_data = [19, 23, 63, 22, 19, 25, 35, 40, 20, 6 ]

logger.info("age_data = " + str(age_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(age_data)
median = statistics.median(age_data)
mode = statistics.mode(age_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(age_data)
stdev = statistics.stdev(age_data)
lowest = min(age_data)
highest = max(age_data)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    = {var: .2f}")
logger.info(f"stdev  = {stdev: .2f}")
logger.info(f"lowest = {lowest: .2f}")
logger.info(f"highest= {highest: .2f}")

