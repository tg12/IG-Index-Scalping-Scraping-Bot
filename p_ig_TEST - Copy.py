#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TO DO's
#Find a better way of setting epic, Rather than the Hacky AF way I do it now. It's OK for now. 

import random
import time
import datetime
import requests
import json
import logging
import sys
import urllib
import time
import random

#JUST USED TO FOR LINUX TO CHANGE COLORS OR TERMINAL
W  = '\033[0m'# white (normal)
R  = '\033[31m'# red
G  = '\033[32m'# green
O  = '\033[33m'# orange
B  = '\033[34m'# blue
P  = '\033[35m'# purple

#Joke here
#REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'

API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
API_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
data = {"identifier":"<<YOUR USERNAME HERE>>>","password": "<<YOUR PASSWORD HERE>>"}

# FOR REAL....
#API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
#API_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#data = {"identifier":"<<YOUR USERNAME HERE>>>","password": "<<YOUR PASSWORD HERE>>"}

headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'Version':'2'
		}

r = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)
 
headers_json = dict(r.headers)
CST_token = headers_json["CST"]
print (R"CST : " + CST_token)
x_sec_token = headers_json["X-SECURITY-TOKEN"]
print (R"X-SECURITY-TOKEN : " + x_sec_token)

#GET ACCOUNTS
base_url = REAL_OR_NO_REAL + '/accounts'
authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'CST':CST_token,
		'X-SECURITY-TOKEN':x_sec_token}

auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

for i in d['accounts']:
	if str(i['accountType']) == "SPREADBET":
		print ("Spreadbet Account ID is : " + str(i['accountId']))
		spreadbet_acc_id = str(i['accountId'])

#SET SPREAD BET ACCOUNT AS DEFAULT
base_url = REAL_OR_NO_REAL + '/session'
data = {"accountId":spreadbet_acc_id,"defaultAccount": "True"}
auth_r = requests.put(base_url, data=json.dumps(data), headers=authenticated_headers)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
#ERROR about account ID been the same, Ignore! 

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************
#--------------------FIND OUT WHAT MARKETS ARE OPEN (Weekend)-------
#This is pointless and likely to exceed your API Allowance
#Code left for posterity


# base_url = REAL_OR_NO_REAL + '/marketnavigation'
# auth_r = requests.get(base_url, headers=authenticated_headers)
# d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

# for i in d['nodes']:
	# print("name : " + str(i['name']))
	# print("id : " + str(i['id']))
	# NODE_TO_SEARCH = i['id']
	# print("----------")
	# base_url = REAL_OR_NO_REAL + '/marketnavigation/'+ NODE_TO_SEARCH
	# auth_r = requests.get(base_url, headers=authenticated_headers)
	# e = json.loads(auth_r.text)
	# for j in e['nodes']:
		# print("name : " + str(j['name']))
		# print("id : " + str(j['id']))
		# NODE_TO_SEARCH = j['id']
		# base_url = REAL_OR_NO_REAL + '/marketnavigation/'+ NODE_TO_SEARCH
		# auth_r = requests.get(base_url, headers=authenticated_headers)
		# e = json.loads(auth_r.text)
		# print(auth_r.status_code)
		# print(auth_r.reason)
		# print (auth_r.text)


#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

# search_term = "Bitcoin Cash"
# base_url = REAL_OR_NO_REAL + '/markets?searchTerm='+ search_term
# auth_r = requests.get(base_url, headers=authenticated_headers)
# d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

# for i in d['markets']:
	# print("High : " + str(i['high']))
	# print("----------")
	# print("Low : " + str(i['low']))
	# print("----------")
	# print("Bid : " + str(i['bid']))
	# print("----------")
	# print("Offer : " + str(i['offer']))
	# print("----------")
	# if str(i['marketStatus']) == "TRADEABLE":
		# print("Status : " + str(i['marketStatus']))
		# print("----------")
		# print("Epic : " + str(i['epic']))
		# print("----------")
	
#epic_id = str(i['epic'])

#HACKY
#epic_id = "CS.D.BITCOIN.TODAY.IP" #Bitcoin
#epic_id = "IX.D.SUNFUN.DAILY.IP" #Weekend Trading
#epic_id = "CS.D.ETHUSD.TODAY.IP" #Ether
#epic_id = "CS.D.BCHUSD.TODAY.IP" #Bitcoin Cash

#LIVE TEST
epic_id = "CS.D.USCGC.TODAY.IP" #Gold


#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

# price_list = []
# ltv_list = []
# time.sleep(2)
# base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR/4'
# # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
# auth_r = requests.get(base_url, headers=authenticated_headers)
# d = json.loads(auth_r.text)

# #DEBUG
# # print(auth_r.status_code)
# # print(auth_r.reason)
# # print (auth_r.text)
	
# for i in d['prices']:
	# #print(i['snapshotTime'])
	# #print(i['lastTradedVolume'])
	# ask_price = i['closePrice']['ask']
	# ltv = i['lastTradedVolume']
	# price_list.append(ask_price)
	# ltv_list.append(ltv)

# #---------------------------------
# firstValue = price_list[0]
# lastValue = price_list[-1]
# #---------------------------------
# Start_Trading_Volume = ltv_list[0]
# End_Trading_Volume = ltv_list[-1]
# #---------------------------------

# print (Start_Trading_Volume)
# print (End_Trading_Volume)
		
# if Start_Trading_Volume < End_Trading_Volume:
	# print ("Higher Volume")
	# if firstValue <= lastValue:
		# #Long Candidate, Buyers require increasing numbers and increasing enthusiasm in order to keep pushing prices higher. 
		# print ("Higher Price")
		# print ("DIRECTION IS UP (LONG)")
		# DIRECTION_TO_TRADE = "BUY"
		# DIRECTION_TO_CLOSE = "SELL"
		# DIRECTION_TO_COMPARE = 'bid'
	# else:
		# print ("DIRECTION IS DOWN (SHORT)")
		# DIRECTION_TO_TRADE = "SELL"
		# DIRECTION_TO_CLOSE = "BUY"
		# DIRECTION_TO_COMPARE = 'offer'
# else:
	# print ("Lower Volume")
	# if firstValue <= lastValue:
		# #Increasing price and decreasing volume show lack of interest, and this is a warning of a potential reversal.
		# print ("Higher Price")
		# print ("DIRECTION IS DOWN (SHORT)")
		# DIRECTION_TO_TRADE = "SELL"
		# DIRECTION_TO_CLOSE = "BUY"
		# DIRECTION_TO_COMPARE = 'offer'
	# else:
		# print ("DIRECTION IS DOWN (SHORT)")
		# DIRECTION_TO_TRADE = "SELL"
		# DIRECTION_TO_CLOSE = "BUY"
		# DIRECTION_TO_COMPARE = 'offer'

			
#A Note on this, Trading Volume should be higher than when you first read it into the list, Then price should move accordingly. If not then this signifies a potential reversal
#Quite proud of this bit of code above

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************
#ALTERNATIVE DIRECTION
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

# base_url = REAL_OR_NO_REAL + '/clientsentiment/'+ marketId
# auth_r = requests.get(base_url, headers=authenticated_headers)
# d = json.loads(auth_r.text)

# # DEBUG!!!!
# # print(auth_r.status_code)
# # print(auth_r.reason)
# # print (auth_r.text)

# long_sent = d['longPositionPercentage']
# short_sent = d['shortPositionPercentage']

# if long_sent > short_sent:
	# DIRECTION_TO_TRADE = "BUY"
	# DIRECTION_TO_CLOSE = "SELL"
	# DIRECTION_TO_COMPARE = 'bid'
# else:
	# DIRECTION_TO_TRADE = "SELL"
	# DIRECTION_TO_CLOSE = "BUY"
	# DIRECTION_TO_COMPARE = 'offer'
	

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

# PROGRAMMABLE VALUES
# UNIT TEST FOR BITCOIN
# limitDistance_value = "1"
# orderType_value = "MARKET"
# size_value = "5"
# expiry_value = "DFB"
# guaranteedStop_value = True
# currencyCode_value = "GBP"
# forceOpen_value = True
# stopDistance_value = "1200"
# NOTE :- HOW TO GET MIN STOP DISTANCE WITH GUARANTEED STOP????????????

# #UNIT TEST FOR GOLD
limitDistance_value = "1"
orderType_value = "MARKET"
size_value = "10"
expiry_value = "DFB"
guaranteedStop_value = True
currencyCode_value = "GBP"
forceOpen_value = True
stopDistance_value = "30"


# Let's say 30 trades? Not to be too greedy.....
#MAIN PROGRAM LOOP STARTS HERE

for x in range(1,30):
	
	price_list = []
	ltv_list = []
	
	if x == 1:
		base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR/4'
	else:
		base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR/' + str(x)
		# Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
	
	auth_r = requests.get(base_url, headers=authenticated_headers)
	d = json.loads(auth_r.text)
	
	for i in d['prices']:
		ask_price = i['closePrice']['ask']
		ltv = i['lastTradedVolume']
		price_list.append(ask_price)
		ltv_list.append(ltv)

	#---------------------------------
	firstValue = price_list[0]
	lastValue = price_list[-1]
	#---------------------------------
	Start_Trading_Volume = ltv_list[0]
	End_Trading_Volume = ltv_list[-1]
	#---------------------------------
	
	print (Start_Trading_Volume)
	print (End_Trading_Volume)

	if Start_Trading_Volume <= End_Trading_Volume:
		print ("Higher Volume")
		if firstValue <= lastValue:
			#Long Candidate, Buyers require increasing numbers and increasing enthusiasm in order to keep pushing prices higher. 
			print ("Higher Price")
			print ("DIRECTION IS UP (LONG)")
			DIRECTION_TO_TRADE = "BUY"
			DIRECTION_TO_CLOSE = "SELL"
			DIRECTION_TO_COMPARE = 'bid'
		else:
			print ("DIRECTION IS DOWN (SHORT)")
			DIRECTION_TO_TRADE = "SELL"
			DIRECTION_TO_CLOSE = "BUY"
			DIRECTION_TO_COMPARE = 'offer'
	else:
		print ("Lower Volume")
		if firstValue <= lastValue:
			#Increasing price and decreasing volume show lack of interest, and this is a warning of a potential reversal.
			print ("Higher Price")
			print ("DIRECTION IS DOWN (SHORT)")
			DIRECTION_TO_TRADE = "SELL"
			DIRECTION_TO_CLOSE = "BUY"
			DIRECTION_TO_COMPARE = 'offer'
		else:
			print ("DIRECTION IS DOWN (SHORT)")
			DIRECTION_TO_TRADE = "SELL"
			DIRECTION_TO_CLOSE = "BUY"
			DIRECTION_TO_COMPARE = 'offer'
			
	#---------------------------------
	#---------------------------------
	#---------------------------------
	#---------------------------------
	
	base_url = REAL_OR_NO_REAL + '/positions/otc'
	authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
			'Accept':'application/json; charset=utf-8',
			'X-IG-API-KEY':API_KEY,
			'CST':CST_token,
			'X-SECURITY-TOKEN':x_sec_token}
			
	data = {"direction":DIRECTION_TO_TRADE,"epic": epic_id, "limitDistance":limitDistance_value, "orderType":orderType_value, "size":size_value,"expiry":expiry_value,"guaranteedStop":guaranteedStop_value,"currencyCode":currencyCode_value,"forceOpen":forceOpen_value,"stopDistance":stopDistance_value}
	r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers)
	# MAKE AN ORDER
	d = json.loads(r.text)
	deal_ref = d['dealReference']
	#CONFIRM MARKET ORDER
	base_url = REAL_OR_NO_REAL + '/confirms/'+ deal_ref
	auth_r = requests.get(base_url, headers=authenticated_headers)
	d = json.loads(auth_r.text)
	DEAL_ID = d['dealId']
	print("DEAL ID : " + str(d['dealId']))
	print(d['dealStatus'])
	print(d['reason'])
	
	# the trade will only break even once the price of the asset being traded has surpassed the sell price (for long trades) or buy price (for short trades). 
	#READ IN INITIAL PROFIT
		
	base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
	auth_r = requests.get(base_url, headers=authenticated_headers)		
	d = json.loads(auth_r.text)
	
	if DIRECTION_TO_TRADE == "SELL":
		PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
		PROFIT_OR_LOSS = PROFIT_OR_LOSS * float(size_value)
		print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
	else:
		PROFIT_OR_LOSS = float(d['market'][DIRECTION_TO_COMPARE] - float(d['position']['openLevel']))
		PROFIT_OR_LOSS = PROFIT_OR_LOSS * float(size_value)
		print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
		
	
	#KEEP READING IN FOR PROFIT
	try:
		while PROFIT_OR_LOSS < 0.1: #Over 10p otherwise not worth it and price could move
			base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
			auth_r = requests.get(base_url, headers=authenticated_headers)		
			d = json.loads(auth_r.text)
			
			#Add artificial stop loss code here - 27/12
			#Check Profit/Loss against size values
			
						
			if DIRECTION_TO_TRADE == "SELL":
				PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
				PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
				print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
				time.sleep(3) #Don't be too keen to read price
			else:
				PROFIT_OR_LOSS = float(d['market'][DIRECTION_TO_COMPARE] - float(d['position']['openLevel']))
				PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
				print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
				time.sleep(3) #Don't be too keen to read price
						
	except Exception as e:
		#print(e) #Yeah, I know now. 
		print ("ERROR : ORDER MIGHT NOT BE OPEN FOR WHATEVER REASON")
		#WOAH CALM DOWN! WAIT .... STOP LOSS MIGHT HAVE BEEN HIT
		time.sleep(random.randint(1, 10))
		pass
	
		time.sleep(1)
			
	if PROFIT_OR_LOSS > 0:
		print ("ASSUME PROFIT!!")
		SIZE = size_value
		ORDER_TYPE = orderType_value
		
		base_url = REAL_OR_NO_REAL + '/positions/otc'
		data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
		#authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
		authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
				'Accept':'application/json; charset=utf-8',
				'X-IG-API-KEY':API_KEY,
				'CST':CST_token,
				'X-SECURITY-TOKEN':x_sec_token,
				'_method':"DELETE"}
		
		auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete)	
		#CLOSE TRADE
		print(r.status_code)
		print(r.reason)
		print (r.text)
		
		# #CONFIRM CLOSE - FUTURE
		# base_url = REAL_OR_NO_REAL + '/confirms/'+ deal_ref
		# auth_r = requests.get(base_url, headers=authenticated_headers)
		# d = json.loads(auth_r.text)
		# DEAL_ID = d['dealId']
		# print("DEAL ID : " + str(d['dealId']))
		# print(d['dealStatus'])
		# print(d['reason'])
		
		time.sleep(random.randint(1, 10)) #Obligatory Wait before doing next order
