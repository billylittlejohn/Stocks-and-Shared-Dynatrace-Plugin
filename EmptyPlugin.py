import logging, json, os, time, sched, random, json, csv, datetime, lxml
import yfinance as yf
import requests
from ruxit.api.base_plugin import RemoteBasePlugin #This must be imported for the plugin to work 
import msvcrt as m

dt = yf.Ticker("DT") #This tells the API what companies data we want to pull back, you can change this to any NYSE ticker symbol

class DynatraceNYSE(RemoteBasePlugin): #For the plugin to work, you must pass in the RemoteBasePlugin parameter

    def initialize(self, **kwargs): #For the plugin to work, you must specify a initialize function 
        logger = logging.getLogger(__name__)
        logger.info("Config: %s", self.config)
      
        
    def query(self, **kwargs): # For the plugin to work, you must specify a query funciton 
        group = self.topology_builder.create_group("Stock Info", "Stock Info") #This will create the device group that you will see in the Dynatrace UI in the Technologies page
        device = group.create_device("Dynatrace", "Dynatrace") #This row will create the device which will appear in the group
        device.absolute(key='dayHigh', value=float(dt.info['dayHigh'])) #This row takes the DailyHigh value from the API, you can see all available metrics from this API by running 'print(dt.info)'. This also saves the result of the metric with the key 'dayHigh' which will be referenced in the JSON.
        
