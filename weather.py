#!/usr/bin/python3
# Import libraries 

import requests
#import mastodon 
import os
import socket
import argparse
import datetime

# Purpose
# Retrieves weather data from the Wunderground API service
# And toots it at an interval and mastodon instance of your choosing

# TODO 
# APIKey arguments aren't filled out
# Add a TimeFunction and argument for Interval to poll Wunderground and toot

# Assign variables 
errorpath = "/home/justin/Documents/code/python/weather/weatherPy.error"
configpath = "/home/justin/Documents/code/python/weather/weatherPy.config"
apiKey = "#KEYDATA"

# File Handling Function
def filehandler(errormsg,errorpath):
    try:
        f = open(errorpath, "a")
        now = datetime.datetime.now()
        f.write("\n" + str(now) + " " + str(errormsg))
        f.close()
        print("Error written to " + errorpath + " successfully.")
        print("Exiting Gracefully")
        return True
    except:
        print("Unable to write to " + errorpath)
        print("\nCrashing Gracefully")
        return False

# Error Function 
def error(errormsg):
    print("Encountered Error: " + str(errormsg))
    print("Attempting to write to log at " + errorpath)
    try: 
        filehandler(errormsg,errorpath)
        exit()
    except:
        exit(1)

# FileChecker
def fileCheck(filepath):
    if not os.path.isfile(filepath):
        error(('File ' + filepath + ' does not exist.'))
        return False
    else:
        return True

# Parse Arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stationid", dest='stationid', type=str, default="KTNWHITW29", help="This is a StationID")
parser.add_argument("-u", "--units", dest='units', choices=['m','e','h'], default="m", help="Valid options are (e)nglish, (m)etric, or (h)ybrid UK, Metric is the default")
parser.add_argument("--precision", dest='precision', default=None, choices=['decimal', None],  help="Valid options are (decimal), integers will be returned by default")
parser.add_argument("-c", "--config", dest='config', default=configpath, help=("Valid file paths may be provided. Otherwise " + configpath + " will be used."))
parser.add_argument("--apiKey", )
args = parser.parse_args()
#print( "Station ID: {} \nUnits: {} \nPrecision: {} ".format(args.stationid,args.units,args.precision))



# Check Config File
fileCheck(args.config)

# Read File 
with open(args.config) as f:
    contents = f.read().splitlines()

for line in contents:
    print(line)


# Check connectivity 
def internet(host="8.8.8.8", port=53, timeout=3):
   
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        error(ex)
        return False

internet()

# Construct URL 
baseUrl = ("https://api.weather.com/v2/pws/observations/current?stationId="+str(args.stationID)+"&format=json&units="+args.units+"&apiKey="+args.Apikey)

# Get Weather 
# Use the IBM Docs Here, and the API Key 

# Toot Weather 

# Time Function



