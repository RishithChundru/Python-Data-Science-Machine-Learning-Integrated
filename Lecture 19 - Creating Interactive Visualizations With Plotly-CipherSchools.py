# Loading the Dataset
import pandas as pd

# load the datset
df=pd.read_csv('sales_data.csv')
print(df.head())

# creating a Line Plot
import plotly.express as px

# Creating a line plot
fig=px.line(df,x='Date',y='Sales',title='Sales Trend over Time',markers=True)
fig.show()


# Creating a Bar Plot
fig=px.bar(df,x='Region',y='Sales',title='Sales by Region',color='Region')
fig.show()


# Creating a Scatter Plot
fig=px.scatter(df,x=='Sales',y='Profit',title='Sales Vs Profit',color='Region',size='Quantity',hover_data=['Product'])
fig.show()


# Creating a Histogram
fig=px.histogram(df,x='Sales',title='Distribution of Sales',nbins==10)
fig.show()


# Creating a Pie Chart
fig=px.pie(df,values='Sales',names='Product',title='Sales Distribution by Product')
fig.show()


# Creating a Interactive Line Plot
fig=px.line(df,x='Date',y='Sales',title='Interactive Sales Trend Over Time',markers=True,color='Region',hover_data=['Product','Quantity','Profit'])
fig.show()


###
import plotly.express as px

# Sample Data
data={
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix'],
    'State':['NY','CA','IL','TX','AZ'],
    'Population':[8419000,398400,2716000,2328000,1690000]
}

# Creating the dataframe
df=pd.DataFrame(data)

# Create a geographical map
fig=px.choropleth(df,locations='State',locationmode='USA-states',color='Population',scope='usa',title='Population by State')
fig.show()