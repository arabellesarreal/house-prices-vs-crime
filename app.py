import streamlit as st
import pandas as pd

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

st.title("Housing Prices and Crime Grades")

st.subheader("Line Chart: Prices vs Crime")

st
st.bar_chart(data = topTenStores, x = 'store_id' , y = 'store_sales')

st.subheader("Top Five Performing Areas")

topTenAreas = df.groupby('store_area')['store_sales'].sum().sort_values(ascending = False).head(5)
tenAreas = topTenAreas.to_frame().reset_index()
st.bar_chart(data = tenAreas, x = 'store_area', y = 'store_sales')

st.subheader("Average Daily Customer Count")
avgDailyCust = int(df['daily_customer_count'].mean())
st.markdown(":blue[" + str(avgDailyCust) + "]")

st.subheader("Total Sales")
totalSales = df['store_sales'].sum()
st.markdown(":green[" + str(totalSales) + "]")