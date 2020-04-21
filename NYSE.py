import logging, json, os, time, sched, random, json, csv, datetime, lxml
import yfinance as yf
import requests
from ruxit.api.base_plugin import RemoteBasePlugin
import msvcrt as m

dt = yf.Ticker("DT")

class DynatraceNYSE(RemoteBasePlugin):

    def initialize(self, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info("Config: %s", self.config)
      
        
    def query(self, **kwargs):
        #Create topology

        group = self.topology_builder.create_group("Stock Info", "Stock Info")

        device = group.create_device("Dynatrace", "Dynatrace")
        device.absolute(key='dayHigh', value=float(dt.info['dayHigh']))
