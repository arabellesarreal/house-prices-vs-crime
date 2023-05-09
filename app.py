import streamlit as st
import pandas as pd
import statsmodels.api as sm

hp = pd.read_csv("C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\HousePricesV3.csv")
cg = pd.read_csv("C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\CrimeGradeV3.csv")

cg = cg.drop_duplicates()
cg['zipcode'] = cg['zipcode'].astype(int)
cg['overall'] = cg['overall'].astype(int)
cg['property'] = cg['property'].astype(int)
cg['violent'] = cg['violent'].astype(int)
cg['other'] = cg['other'].astype(int)

hp = pd.read_csv("HousePricesV3.csv")
hp = hp.drop_duplicates()
hp = hp.drop('address', axis=1)
hp['price'] = hp['price'].astype(int)
hp['zipcode'] = hp['zipcode'].astype(int)

grouped = hp.groupby('zipcode')['price'].mean().reset_index()
pd.options.display.float_format = '{:.0f}'.format
mergedData = grouped.merge(cg, left_on = 'zipcode', right_on ='zipcode')

st.title("Housing Prices and Crime Grades")

filter = st.radio(
    "Which data would you like to view against average housing prices?",
    (('Overall Crime', 'Property Crime', 'Violent Crime', 'Other Crime'))
)
if filter == 'Overall Crime':
    
    st.subheader("Prices vs Overall Crime")
    st.bar_chart(data=mergedData, x="overall", y="price")

if filter == 'Property Crime':
    st.subheader("Prices vs Property Crime")
    st.bar_chart(data=mergedData, x="property", y="price")

if filter == 'Violent Crime':
    st.subheader("Prices vs Violent Crime")
    st.bar_chart(data=mergedData, x="violent", y="price")

if filter == 'Other Crime':
    st.subheader("Prices vs Other Crime")
    st.bar_chart(data=mergedData, x="other", y="price")

#Linear Regression

values = st.slider('Select a violent crime grade from 1 - 15', 1, 15)

# sets X to violent

x = mergedData['violent']

# sets Y to price

y = mergedData['price']

x = sm.add_constant(x)
results = sm.OLS(y,x).fit()

new_df = pd.DataFrame({'constant':1, 'violent':[ 1, 2,3, 4,5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15]})
predictions = results.predict(new_df)
new_df['price_predictions'] = results.predict(new_df)

st.write('Anticipated Prices:', "{:,}".format(int(new_df.iloc[values-1,2])))