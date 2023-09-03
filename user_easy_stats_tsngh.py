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