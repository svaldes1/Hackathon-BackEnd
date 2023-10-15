import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import skewnorm

def generate_random_numbers():
    # Set the random seed for reproducibility (optional)
    np.random.seed(42)

    # Generate an array of 5000 random numbers between 50 and 90
    random_numbers = np.random.uniform(50, 90, 5000)

    return random_numbers   

# df = pd.read_csv('skewtest.csv')

def generateSkewSample(alpha, loc, scale, num_samples, column_name, df):
    # Generate samples from the skew normal distribution
    samples = skewnorm.rvs(alpha, loc=loc, scale=scale, size=num_samples)

    df[column_name] = samples
    return df
def round_column_down(data_frame, column_name):

    if column_name in data_frame.columns:
        data_frame_rounded = data_frame.copy()
        data_frame_rounded[column_name] = np.floor(data_frame_rounded[column_name])
        return data_frame_rounded
    else:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")


# Generate samples from the skew normal distribution

df = pd.DataFrame()
df = generateSkewSample(0, 70, 6, 5000, 'Spend_Power', df)
df = generateSkewSample(0, 0.6, 0.1, 5000, 'Tech_Sav', df)
df = generateSkewSample(10, 18, 3.5, 5000, 'Age', df)
df = generateSkewSample(10, 1, 1, 5000, 'Time_Cust', df)
df = generateSkewSample(0, 5, 1.75, 5000, 'Satisfaction', df)
df = generateSkewSample(5, 1, 0.5, 5000, 'House_Size', df)
df = generateSkewSample(10, 1, 0.6, 5000, 'Latest_Plan', df)


# Isolate values outside of range
df.loc[df['Tech_Sav'] > 1, 'Tech_Sav'] = 1
df.loc[df['Tech_Sav'] < 0, 'Tech_Sav'] = 0
df.loc[df['Age'] < 18, 'Age'] = 18
df.loc[df['Time_Cust'] < 0, 'Time_Cust'] = 0
df.loc[df['Satisfaction'] < 0, 'Satisfaction'] = 0
df.loc[df['Satisfaction'] > 10, 'Satisfaction'] = 10
df = round_column_down(df, 'House_Size')
df = round_column_down(df, 'Latest_Plan')
df.loc[df['Latest_Plan'] > 3, 'Latest_Plan'] = 3
df.loc[df['Latest_Plan'] < 1, 'Latest_Plan'] = 1

# Create recommendations
list = [["Iphone 15 Pro Max","Iphone 15 Pro"," Iphone 15"", Iphone 14 pro max"," Iphone 14"," Iphone 13"],
        ["Samsung Galaxy S23 Ultra"," Samsung Galaxy S23"," Samsung Galaxy S22","Samsung Galaxy S21"," Samsung Galaxy Z Flip5"],
        ["Motorola one 5G UW ace"," Google Pixel 7a"," Google Pixel Fold,Motorola edge - 2022"," Google Pixel 7"," Google Pixel 6a"]]
# export df to csv
df.to_csv('collegestudentdata.csv', index=False)


