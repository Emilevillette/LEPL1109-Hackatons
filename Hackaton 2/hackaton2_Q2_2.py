from hackaton2_Q2_1 import *


def mean_values_dataset(index_title, value_title):
    return df.groupby([index_title])[value_title].sum().div(df.groupby([index_title])[value_title].count())


if __name__ == '__main__':
    plt.figure(figsize=(8, 3))
    plt.plot(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
             mean_values_dataset('Weekday', 'Load'), 'o')
    plt.figure(figsize=(8, 3))
    plt.plot(range(0, 24), mean_values_dataset('Hour', 'Load'), 'o--')
    plt.show()
