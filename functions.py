import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\digan\OneDrive\Desktop\rainfall_dataset.csv")


def max_rainfall():
    print(df['ANNUAL'].max())


def min_rainfall():
    print(df['ANNUAL'].min())
    print(2)


def avg_rainfall():
    no_of_sub_div = df['ANNUAL'].count()
    total_rainfall = df['ANNUAL'].sum()
    print("Average Rainfall in India is:", total_rainfall / no_of_sub_div)
    print(3)


def name_max():
    max_rainfall = df['ANNUAL'].max()
    val = df[df['ANNUAL'] == max_rainfall]
    for i in val['SUBDIVISION']:
        print(i)


def name_min():
    min_rainfall = df['ANNUAL'].min()
    val = df[df['ANNUAL'] == min_rainfall]
    for i in val['SUBDIVISION']:
        print(i)


def month_min():
    print("Enter the month Name to get the Min Rainfall")
    month = input()
    min_month = df[month].min()
    val = df[df[month] == min_month]
    for i in val['SUBDIVISION']:
        print(i)


def month_max():
    print("Enter the month Name to get the Max Rainfall")
    month = input()
    min_month = df[month].max()
    val = df[df[month] == min_month]
    for i in val['SUBDIVISION']:
        print(i)


def graph_1():
    groups = df.groupby(by='SUBDIVISION')
    list_of_sub_div = list(groups.groups.keys())
    list_of_annual_mean_rainfall = []
    for i in groups.groups.keys():
        data = groups.get_group(i)
        value = data['ANNUAL'].mean()
        list_of_annual_mean_rainfall.append(value)
    plt.barh(list_of_sub_div, list_of_annual_mean_rainfall)
    plt.show()


def graph_2():
    groups = df.groupby(by='SUBDIVISION')
    list_of_sub_div = list(groups.groups.keys())
    list_of_annual_mean_rainfall = []
    for i in groups.groups.keys():
        data = groups.get_group(i)
        value = data['ANNUAL'].mean()
        list_of_annual_mean_rainfall.append(value)
    plt.plot(list_of_annual_mean_rainfall)
    plt.show()
