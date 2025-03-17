from preswald import text, plotly, connect, get_df, table,query,slider
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('sample_csv')

sql = "SELECT * FROM sample_csv WHERE TOTAL_SPEND > 40"
filtered_df = query(sql, "sample_csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

threshold = slider("Threshold", min_val=0, max_val=50000, default=10000)
table(df[df["TOTAL_SPEND"] > threshold], title="Dynamic Data View")

# Create a scatter plot
fig = px.scatter(df, x='LOCATION', y='TOTAL_SPEND', text='USD_CAP',
                 title='Location vs. Total Spend',
                 labels={'Location': 'Location', 'Total_Spend': 'Total Spend'})

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Show the data
table(df)
