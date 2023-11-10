import pandas as pd

file = 'country_pop_and_vax.csv' #file with country population and number of vaccines available
df = pd.read_csv(file)

#Import pair scores as a dictionary
file2 = 'normdata.csv' #file with country scores
pair_score = {}
n = 0
with open(file2, 'r', encoding='utf-8') as score_file:
    for line in score_file:
        if n > 0:
            pair = line.split(",")
            pair_name = pair[2]+pair[1] #Reporter Country -> Partner
            pair_score[pair_name] = float(pair[8].strip()) #turn score to float
        n += 1

#get dictionary of number of vaccine surplus / deficit
vax_gap ={}
for row in df.iterrows():
    vax_gap[row[1][1]]  = row[1][3] #get country code and vax gap in dictionary

#split countries by surplus or deficit
surplus = df[df['S/D'] == 'Surplus'].copy()
deficit = df[df['S/D'] == 'Deficit'].copy()

deficit.set_index('CCA3', inplace = True) #set the CCA3 code as index so you can drop the rows after the deficit is filled

#Dictionary to collect ideal pairs
pair_list = {'Supplier': [], 'Receiver': [], 'Amount': []}

#find ideal pair

for d in deficit.index:
    best_score = float('-inf')
    ideal_supplier = ''
    for s in surplus['CCA3']:
        if vax_gap[s] + vax_gap[d] >=0: #if surplus is bigger than deficit, countries are viable
            current_pair = s+d
            try:
                current_score = pair_score[current_pair] #check if country pair has a score
                status = 'assigned'
            except:
                current_score = float('-inf') #if not, give it worst possible score
                status = 'unassigned'
            if current_score >= best_score: #the higher score is better.
                ideal_supplier = s


    gap = vax_gap[d] #Amount of vacciness to be transfered
    pair_list['Supplier'].append(ideal_supplier) #add supplier to pair list
    pair_list['Receiver'].append(d) #add reciever to pair list
    pair_list['Amount'].append(gap*-1) #add amount to pair list
    vax_gap[s] += gap #remove transferred vaccines from supplier amount
    surplus = surplus.sample(frac=1, random_state = 200).reset_index(drop=True) #shuffle surplus countries so last one isn't always picked
    try:
        deficit.drop(index = ideal_receiver, inplace = True)
    except:
        pass

results = pd.DataFrame.from_dict(pair_list)
results.to_csv('ideal_pairs.csv')

