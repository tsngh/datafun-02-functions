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

# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (day) is independent and
# y is dependent on x (e.g. miles biked)
xday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
yvalues = [35, 25, 18, 50, 0, 45, 25, 27, 18, 20, 20, 32, 15, 0, 12]

# if the lists are not the same size,
# log an error and quit the program
if len(xday) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xday)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xday, xday)
xy_corr = statistics.correlation(xday, yvalues)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xday}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

print( 'Done.')