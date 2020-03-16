import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data: https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv
# Load data
# data = pd.read_csv('/Users/ivshina/Desktop/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
data = pd.read_csv('/Users/sualeh/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

# Select data for the last 7 days
data_y = data.iloc[:,-7:]
print(data_y)
# Select columns with locations
data_location = data.iloc[:,:2] # locations (province/state + country/region)

# Define exponential fit function 
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# exponential fit for specific location
# NYC data
ydata = data_y.iloc[100].values
data_SF = data_y.iloc[100]
times = np.linspace(1,7,7)


popt, pcov = curve_fit(func, times, ydata)

plt.figure()
plt.plot(times, ydata, '.k')
plt.plot(times, func(times, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.ylabel('Number of cases in NY')
plt.xlabel('9/03-15/03 week')
plt.show()
