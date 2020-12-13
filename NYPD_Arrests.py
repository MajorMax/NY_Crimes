import pandas as pd
import matplotlib.pyplot as plt


#Import data
data = pd.read_csv('NYPD_Arrests.csv')

#Print out all column names
for col in data.columns:
    print(col)

#Plot of crimes commited by race
data['PERP_RACE'].value_counts().plot.barh()
print(data['PERP_RACE'].value_counts())

#Plot of crimes commited by sex
data['PERP_SEX'].value_counts().plot.barh()

#Print all age groups in the dataset
print(data['AGE_GROUP'].value_counts())

#Remove all the records where age was improperly entered
proper_age = data.loc[(data['AGE_GROUP'] == '<18') | (data['AGE_GROUP'] == '18-24') | (data['AGE_GROUP'] == '25-44') | (data['AGE_GROUP'] == '65+')]

#Print the new age groups
print(proper_age['AGE_GROUP'].value_counts())

#Graph the crimes by age without inproperly entered data
proper_age['AGE_GROUP'].value_counts().plot.barh()
plt.ylabel('Age')

#Print all the crimes commited by category
print(data['PD_DESC'].value_counts())

#Print out the crimes commited by race
print(data['PERP_RACE'].value_counts())

#Graph the crimes by race
data['PERP_RACE'].value_counts().plot.barh()
plt.ylabel('Race')

#Print out the filtered crimes (more than 50000)
#Filter out only the most common types of crimes (to prevent graph overcrowding)
#crime = data.loc[data['PD_DESC'].value_counts() >= 5000]

#Plotting the points on a map

BBox = (data.Longitude.min(), data.Longitude.max(), data.Latitude.min(), 41.0000)
print(BBox)
map = plt.imread('NY.png')

fig, ax = plt.subplots(figsize= (8,7))
ax.scatter(data.Longitude, data.Latitude, zorder=1, alpha= 0.2, c='r', s=10)
ax.set_title('Crimes in NY by location')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],41.0000)
ax.imshow(map, zorder=0, extent = BBox, aspect= 'equal')

#Export 80000 records selected randomly to new dataframe for Tableau analysis
data_trunc = data.sample(90000)

data_trunc.to_excel("NY_truncated.xlsx")