#!/usr/bin/env python

import os
#import pyttsx #for the text to speach later
import datetime
from MetOfficeObservationData import latestObservationData #the shizzle for current data

# pulls in the latest reported observations 3772 is heathrow, closest location to wandsworth
observationURL = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3772?res=hourly&key=

#just grabs the day and night forcast 354361 is for wimbledon
forecastURL = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354361?res=daily&key=

#not likely to be used grabs the 3 hourly forcast 354361 is for wimbledon
forecast3HourlyURL = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354361?res=3hourly&key=

#grab the observation data
observationData = AllObservationData(observationURL)
for i in observationData:
	print i
#grab the forcast
forecastData = json.load(urllib.urlopen(forecastURL))

