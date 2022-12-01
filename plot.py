from dateutil import parser
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

#storage amount of squats per day
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []

#use pandas to open the file
df = pd.read_csv('cu.csv')

#loop through file
for i in range(len(df)):
    #for every file take the date and amount of squats
    data = df.iloc[i]
    #get day number
    day = parser.parse(data[0]).isoweekday()
    #get data
    amount = int(data[1])

    #add amount of squats to list of corresponding day
    match day:
        case 1:
            monday.append(amount)
        case 2:
            tuesday.append(amount)
        case 3:
            wednesday.append(amount)
        case 4:
            thursday.append(amount)
        case 5:
            friday.append(amount)
        case 6:
            saturday.append(amount)
        case 7:
            sunday.append(amount)

#create dataset mean squats per day
data = {
    'monday' : np.mean(monday),
    'tuesday' : np.mean(tuesday),
    'wednesday' : np.mean(wednesday),
    'thursday' : np.mean(thursday),
    'friday' : np.mean(friday),
    'saturday' : np.mean(saturday),
    'sunday' : np.mean(sunday)
}

#create list with standard deviation per day
stdev = [np.std(monday), np.std(tuesday), np.std(wednesday), np.std(thursday), np.std(friday), np.std(saturday), np.std(sunday)]

#initialise plot
f = mp.figure(figsize = (15, 5))
#add data to the plot
mp.bar(list(data.keys()), list(data.values()))
#add errorbars
mp.errorbar(list(data.keys()), list(data.values()), yerr=stdev, fmt='None', ecolor='black')
mp.xlabel('days')
mp.ylabel('mean number of squats')
mp.title('mean number of squats per day')

#show the plot
mp.show()
