#IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin .... 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC
#More Info here :-https://github.com/tg12/IG-Index-Scalping-Scraping-Bot
#And here :- https://www.reddit.com/r/UKInvesting/comments/7lx03l/python_ig_index_bot/

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import requests
import json
import logging
import sys
import urllib
from time import time, sleep
import random
import time as systime
from statistics import mean, median


#Joke here
#REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'

API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
API_KEY = '*****************************'
data = {"identifier":"****************","password": "****************"}

# FOR REAL....
# API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
# API_KEY = '********************************************'
# data = {"identifier":"**************************","password": "***************************"}

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

#DOW RALLY EVERYDAY AT 20:40 - 21:00GMT
now = datetime.datetime.now()
now_time = now.time()

#-------------THIS NEEDS CHANGING AT SOME POINT---------------------------
#-------------THIS NEEDS CHANGING AT SOME POINT---------------------------
#-------------THIS NEEDS CHANGING AT SOME POINT---------------------------
#-------------THIS NEEDS CHANGING AT SOME POINT---------------------------
#-------------THIS NEEDS CHANGING AT SOME POINT---------------------------

# if now_time >= datetime.time(5,30) and now_time <= datetime.time(16,30): # Day Trading
	# print ("CS.D.GBPUSD.TODAY.IP")
	# epic_id = "CS.D.GBPUSD.TODAY.IP"
# elif now_time >= datetime.time(23,30) and now_time <= datetime.time(5,29): #Overnight
	# print ("CS.D.USCGC.TODAY.IP")
	# epic_id = "CS.D.USCGC.TODAY.IP"
# elif now_time >= datetime.time(18,30) and now_time <= datetime.time(20,30): #Wall Street
	# print ("IX.D.DOW.DAILY.IP")
	# epic_id = "IX.D.DOW.DAILY.IP"
# else:
	# print ("DEFAULT/NO TRADE")
	# epic_id = "CS.D.USCSI.TODAY.IP"
	
#HACKY/Weekend Testing - DO NOT USE!!! UNLESS YOU KNOW WHAT YOU ARE DOING!!
#epic_id = "CS.D.BITCOIN.TODAY.IP" #Bitcoin
#epic_id = "IX.D.SUNFUN.DAILY.IP" #Weekend Trading
#epic_id = "CS.D.ETHUSD.TODAY.IP" #Ether
#epic_id = "CS.D.BCHUSD.TODAY.IP" #Bitcoin Cash

#LIVE TEST
#epic_id = "CS.D.USCGC.TODAY.IP" #Gold - OK, Not Great
#epic_id = "CS.D.USCSI.TODAY.IP" #Silver - NOT RECOMMENDED 
#epic_id = "IX.D.FTSE.DAILY.IP" #FTSE 100 - Within Hours only, Profitable
#epic_id = "IX.D.DOW.DAILY.IP" #Wall St - Definately Profitable between half 6 and half 8 GMT
epic_id = "CS.D.GBPUSD.TODAY.IP" # - Very Profitable 

# PROGRAMMABLE VALUES
# UNIT TEST FOR CRYPTO'S
# limitDistance_value = "1"
# orderType_value = "MARKET"
# size_value = "5"
# expiry_value = "DFB"
# guaranteedStop_value = True
# currencyCode_value = "GBP"
# forceOpen_value = True
# stopDistance_value = "250"

#UNIT TEST FOR OTHER STUFF
limitDistance_value = "1"
orderType_value = "MARKET"
size_value = "1"
expiry_value = "DFB"
guaranteedStop_value = True
currencyCode_value = "GBP"
forceOpen_value = True
stopDistance_value = "20" #Initial Stop loss, Worked out later per trade

base_url = REAL_OR_NO_REAL + '/markets/' + epic_id
auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

#DEBUG
# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

MARKET_ID = d['instrument']['marketId']

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

# #Calculate average number of pips moved per hour and take an average
# #Do this on an 24 hour basis once?? OR Do it each time??

# price_list = []
# base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR_4/3'
# # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
# auth_r = requests.get(base_url, headers=authenticated_headers)
# d = json.loads(auth_r.text)

# # print ("-----------------DEBUG-----------------")
# # print(auth_r.status_code)
# # print(auth_r.reason)
# # print (auth_r.text)
# # print ("-----------------DEBUG-----------------")

# for i in d['prices']:
	# ask_price = i['closePrice']['ask']
	# price_list.append(float(ask_price))

# avg_diff = [price_list[i+1]-price_list[i] for i in range(len(price_list)-1)]
# #DEBUG
# print ("AVG PIP MOVEMENT FOR EACH HOUR " + str(avg_diff))
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("MAX PIP MOVEMENT IN 24 HOURS : " + str(max(avg_diff)))
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# # STOP_LOSS_MULTIPLIER = int(max(avg_diff))

# if min(avg_diff) < 0:
	# STOP_LOSS_MULTIPLIER = min(avg_diff) * -1 
	# #STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER * random.randint(3,4) #B'cos you know
	# STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + int(size_value) 
	# print ("STOP_LOSS_MULTIPLIER : " + str(STOP_LOSS_MULTIPLIER))
# else:
	# #STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER * random.randint(3,4) #B'cos you know
	# STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + int(size_value) 
	# print ("STOP_LOSS_MULTIPLIER : " + str(STOP_LOSS_MULTIPLIER))


# #------------------------------------
# #------------------------------------
# #------------------------------------
# #------------------------------------

#NOTE - This code works out the value from the last few hours percent change wise. Then uses that as a guide to work out the percent change. 
#i.e Avoid low quality trades by checking the volume traded

vol_list = []
base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR/6'
# Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print ("-----------------DEBUG-----------------")
# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
# print ("-----------------DEBUG-----------------")

for i in d['prices']:
	ltv = i['lastTradedVolume']
	vol_list.append(int(ltv))

print ([((a - b) / a * 100) for a, b in zip(vol_list[::2], vol_list[1::2])])
avg_diff = ([((a - b) / a * 100) for a, b in zip(vol_list[::2], vol_list[1::2])])
#THIS IS THE CODE THAT WORKS - REF ONLY
#((list price - actual price) / (list price)) * 100%

#DEBUG
# print ("AVG VOLUME FOR EACH HOUR " + str(avg_diff))
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("MAX VOLUME IN 24 HOURS : " + str(max(avg_diff)))
# print ("MIN VOLUME IN 24 HOURS : " + str(min(avg_diff)))
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
# print ("--------------------------------------------------")
VOL_CHANGE_MULTI = mean(avg_diff)
print ("VOL_CHANGE_MULTI : " + str(VOL_CHANGE_MULTI))

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

#TO DO:
#-------------
#READ IN PRICE CHANGE ON DAY FOR THESE
#NEW YEARS EVE EVE TO DO:
#TEST FOR NEGATIVE MOVEMENT ALL DAY THEN CONVERT

#HACKY TO TEST
#-------------
#VOL_CHANGE_MULTI = 5
#STOP_LOSS_MULTIPLIER = 50

# Let's say 30 trades? Not to be too greedy.....
#MAIN PROGRAM LOOP STARTS HERE
#------------------------------------------------

TIME_WAIT_MULTIPLIER = 45
def percentage(part, whole):
  return (part * whole) / 100.0

for x in range(1,7):
	
	#systime.sleep(4)
	
	DO_A_THING = False
	while not DO_A_THING == True:
		try:
			systime.sleep(random.randint(1,9))
			price_list = []
			ltv_list = []
			
			base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/MINUTE/' + str(random.randint(9,15))
			# Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
			auth_r = requests.get(base_url, headers=authenticated_headers)
			d = json.loads(auth_r.text)
			# print ("-----------------DEBUG-----------------")
			# print(auth_r.status_code)
			# print(auth_r.reason)
			# print (auth_r.text)
			# print ("-----------------DEBUG-----------------")
			
			for i in d['prices']:
				ask_price = i['closePrice']['ask']
				ltv = i['lastTradedVolume']
				price_list.append(float(ask_price))
				ltv_list.append(int(ltv))

			#---------------------------------
			firstValue = price_list[0]
			lastValue = price_list[-1]
			#---------------------------------
			Start_Trading_Volume = ltv_list[0]
			End_Trading_Volume = ltv_list[-1]
			#---------------------------------
			
			avg_diff = [price_list[i+1]-price_list[i] for i in range(len(price_list)-1)]
			#print ("AVERAGE PIP MOVEMENT IN THIS TIME PERIOD : " + str(avg_diff))
			#print ("MAX PIP MOVEMENT IN THIS TIME PERIOD : " + str(max(avg_diff)))
			
			if min(avg_diff) < 0:
				STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + min(avg_diff) * -1  #Convert Negative to Positive
				STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + mean(avg_diff)
				#STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER * random.randint(3,4) #B'cos you know
				#STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + int(size_value) 
				print ("STOP_LOSS_MULTIPLIER : " + str(STOP_LOSS_MULTIPLIER))
			else:
				STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + mean(avg_diff)
				#STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER * random.randint(3,4) #B'cos you know
				#STOP_LOSS_MULTIPLIER = STOP_LOSS_MULTIPLIER + int(size_value) 
				print ("STOP_LOSS_MULTIPLIER : " + str(STOP_LOSS_MULTIPLIER))
				
				
			
			#DEBUG
			print ("-----------------")
			print (firstValue)
			print (lastValue)
			print ("-----------------")
			print ("Trade Volume : " + str(Start_Trading_Volume))
			print ("Trade Volume : " + str(End_Trading_Volume))
			print ("-----------------")
			
			#NOTE :-
			#Rule to add If volume increases when the price moves up or down, it is considered a price movement with strength.
			#Already Covered
			# if Start_Trading_Volume <= End_Trading_Volume and firstValue <= lastValue:
				# print ("Higher Volume")
				# print ("Higher Price")
				# #Go Long
			
			if Start_Trading_Volume < End_Trading_Volume and firstValue > lastValue:
				vol_percent = percentage(Start_Trading_Volume, End_Trading_Volume)
				#price_percent = percentage(firstValue, lastValue)
				price_percent = 100 * (float(lastValue) - float(firstValue)) / float(lastValue)
				price_percent = 100 * (float(firstValue) - float(lastValue)) / float(firstValue)
				#DEBUG - PRINT PERCENT CHANGE
				print ("Volume Change Percent : " + str(vol_percent))
				print ("Price Change Percent : " + str(price_percent))
				print ("Higher Volume")
				print ("Lower Price")
				print ("DIRECTION IS DOWN (SHORT)")
				
				if vol_percent > VOL_CHANGE_MULTI:
					DIRECTION_TO_TRADE = "SELL"
					DIRECTION_TO_CLOSE = "BUY"
					DIRECTION_TO_COMPARE = 'offer'
					DO_A_THING = True
					
			elif Start_Trading_Volume < End_Trading_Volume and firstValue < lastValue:
				vol_percent = percentage(Start_Trading_Volume, End_Trading_Volume)
				#price_percent = percentage(firstValue, lastValue)
				price_percent = 100 * (float(lastValue) - float(firstValue)) / float(lastValue)
				price_percent = 100 * (float(firstValue) - float(lastValue)) / float(firstValue)
				#DEBUG - PRINT PERCENT CHANGE
				print ("Volume Change Percent : " + str(vol_percent))
				print ("Price Change Percent : " + str(price_percent))
				#Long Candidate, Buyers require increasing numbers and increasing enthusiasm in order to keep pushing prices higher. 
				print ("Higher Volume")
				print ("Higher Price")
				print ("DIRECTION IS UP (LONG)")
				
				if vol_percent > VOL_CHANGE_MULTI:
					DIRECTION_TO_TRADE = "BUY"
					DIRECTION_TO_CLOSE = "SELL"
					DIRECTION_TO_COMPARE = 'bid'
					DO_A_THING = True
			elif int(Start_Trading_Volume) > int(End_Trading_Volume) and firstValue < lastValue:
				vol_percent = percentage(Start_Trading_Volume, End_Trading_Volume)
				#price_percent = percentage(lastValue, firstValue)
				price_percent = 100 * (float(lastValue) - float(firstValue)) / float(lastValue)
				price_percent = 100 * (float(firstValue) - float(lastValue)) / float(firstValue)
				#DEBUG - PRINT PERCENT CHANGE
				print ("Volume Change Percent : " + str(vol_percent))
				print ("Price Change Percent : " + str(price_percent))
				#Increasing price and decreasing volume show lack of interest, and this is a warning of a potential reversal.
				print ("Higher Price")
				print ("Lower Volume")
				print ("DIRECTION IS DOWN (SHORT)")
				
				if vol_percent > VOL_CHANGE_MULTI:
					DIRECTION_TO_TRADE = "SELL"
					DIRECTION_TO_CLOSE = "BUY"
					DIRECTION_TO_COMPARE = 'offer'
					DO_A_THING = True
			else:
				DO_A_THING = False
				print ("NO TRADE")
				systime.sleep(4)
				#DO NOT TRADE
				# print ("No Clear Direction of Trade/Trade on Client Sentiment")
				# base_url = REAL_OR_NO_REAL + '/clientsentiment/'+ MARKET_ID
				# auth_r = requests.get(base_url, headers=authenticated_headers)
				# d = json.loads(auth_r.text)
				# # DEBUG!!!!
				# print(auth_r.status_code)
				# print(auth_r.reason)
				# print (auth_r.text)
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
					
			#---------------------------------
			#---------------------------------
			#---------------------------------
			#---------------------------------
	
		except Exception as e:
			#print (e)
			DO_A_THING = False
			print ("ERROR READING PRICE - NO TRADE")
			systime.sleep(4)
	
	
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
	systime.sleep(2) #For some reason sleep here, Maybe just delay on IG Side??
	
	# the trade will only break even once the price of the asset being traded has surpassed the sell price (for long trades) or buy price (for short trades). 
	#READ IN INITIAL PROFIT
		
	base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
	auth_r = requests.get(base_url, headers=authenticated_headers)		
	d = json.loads(auth_r.text)
	
	
	# DEBUG
	# print(auth_r.status_code)
	# print(auth_r.reason)
	# print (auth_r.text)
	
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
			
			if DIRECTION_TO_TRADE == "SELL":
				PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
				PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
				print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
				systime.sleep(2) #Don't be too keen to read price
			else:
				PROFIT_OR_LOSS = float(d['market'][DIRECTION_TO_COMPARE] - float(d['position']['openLevel']))
				PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
				print ("Deal Number : " + str(x) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
				systime.sleep(2) #Don't be too keen to read price
				
			ARTIFICIAL_STOP_LOSS = int(size_value) * STOP_LOSS_MULTIPLIER
			ARTIFICIAL_STOP_LOSS = ARTIFICIAL_STOP_LOSS * -1 #Make Negative, DO NOT REMOVE!!
			# print (PROFIT_OR_LOSS)
			# print (ARTIFICIAL_STOP_LOSS)
			
			if PROFIT_OR_LOSS < ARTIFICIAL_STOP_LOSS:
				#CLOSE TRADE/GTFO
				print ("WARNING!! POTENTIAL DIRECTION CHANGE!!")
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
				#DEBUG
				print(r.status_code)
				print(r.reason)
				print (r.text)
				systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER)) #Obligatory Wait before doing next order
						
	except Exception as e:
		#print(e) #Yeah, I know now. 
		print ("ERROR : ORDER MIGHT NOT BE OPEN FOR WHATEVER REASON")
		#WOAH CALM DOWN! WAIT .... STOP LOSS MIGHT HAVE BEEN HIT
		systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER))
		pass
	
		#systime.sleep(1)
			
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
		
		systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER)) #Obligatory Wait before doing next order
