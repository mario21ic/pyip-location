#!/usr/bin/env python

import requests
import subprocess
import sys
import os

import logging
import json

from urllib.parse import urlparse

logging.basicConfig(filename='pyip.log', filemode='w', \
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
    level=logging.DEBUG)

def main():
    print("## Start ##")

    file_input = open("ips.txt", 'r')
    token = os.environ["GEO_TOKEN"]
    
    for ip in file_input.readlines():
        ip = ip.strip()
        url = ("https://api.ip2location.com/v2/?ip=%s&key=%s&package=WS25" % (ip, token))
        response = requests.get(url)
        response_json = response.json()
        print("=====")
        print("ip:", ip)
        print("code:", response_json['country_code'])
        print("country:", response_json['country_name'])
    """ {
	"country_code":"PE",
	"country_name":"Peru",
	"region_name":"Lima",
	"city_name":"Lima",
	"latitude":"-12.043333",
	"longitude":"-77.028333",
	"zip_code":"15000",
	"time_zone":"-05:00",
	"isp":"Telefonica del Peru S.A.A.",
	"domain":"telefonica.com.pe",
	"net_speed":"DSL",
	"idd_code":"51",
	"area_code":"01",
	"weather_station_code":"PEXX0011",
	"weather_station_name":"Lima",
	"mcc":"716",
	"mnc":"06",
	"mobile_brand":"Movistar",
	"elevation":"155",
	"usage_type":"ISP/MOB",
	"address_type":"U",
	"category":"IAB19-18",
	"category_name":"Internet Technology",
	"credits_consumed":20
    } """
    return


if __name__=="__main__":
  main()
