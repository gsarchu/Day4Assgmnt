#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
#st.balloons()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Used Car Sale")

#import dataset
df = pd.read_csv('usedcar.csv')
print(df.info())
print(df.describe())
#First thirty rows
SalePrice = df.head(50)
#Display the table
st.table(SalePrice)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
SalePrice.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(SalePrice['SalePrice'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='year',y='SalePrice',data=SalePrice,kind='scatter')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(SalePrice,hue='seller_type',palette='rainbow')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(SalePrice['SalePrice'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(SalePrice.corr(),cmap='coolwarm',annot=True)
st.pyplot()
