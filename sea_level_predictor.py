import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.subplots(figsize=(10,10))
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],label="Comulative changes (in inches) in sea level")
  
    # Create first line of best fit
  a,b,r2,p_value,std_err = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
  years=pd.Series(range(1880, 2051))
  plt.plot(years, a*years+b, 'k', label = "first line of best fit")
  

    # Create second line of best fit
  a2,b2,r3,p_value1,std_err1 = linregress(df['Year'][df["Year"]>=2000], df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level'])
  years1=pd.Series(range(2000, 2051))
  plt.plot(years1, a2*years1+b2, 'k', label = "second line of best fit",color="red")

    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.legend(loc='upper left')
  plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()