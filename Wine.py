# We import the data with the Pandas library

import pandas as pd

df = pd.read_csv(r"C:\Users\Alex\Desktop\Datasets\Wine\wine_data.txt", header = 0)

data = df.values.tolist()

tag = []
alcochol = []
malic_acid = []
ash = []
alcalinity_of_ash = []
magnesium = []
phenols = []
flavanoids = []
nonflavanoid_phenols = []
proanthocyanins = []
color_intensity = []
hue = []
diluted_wines = []			
proline = []            


for i in range(len(data)): 
    tag.append(int(data[i][0]))
    alcochol.append(data[i][1])
    malic_acid.append(data[i][2])
    ash.append(data[i][3])
    alcalinity_of_ash.append(data[i][4])
    magnesium.append(data[i][5])
    phenols.append(data[i][6])
    flavanoids.append(data[i][7])
    nonflavanoid_phenols.append(data[i][8])
    proanthocyanins.append(data[i][9])
    color_intensity.append(data[i][10])
    hue.append(data[i][11])
    diluted_wines.append(data[i][12])
    proline.append(data[i][13])


counter = [0,0,0]
for i in range(len(tag)):
    if tag[i] == 1:
        counter[0]+=1
    elif tag[i] == 2:
        counter[1]+=1
    else:
        counter[2]+=1

# We visualise the data with the Matplotlib library

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = "C1","C2","C3"
sizes = counter
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

choices = ['blue','orange', 'red']

#%%

choices = ['blue','cyan', 'red']
colors = []

for i in range(len(tag)):
    if tag[i] == 1:
        colors.append(choices[0])
    elif tag[i] == 2:
        colors.append(choices[1])
    else:
        colors.append(choices[2])


plt.scatter(alcochol,magnesium,c=colors)    
plt.xlabel("Alcochol")
plt.ylabel("Magnesium")
  
plt.show()

#%%

plt.scatter(alcochol,ash,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Ash")

#%%

plt.scatter(alcochol,malic_acid,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Malic acid")

#%%

plt.scatter(alcochol,alcalinity_of_ash,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Alcalinity of ash")

#%%

plt.scatter(alcochol,phenols,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Phenols")

#%%

plt.scatter(alcochol,flavanoids,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Flavanoids ")

#%%

plt.scatter(alcochol,nonflavanoid_phenols ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Nonflavanoid phenols")

#%%

plt.scatter(alcochol, proanthocyanins ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Proanthocyanins")

#%%

plt.scatter(alcochol, color_intensity ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Color intensity")

#%%

plt.scatter(alcochol, hue ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Hue")   

#%%

plt.scatter(alcochol, diluted_wines ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Diluted wines")   

#%%

plt.scatter(alcochol, proline ,c=colors)
plt.xlabel("Alcochol")
plt.ylabel("Proline")   


