# DSKUS
This project was done in ‘2023 DSKUS’ program.The Data Science South Korea/US (DSKUS) Global Lab is a cross-national project between Hanyang University in Seoul, DePaul University, and Indiana University. The program is funded by a grant from the United States Embassy in Seoul (via the US State Department). Teams of students from the three universities work together to solve unique data science challenges with real-world implications
### Members
Members of Group 6 was Carolyn Haythorn(MS in Indianan University), Sneha Satish(MS in Indiana University), Haneul Kim(MS in Hanyang University), Yeeun Jeon(Junior in Hanyang University)

## Introduction
Our group was assigned the topic, “Mitigating disruptions in the global supply chain caused by the continued COVID-19 pandemic.” Many experts in the field emphasized the importance of preferentially recovering from COVID-19 in order to mitigate disruptions in the global supply chain. So our group specified the project topic as “Optimizing vaccine distribution in future pandemic situations.” During COVID-19, richer nations focused on being the first to develop and rolled out COVID-19 vaccines to their own populations, and it lead to emergence of the Omicron variant and its rapid spread. So our project is aiming to find ways for equal vaccine distribution in future pandemic. 

## EDA
We visualized the vaccination rates between countries, and analyzed vaccine manufacturing data. Also, we could find out the country relationships based on trade. By doing the EDA, we could find out that number of vaccinations is related to exports. 

## Datasets
We had 4 parts of datasets used in the project: 1) Country populations, 2) Possible Vaccine Supply datasets, 3) Trade Relationships, 4) Country Distances

## Model
These are the steps how we designed the model for equal vaccine distribution. 
(1) Divide all countries into those with vaccine surplus and vaccine deficits.
(2) For each country with a vaccine deficit, identify viable supply partners.
(3) Of all the viable supply partners, identify the country pair with the highest score. The score is calculated by proximity and level of trade shared between countries.
(4) Remove the vaccines provided to the partner country from the supply country’s vaccine stock.
(5) Shuffle the supplier data.
(6) Iterate through the countries with vaccine deficits until all needs are met. 
