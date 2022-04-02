"""
settings.py
-----------
This module provides package constants.
By: Sebastian D. Goodfellow, Ph.D.
"""

# Import 3rd party libraries
import os

# Set working directory
WORKING_PATH = (
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__)
        )
    )
)

# Set data directory
DATA_PATH = os.path.join(WORKING_PATH, 'data')

# Set base url
BASE_URL = 'http://pems.dot.ca.gov'

# Clearing house url
CLEARING_HOUSE_URL = '{}/?srq=clearinghouse&district_id={}&yy={}&type={}&returnformat=text'
# 
# https://pems.dot.ca.gov/?report_form=1&dnode=Freeway&content=spatial&tab=contours&export=xls&fwy=10&dir=W&s_time_id=1613692800&=02%2F19%2F2021&from_hh=0&to_hh=23&start_pm=.17&end_pm=239.92&lanes=&station_type=ml&q=flow&colormap=30%2C31%2C32&sc=auto&ymin=&ymax=&view_d=2

SPATIAL_TIMESERIES_URL = '{}/?report_form=1&dnode=Freeway&content=spatial&tab=contours&export=xls&fwy=10&dir=W&s_time_id={}&s_time_id_f={}&from_hh=0&to_hh=23&start_pm=.17&end_pm=239.92&lanes=&station_type=ml&q={}&colormap=30%2C31%2C32&sc=auto&ymin=&ymax=&view_d=2'

# Set available districts
DISTRICTS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
