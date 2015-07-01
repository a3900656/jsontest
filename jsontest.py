import json
import re
from pprint import pprint

with open('/Users/ken/Desktop/jsontest/_User.json') as data_file:    
    data = json.load(data_file)
male = 0.0
female = 0.0
gay = 0.0
pat='2015-06'
pat2 = '2015-05'
for gender in data["results"]:
	try:
		if re.search(pat,gender["updatedAt"]):
			print(gender["nickname"])
			print(gender["createdAt"])
			print(gender["updatedAt"])
			print("-----------------")
			gay=gay+1
	except:
		continue
		# gay = gay+1
# print("male number",male,"persent:",male/(male+female)*100)
# print("female number",female,"persent:",female/(male+female)*100)
print("gay number",gay)

year_20 = 0.0
year_20_30=0.0
year_30_40=0.0
year_40_50=0.0
year_50=0.0

for age in data["results"]:
	try:
		if (2015-age['birthYear'])>50:
			year_50 = year_50+1
		elif (2015-age['birthYear'])>40 and (2015-age['birthYear'])<50:
			year_40_50 = year_40_50+1
		elif (2015-age['birthYear'])>30 and (2015-age['birthYear'])<40:
			year_30_40 = year_30_40+1
		elif (2015-age['birthYear'])>20 and (2015-age['birthYear'])<30:
			year_20_30 = year_20_30+1
		elif (2015-age['birthYear'])<20:
			year_20 = year_20+1
	except:
		continue
age_tt = year_50+year_20_30+year_30_40+year_40_50+year_20;
print ("~~20 ",year_20," persent: ",year_20/age_tt*100)
print ("20~30 ",year_20_30," persent: ",year_20_30/age_tt*100)
print ("30~40",year_30_40," persent: ",year_30_40/age_tt*100)
print ("40~50",year_40_50," persent: ",year_40_50/age_tt*100)
print ("50~~",year_50," persent: ",year_50/age_tt*100)

weight = 0.0
height = 0.0
thin = 0.0
normal = 0.0
upnormal = 0.0
fat = 0.0
fater = 0.0
fattest = 0.0
for BMI in data["results"]:
	try:
		weight = BMI['weight']
		height = BMI['height']*1.0/100
		bmi =  weight/(height*height)
		if bmi<18.5:
			thin = thin+1
		elif 24>bmi>18.5:
			normal = normal+1
		elif 27>bmi>24:
			upnormal = upnormal+1
		elif 30>bmi>27:
			fat = fat+1
		elif 35>bmi>30:
			fater = fater+1
		elif bmi>35:
			fattest = fattest+1
			# print(BMI['nickname'])
		# print(bmi)
	except:
		continue

BMItt = thin + normal + upnormal + fat + fater +fattest
print ("below average:" ,thin ,thin/BMItt*100)
print ("normal :" ,normal,normal/BMItt*100)
print ("above average :",upnormal,upnormal/BMItt*100)
print ("fat :",fat,fat/BMItt*100)
print ("fater :",fater/BMItt*100)
print ("fattest :",fattest/BMItt*100)





















# pprint(data)