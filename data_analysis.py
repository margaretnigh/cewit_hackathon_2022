
import pandas as pd  

# gender ratio x vs net income y
# only 2020
# as gender ratio gets higher does net income 
# regression

df = pd.read_csv (r"Hackathon_20220208_24var.CSV")

#our group's data
data = df.loc[df["rh_label"] == "5: Shops"]
data = df.loc[df["Ind_label"] == "05: Shops"]
data = data.loc[df["year"] == 2020]

array1 = []
genderRatio = [] #x
netIncome = [] #y
average_men = 0
average_women = 0
average_total = 0
salesGrowth = []

#go through all the data
for index, row in df.iterrows():
    #businessSuccess = iva_company_rating_num, environmental_pillar_score, governance_pillar_score
    #0.7 and less is better
    genderScore = row["genderratio"] #The proportion of male directors at the Annual Report Date selected
    numberDirectors = row["numberdirectors"] #Total number of directors on the board
    numberOfMen = (genderScore * numberDirectors)
    numberOfWomen = numberDirectors - (genderScore * numberDirectors)
    array1.append([numberDirectors, numberOfMen, numberOfWomen])

    genderRatio.append(row["genderratio"])
    netIncome.append(row["ni"])
    salesGrowth.append(row["mve"])

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(color_codes=True)
f, ax = plt.subplots(figsize=(10, 10))
a = sns.regplot(x=genderRatio, y=netIncome, data=data, scatter_kws={"s": 30},x_estimator=np.mean)
a.set(ylim=(-2000,10000))

sns.set_theme(color_codes=True)
f, ax = plt.subplots(figsize=(10, 10))
a = sns.regplot(x=genderRatio, y=roa, data=data, scatter_kws={"s": 30},x_estimator=np.mean)
a.set(ylim=(-0.4,0.3))

sns.set_theme(color_codes=True)
f, ax = plt.subplots(figsize=(10, 10))
a = sns.regplot(x=genderRatio, y=salesGrowth, data=data, scatter_kws={"s": 30}, x_estimator=np.mean)
a.set(ylim=(-100,30000))




