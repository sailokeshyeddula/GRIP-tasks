import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('SampleSuperstore.csv')

# Calculate profit by Category and Sub-Category
profit_data = df.groupby(['Category', 'Sub-Category'])['Profit'].sum().reset_index()

# Create a bar chart for profit by Sub-Category
fig_profit = px.bar(profit_data, x='Sub-Category', y='Profit', color='Category',
                    title='Profit by Sub-Category and Category')
fig_profit.update_xaxes(title_text='Sub-Category')
fig_profit.update_yaxes(title_text='Profit')

# Calculate total sales and profit by Region
region_data = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()

# Create a bar chart for total sales and profit by Region
fig_region = go.Figure(data=[
    go.Bar(name='Sales', x=region_data['Region'], y=region_data['Sales'], text=region_data['Sales'], textposition='auto'),
    go.Bar(name='Profit', x=region_data['Region'], y=region_data['Profit'], text=region_data['Profit'], textposition='auto')
])
fig_region.update_layout(barmode='group', title='Total Sales and Profit by Region')
fig_region.update_xaxes(title_text='Region')
fig_region.update_yaxes(title_text='Amount')

# Create a subplot with the profit by Sub-Category chart and the total sales and profit by Region chart
fig = make_subplots(rows=2, cols=1, subplot_titles=('Profit by Sub-Category and Category', 'Total Sales and Profit by Region'))
fig.add_trace(fig_profit.data[0], row=1, col=1)
fig.add_trace(fig_region.data[0], row=2, col=1)
fig.add_trace(fig_region.data[1], row=2, col=1)

# Update the layout
fig.update_layout(showlegend=True)

# Display the dashboard
fig.show()
