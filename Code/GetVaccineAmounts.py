import pandas as pd
import numpy as np

s = 'vaccine_supply.csv' #Renamed from Hanuel's file
p ='census_data.csv' #Sneha's file

#Read vaccine supply data into surplus df
surplus = pd.read_csv(s)
surplus.rename(columns={'Secured and/or Expected Vaccine Supply in total doses (% of population)': 'VaxPortion'}, inplace = True)
surplus['VaxPortion'].replace(np.nan, 0, inplace = True)

#Read census data into population df
population = pd.read_csv(p)

#Merge census and vaccine data into df on 3-letter country codes
df = population.merge(surplus, left_on= 'CCA3', right_on = 'ISO-3 Code')
print(str(len(surplus.index) - len(population.index))+" rows dropped")

df['VaxCount'] = round(df['2022 Population'] * df['VaxPortion'] / 100,0) #get vaccine count
df['VaxGap'] = df['VaxCount'] - df['2022 Population'] #Get shortage (or overage) of vaccines. Negative is a shortage, positive is a surplus

df['S/D'] = np.where(df['VaxGap']>= 0, 'Surplus', 'Deficit')

df[['CCA3', 'VaxCount', 'VaxGap', 'S/D']].to_csv('country_pop_and_vax.csv')