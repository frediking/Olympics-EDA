#!/usr/bin/env python
# coding: utf-8

# In[1]:


# filepath: /C:/Users/ADMIN/Downloads/EDA Olympics.py
import os

# Create folder to store plots
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

plot_counter = 1  # Global counter for file names

def save_and_show():
    global plot_counter
    filename = os.path.join(output_dir, f"plot_{plot_counter:02d}.png")
    plt.savefig(filename, dpi=300)
    print(f"Saved {filename}")
    plt.close()
    plot_counter += 1


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


import os
print(os.getcwd())


# In[4]:


# Read the Olympics dataset and display the first few rows
olymp = pd.read_csv(r"C:\Users\ADMIN\Desktop\dataset_olympics.csv")
olymp.head()


# In[5]:


# Dataset Info
olymp.info()


# In[6]:


# Summary Statistics
olymp.describe()


# In[7]:


olymp.describe(include=["object"])


# In[8]:


# Checking for missing values 
olymp.isna().sum()


# In[9]:


# Checking and removing duplicated values
olymp.duplicated().sum()
olymp.drop_duplicates(inplace = True)
olymp.duplicated().sum()


# In[10]:


# VISUALIZATIONS
# Countplot for Gender Distribution 
sns.countplot(data=olymp, x="Sex", color=sns.color_palette("viridis", 1)[0])
plt.title("Distributions by Gender")
save_and_show()


# In[11]:


# Histogram: Age Distribution 

sns.histplot(data=olymp, x="Age", bins=10, kde=True, fill=True, 
             color=sns.color_palette("viridis", 1)[0], alpha=0.5)
plt.title("Distribution of Age")
save_and_show()


# In[12]:


# Histogram: Height Distribution 

import matplotlib.cm as cm
sns.histplot(data=olymp, x="Height", bins=20, kde=True, fill=True, 
             color=sns.color_palette("viridis", 1)[0], alpha=0.5)
plt.title("Height Distribution")
save_and_show()


# In[13]:


# Histogram: Weight Distribution 

sns.histplot(data=olymp, x="Weight", bins=20, kde=True, fill=True, 
             color=sns.color_palette("cividis", 1)[0], alpha=0.5)
plt.title("Weight Distribution")
save_and_show()


# In[14]:


# Countplot: Medals Distribution 

sns.countplot(data=olymp, x="Medal", color=sns.color_palette("viridis", 1)[0])
plt.title("Medals Distribution")
plt.show()


# In[15]:


# Countplot: Distribution of Medals Over the Years 
sns.countplot(data= olymp, x ="Year", hue = "Medal")
plt.title("Distribution of Medals Over the Years")
plt.xticks(rotation = 90)
save_and_show()


# In[16]:


#GROUP BY YEAR & CALCULATE AVERAGE AGE
Y_avg_age = olymp.groupby("Year")["Age"].mean()
print(Y_avg_age)


# In[17]:


# Calculate median Height by Sport
medianheight_sport = olymp.groupby("Sport")["Height"].median()
print(medianheight_sport)


# In[18]:


# Maximum and Minimum values of median height of sports
print("Max:" ,medianheight_sport.max())
print("Min:" ,medianheight_sport.min())


# In[19]:


# Sports with median height
medianheight_sport[medianheight_sport == 190.0]


# In[20]:


# Count the number of participants grouped by Country (NOC) and Gender
country_gender_count = olymp.groupby(["NOC" , "Sex"])["ID"].count()
print(country_gender_count)


# In[21]:


# Calculate gold medals per country 

goldmedals_country = olymp[olymp["Medal"] == "Gold"].groupby("NOC")["Medal"].count()
print("Gold Medals by Country:", goldmedals_country)


# In[22]:


print("Maximum gold medals:", goldmedals_country.max())


# In[23]:


# Countries with 747 Gold Medals
goldmedals_country[goldmedals_country == 747]


# In[24]:


# Calculate average Weight by Sport and Gender
avgweight_sport_gender = olymp.groupby(["Sport", "Sex"])["Weight"].mean()

# Average Weight for Wrestling (Female)
print(avgweight_sport_gender["Wrestling"]["F"])


# In[25]:


# Bar Chart: Number of Unique Events per Sport 

sportevent_count = olymp.groupby("Sport")["Event"].nunique().sort_values(ascending = False)
colors= plt.cm.viridis(np.linspace(0, 1, len(sportevent_count)))
plt.figure(figsize=(14, 7))
bars = sportevent_count.plot(kind = "bar",color=colors)
plt.title("Number of Unique Events per sport")
plt.xlabel("Sport")
plt.ylabel("Number of Unique Events")
plt.xticks(rotation = 90, fontsize=8)
plt.tight_layout()
save_and_show()


# In[26]:


# Line Plot: Number of Participants Over the Years 

YearParticipant_count = olymp.groupby("Year")["ID"].nunique()
plt.figure(figsize=(10, 5))
plt.plot(YearParticipant_count, marker='o', linestyle='-', 
         color=sns.color_palette("viridis", 1)[0], linewidth=2, markersize=6)

plt.title("Number of Participants Over the Years", fontsize=12, fontweight='bold', color='black')
plt.xlabel("Year", fontsize=10, fontweight='bold')
plt.ylabel("Number of Participants", fontsize=10, fontweight='bold')

plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)
save_and_show()


# In[27]:


# ALTERNATE BAR PLOT VISUALIZATION FOR THE LINE PLOT OF THE NUMBER OF PARTICIPANT OVER THE YEARS 

YearParticipant_count = olymp.groupby("Year")["ID"].nunique()
colors= plt.cm.viridis(np.linspace(0, 1, len(YearParticipant_count)))
plt.figure(figsize=(14, 7))
bars = YearParticipant_count.plot(kind = "bar",color=colors)
plt.title("Number of participants over the years")
plt.xlabel("Year")
plt.ylabel("Number of Participants")
save_and_show()


# In[28]:


# Bar Plot: Top 10 Countries with the Highest Average Age 

country_avg_age = olymp.groupby("NOC")["Age"].mean().sort_values(ascending = False)
plt.figure(figsize=(14, 7))
colors= plt.cm.viridis(np.linspace(0, 1, len(country_avg_age.head(10))))
bars = country_avg_age.head(10).plot(kind = "bar",color=colors)
plt.title("Top 10 countries with the Highest Average age of participants")
plt.xlabel("Country")
plt.ylabel("Average Age")
plt.xticks(rotation = 90)
save_and_show()


# In[29]:


# Bar Plot: Top 10 Countries with the Lowest Average Age
# Show the lowest "country_avg_age" by using the 'tail()' function to view from the bottom

country_avg_age = olymp.groupby("NOC")["Age"].mean().sort_values(ascending = False)
plt.figure(figsize=(14, 7))
colors= plt.cm.viridis(np.linspace(0, 1, len(country_avg_age.tail(10))))
bars = country_avg_age.tail(10).plot(kind = "bar",color=colors)
plt.title("Top 10 countries with the Lowest Average age of participants")
plt.xlabel("Country")
plt.ylabel("Average Age")
plt.xticks(rotation = 90)
save_and_show()


# In[30]:


# Boxplot: Age Distributions by Season 
plt.figure(figsize=(10, 6))
sns.boxplot(data = olymp, x = "Season", y = "Age", palette="viridis")
plt.title("Distributions of Ages by Seasons")
plt.xlabel("Season")
plt.ylabel("Age")
save_and_show()


# In[31]:


# Violin Plot: Height Distribution by Medal 
# Update palette from Set2 to viridis for a modern look
sns.violinplot(data=olymp, x="Medal", y="Height", palette="viridis")
plt.title("Distribution of Heights by Medal")
plt.xlabel("Medal")
plt.ylabel("Height")
save_and_show()


# In[32]:


# COUNTRY WITH THE MOST MEDALS
country_mostmedals = olymp["NOC"].value_counts().idxmax()
print("Most Awarded Country(Medals):", country_mostmedals)


# In[33]:


# Tallest Athlete
tallest_athlete = olymp[olymp["Height"] == olymp["Height"].max()]
print("Tallest Athlete:")
print(tallest_athlete[["ID", "Name", "Height", "Sport","Year"]])


# In[34]:


# Shortest Athlete
shortest_athlete = olymp[olymp["Height"] == olymp["Height"].min()]
print("Shortest Athlete:")
print(shortest_athlete[["ID","Name", "Height", "Sport", "Year","Event"]])


# In[35]:


# Heaviest Athlete

heaviest_athlete = olymp[olymp["Weight"] == olymp["Weight"].max()]
print("Heaviest Athlete:")
print(heaviest_athlete[["ID", "Name", "Height", "Sport", "Year","Event"]])


# In[36]:


# Scatter Plot: Athlete Height vs Weight by Medal Status 

sns.scatterplot(data = olymp, x = "Height", y = "Weight", hue = "Medal", palette = "Set2")
plt.title("Athlete Height vs Weight by Medal Status")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend(title = "Medal")
save_and_show()


# In[37]:


# Heatmap: Medal Counts by Country and Year 
MedalsbyCountry_year = olymp.pivot_table(index = "NOC", columns = "Year", values = "Medal", aggfunc = "count")
sns.heatmap(MedalsbyCountry_year, cmap = "viridis", linewidths = 0.5)
plt.title("Medal Counts by Country and Year")
plt.xlabel("Year")
plt.ylabel("Country")
plt.xticks(rotation = 90, fontsize=8)
save_and_show()

