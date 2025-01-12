# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lP2q_4Qz6IbNkqiP52b1o7y08eTFoFNi
"""

import pandas as pd
import numpy as np
from google.colab import files

# Faylni yuklash
uploaded = files.upload()

# DataFrame-ga ma'lumotlarni yuklash
df = pd.read_csv("WHO COVID-19 cases.csv")

# Ma'lumotlarni ko'rish
print("Birinchi 5 qator:")
print(df.head())

# Ma'lumotlarning umumiy ko'rinishi
print("\nUmumiy ma'lumot:")
print(df.info())

# Masalan, "Uzbekistan" davlatiga oid ma'lumotlar
uzbekistan_df = df[df['Country'] == 'Uzbekistan']
print("O'zbekiston bo'yicha ma'lumotlar:")
print(uzbekistan_df)

# Ma'lum sanadan keyingi yoki oldingi ma'lumotlar
filtered_df = df[df['Date_reported'] >= '2022-01-01']
print("2022-yil 1-yanvardan keyingi ma'lumotlar:")
print(filtered_df.head())

# Kasallar soni 1000 dan katta bo'lgan ma'lumotlar
high_cases_df = df[df['New_cases'] > 1000]
print("1000 dan ortiq yangi kasallar:")
print(high_cases_df)

import matplotlib.pyplot as plt
import seaborn as sns

# Davlatlar bo'yicha umumiy kasallar sonini ko'rsatish
top_countries = df.groupby('Country')['New_cases'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Eng ko'p yangi kasallar aniqlangan 10 ta davlat")
plt.xlabel("Yangi kasallar soni")
plt.ylabel("Davlat")
plt.show()