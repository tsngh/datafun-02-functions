"""
Tesheen Singh, September 2, 2023 Week 2 - Project 2

Purpose: Illustrate the math module and how to write
mathematical functions by trying them.

Import the math module.

Steal the logging setup code from any of the examples.

Define at least one function that you might use in your domain - a simple reusable math function. 
For example: get_area_of_rectangle(height, width). Change the name of the function to something in 
your domain - the size of CD case, the size of a parking lot, or advertisement, etc. 

Implement the function to calculate the correct area. 

"""
import math

#Steal the logging setup code from any of the examples; taken from defensive_math.py

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

#Define one function that you might use in your domain (we are going to pretend all countries are square and small) units are in km

import statistics as stats

def area_of_country(height, width):
    """
    Return area of a country given by its height and width.

    """
    try: 
        area = height * width
        logger.info(f"The area of the country is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

#Use the defensive math examples to call the permutations and combinations as shown

if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

#Then, call the method you just created with several different arguments. For example, 
#call get_area_of_rectangle(6, 2) and display the result. Call it again with different values for height and width.

logger.info("TRY: Call area_of_country() function with a different values.")
area_of_country (250, 150)
area_of_country (150, 100)
area_of_country (100, 200)
logger.info("")

#Add three more simple functions that might be useful to your domain. At least one must call a function from the math module, for example, math.fsum(). 

#1
logger.info("TRY: Call area_of_country() function with exact values")
exact_area = [25000.23]
print(math.ceil(25000.23))
logger.info("")

#2
logger.info("TRY: Call country_annual_temp_average() funtion with average annual temperature (F) over a year")
greece_temps = [46.8, 48.3, 53, 59.5, 68.6, 77.3, 81.9, 81.4, 73.9, 65.4, 57.3, 49.8]
country_annual_temp_average = (sum(greece_temps)/len(greece_temps))
logger.info(f"country_annual_temp_average   = {country_annual_temp_average:.2f}")

#3
logger.info("TRY: Call get_country_areas_given_list() function with a list that may include BAD values")
bad_list = [-500, 0, math.inf, '30']
get_country_areas_given_list= (bad_list) 

print("Done. Please check the log file for more details.")