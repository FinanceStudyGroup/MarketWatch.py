#!/usr/bin/python
# ------------------------------------------------------------------------------
# MarketWatch Launcher
# ------------------------------------------------------------------------------

# Import required packages
import sys, os, re, subprocess, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
# ------------------------------------------------------------------------------

driver = webdriver.Chrome()

# Restate the ticker symbol in lower case
Ticker = Ticker.lower()

# Link to the profile page
MarketWatch = ("https://www.marketwatch.com/investing/stock/"+Ticker+"/profile")

# Locate MarketWatch company profile page
driver.get(MarketWatch)

# Expand business description
#time.sleep(1)
Expand = driver.find_element_by_css_selector('#maincontent > div.block.sixwide.addgutter.companydescription.vanilla > h2 > input')
Expand.click()