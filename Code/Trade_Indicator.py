import pandas as pd
import csv

#Ind1 is the share of IMPORTS from SELECTED COUNTRY
#Ind2 is the share of EXPORTS from the SELECTED COUNTRY
#Ind3 is the imports from OTHER ECONOMIES
#Ind4 is the share of exports froms OTHER ECONOMIES
file = 'data.csv' #large file with trade data
reporter = 'selected_economy.csv' #codes for reporter countries
partner ='other_economy.csv' #code for partner countries

trade_data = pd.read_csv(file)
trade_data['CountryPair'] = trade_data['Reporter'] + trade_data['Partner'] #use this column to join datasets later if needed
trade_data['Trade_Indicator'] = trade_data['Ind1'] + trade_data['Ind4'] #share of exports from reporter country + share of imports from partner country
trade_data = trade_data[['Partner', 'Reporter', 'Trade_Indicator', 'CountryPair', 'L3']]

all_products = trade_data[trade_data['L3']=='000'].copy() ##All products code is 000
medical = trade_data[trade_data['L3'].isin(['N03', 'M03'])].copy()#pharmecutical and medical supplies
medical = medical.groupby(by=['Reporter','Partner'], dropna=False).sum()
medical.reset_index(inplace = True)

#get codes for reporter countries
report_dict = {}
with open(reporter,'r') as data:
   for line in csv.reader(data):
       report_dict[line[0]] = line[1]

#get codes for partner countries
partner_dict ={}
with open(partner,'r') as data:
   for line in csv.reader(data):
       partner_dict[line[0]] = line[2]

all_products.replace(to_replace = {'Reporter': report_dict, 'Partner' : partner_dict}, inplace = True)
medical.replace(to_replace = {'Reporter': report_dict, 'Partner' : partner_dict}, inplace = True)

all_products.to_csv('trade_partners_all_products.csv')
medical.to_csv('trade_partners_medical_pharma.csv')
