# %% [markdown]
# # Project 1 : Unemployment Rate Analysis

# %% [markdown]
# ## Setup Testing

# %%
import pandas as pd
import matplotlib.pyplot as plt
print("All packages imported successfully!")
print(f"Pandas version: {pd.__version__}")
# Test loading the data file
df = pd.read_csv('UNRATE.csv')
print(f"Data loaded successfully! Shape: {df.shape}")

# %% [markdown]
# ## Data Loading

# %%
import pandas as pd
import matplotlib.pyplot as plt
# Load the provided unemployment data
df = pd.read_csv('UNRATE.csv')
# Convert DATE column to datetime
df['observation_date'] = pd.to_datetime(df['observation_date'])
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
df.head()

# %% [markdown]
# ## Basic Exploration

# %%
print(f"\nData types:",df.dtypes)
# Unrate statistics:
print(f"\nBasic statistics for unrate:", df['UNRATE'].describe())
# Observation Date statistics:
print(f"\nBasic statistics for observation_date:", df['observation_date'].describe())

# %% [markdown]
# ## Statistical Analysis

# %%
print("\nStatistical Analysis (15 points)")

# %% [markdown]
# ### Overall Average Unemployment Rate:

# %%
# The overall average unemployment rate
average_unemployment_rate = df['UNRATE'].mean()
print(f"\n Overall average unemployment rate: {average_unemployment_rate:.2f}%")

# %% [markdown]
# ### Minimum and Maximum Unemployment Rates with Dates:

# %%
# Minimum Unemployment rate
print(f"\n Minimum unemployment rate:{df[df['UNRATE'] == df['UNRATE'].min()]}")
# Maximum Unemployment rate
print(f"\n Maximum unemployment rate:{df[df['UNRATE'] == df['UNRATE'].max()]}")

# %% [markdown]
# ### Unemployment Statistics by Decade:

# %%
# New column 'Decade'
df['decade_col'] = (df['observation_date'].dt.year // 10) * 10
# Statistics by decade 
decade_statistics = df.groupby('decade_col')['UNRATE'].agg(['mean', 'min', 'max', 'std', 'count']).round(2)
print(f"\n Unemployment Statistics by Decade:{decade_statistics}")

# %% [markdown]
# ### Year of The Highest Average Unemployment Rate:

# %%
# New column Year
df['Year_col'] = df['observation_date'].dt.year
# Calculate the average unrate per year
average_unrate_by_year = df.groupby('Year_col')['UNRATE'].mean()
# Find the year of the highest average
max_average_year = average_unrate_by_year.idxmax()
# Print the value
print(f"\n The highest average unemployment rate was {average_unrate_by_year.max():.2f}% in {max_average_year}.")

# %% [markdown]
# ## Business Questions to Answer

# %% [markdown]
# ### What was the unemployment rate during major economic events (2008 financial crisis, COVID-19 pandemic)?

# %% [markdown]
# #### 2008 Financial Crisis
# The 2008 financial crisis was triggered by the collapse of the housing market and major financial institutions. It led to a severe global recession. In the U.S., unemployment rose sharply as businesses cut jobs during the economic downturn. Between mid-2007 and mid-2010, unemployment peaked above 10%, reflecting the deep impact on labor markets.

# %%
# 2008 Financial Crisis Custom Period 
gfc_period = df[(df['observation_date'] >= '2007-07-01') & (df['observation_date'] <= '2010-06-30')]
peak_gfc = gfc_period.loc[gfc_period['UNRATE'].idxmax()]
avg_gfc = gfc_period['UNRATE'].mean()
print("\n2008 Financial Crisis (Jul 2007 - Jun 2010)")
print(f" Peak Unemployment: {peak_gfc['UNRATE']}% in {peak_gfc['observation_date'].strftime('%b %Y')}")
print(f" Average Unemployment: {avg_gfc:.2f}%\n")

# %% [markdown]
# #### COVID-19 Pandemic
# The COVID-19 pandemic caused an unprecedented economic shock. Lockdowns and business closures led to massive job losses in early 2020. Unemployment spiked quickly, reaching a record high of 14.8% in April 2020, the highest rate since World War II. Although recovery followed, the average unemployment rate remained elevated through 2021 and beyond.

# %%
# COVID-19 Period (Feb 2020 – Apr 2023)
covid_period = df[(df['observation_date'] >= '2020-02-01') & (df['observation_date'] <= '2023-04-30')]
peak_covid = covid_period.loc[covid_period['UNRATE'].idxmax()]
avg_covid = covid_period['UNRATE'].mean()
print("\nCOVID-19 Pandemic (Feb 2020 - Apr 2023)")
print(f" Peak Unemployment: {peak_covid['UNRATE']}% in {peak_covid['observation_date'].strftime('%b %Y')}")
print(f" Average Unemployment: {avg_covid:.2f}%")


# %% [markdown]
# ### Which decade had the most stable unemployment rates (lowest standard deviation)?

# %%
# Calculate standard deviation by decade (decade column added previously)
stability = df.groupby('decade_col')['UNRATE'].std()
# Find most stable decade
best_decade = stability.idxmin()
lowest_std = stability.min()
print("\nMost Stable Decade Analysis")
print(f" The decade with the lowest variation in unemployment was the {best_decade}s")
print(f" Standard deviation: {lowest_std:.2f}%")

# %% [markdown]
# ### What’s the trend in unemployment over the last 10 years?

# %%
# Filter last 10 years (year column added previously)
latest_year = df['Year_col'].max()
recent_years = df[df['Year_col'] >= latest_year - 9]
# Summarize trend
print("\nTrend in Unemployment (Last 10 Years)")
print(recent_years[['observation_date', 'UNRATE']].reset_index(drop=True).to_string(index=False))
# Plot
plt.figure(num='Figure1:U.S. Unemployment Rate (Last 10 Years)', figsize=(10, 5))
plt.plot(recent_years['observation_date'], recent_years['UNRATE'], marker='o')
plt.title("U.S. Unemployment Rate (Last 10 Years)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## Data Visualization

# %% [markdown]
# ### Unemployment Rate Over Time

# %%
plt.figure(num='figure 2:Unemployment Rate Over Time', figsize=(12, 6))
plt.plot(df['observation_date'], df['UNRATE'], color='blue', linewidth=1.5, label='Unemployment Rate')  # <-- Add label here
plt.title('U.S. Unemployment Rate Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.grid(True)
plt.legend()  # Now this will display 'Unemployment Rate'
plt.tight_layout()
plt.savefig("unemployment_over_time.png")
plt.show()

# %% [markdown]
# ### Average Unemployment Rate by Decade

# %%
# Calculate average by decade
decade_avg = df.groupby('decade_col')['UNRATE'].mean().reset_index()
plt.figure(num='figure 3:Average U.S. Unemployment Rate by Decade', figsize=(10, 5))
plt.bar(decade_avg['decade_col'].astype(str), decade_avg['UNRATE'], color='pink')
plt.title('Average U.S. Unemployment Rate by Decade', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.tight_layout()
plt.savefig("average_unemployment_by_decade.png")  # Save the figure
plt.show()


