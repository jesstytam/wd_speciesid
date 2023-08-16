#load excel file
import pandas as pd
data = pd.read_csv('~/data/wild_deserts/Beyond the Fence- information/Beyond_the_Fence_ALL_TAGS_to_Feb22.csv', header=1)
print(data.head())

#find the number of images per species
#species_list = data['Species']

#for species in species_list.unique():
#    print(species_list.count(species))

print(data['Species'].value_counts())
