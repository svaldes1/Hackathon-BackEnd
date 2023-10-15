import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import skewnorm
def product_funct(apple, samsung, Google, df):

   # Random num between 0 and 1
    
#    data = {"Apple": 0, "Samsung": 0, "Google": 0, "Other": 0}
#    temp = pd.DataFrame(data, index=[0])
    values = []
    for i in range(5000):
        rand_num = np.random.rand(1)
        if rand_num < apple:
            values.append([1,0,0,0])

        elif rand_num < apple + samsung:
            values.append([0,1,0,0])

        elif rand_num < apple + samsung + Google:
            values.append([0,0,1,0])

        else:
            values.append([0,0,0,1])

    df["apple_pref"] = [i[0] for i in values]
    df["samsung_pref"] = [i[1] for i in values]
    df["google_pref"] = [i[2] for i in values]
    df["other_pref"] = [i[3] for i in values]
    return values

def accessory_funct(basic, prot, audio, df):

  
    values = []
    for i in range(5000):
        rand_num = np.random.rand(1)
        if rand_num < basic:
            values.append([1,0,0,0])

        elif rand_num < basic + prot:
            values.append([0,1,0,0])

        elif rand_num < basic + prot + audio:
            values.append([0,0,1,0])

        else:
            values.append([0,0,0,1])

    df["basic_pref"] = [i[0] for i in values]
    df["prot_pref"] = [i[1] for i in values]
    df["audio_pref"] = [i[2] for i in values]
    df["game_pref"] = [i[3] for i in values]
    return values


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
    
list = [["Iphone 15 Pro Max","Iphone 15 Pro"," Iphone 15"", Iphone 14 pro max"," Iphone 14"," Iphone 13"],
["Samsung Galaxy S23 Ultra"," Samsung Galaxy S23"," Samsung Galaxy S22","Samsung Galaxy S21"," Samsung Galaxy Z Flip5"],
["Google Pixel 7a","Google Pixel Fold"," Google Pixel 7"," Google Pixel 6a"],
["Motorola one 5G UW ace", "Motorola edge - 2022"]]


# Generate samples from the skew normal distribution

df = pd.DataFrame()
df = generateSkewSample(0, 200, 20, 5000, 'Spend_Power', df)
df = generateSkewSample(0, 0.5, 0.16, 5000, 'Tech_Sav', df)
df = generateSkewSample(2, 27.5, 8, 5000, 'Age', df)
df = generateSkewSample(0, 6, 2, 5000, 'Time_Cust', df)
df = generateSkewSample(0, 5, 1.5, 5000, 'Satisfaction', df)
df = generateSkewSample(5, 1, 0.5, 5000, 'House_Size', df)
df = generateSkewSample(10, 1, 0.6, 5000, 'Latest_Plan', df)
test = product_funct(0.5, 0.4, 0.1, df)
print(test)
test2 = accessory_funct(0.25, 0.25, 0.05, df)
print(test2)
df = generateSkewSample(0, 5, 2, 5000, 'Phone_Plan', df)
df = generateSkewSample(0, 5, 1, 5000, 'Home_Plan', df)


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
df.loc[df['Phone_Plan'] < 0, 'Phone_Plan'] = 0
df.loc[df['Phone_Plan'] > 10, 'Phone_Plan'] = 10
df.loc[df['Home_Plan'] < 0, 'Home_Plan'] = 0
df.loc[df['Home_Plan'] > 10, 'Home_Plan'] = 10

# export df to csv
df.to_csv('parentdata.csv', index=False)


