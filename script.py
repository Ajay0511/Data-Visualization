import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:


wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood_rankings.head())
print(steel_rankings.head())


# write function to plot rankings over time for 1 roller coaster here:
def plotting_one(coaster_name, park_name, rankings_df):
    coaster_rankings = rankings_df[(rankings_df['Name'] == coaster_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    ax.set_yticks(coaster_rankings['Rank'].values)
    ax.set_xticks(coaster_rankings['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title("{} Rankings".format(coaster_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()


plotting_one('El Toro', 'Six Flags Great Adventure', wood_rankings)

plt.clf()


# write function to plot rankings over time for 2 roller coasters here:
def plotting_two(coaster_1_name, park_1_name, coaster_2_name, park_2_name, rankings_df):
    coaster_1_rankings = rankings_df[(rankings_df['Name'] == coaster_1_name) & (rankings_df['Park'] == park_1_name)]
    coaster_2_rankings = rankings_df[(rankings_df['Name'] == coaster_2_name) & (rankings_df['Park'] == park_2_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_1_rankings['Year of Rank'], coaster_1_rankings['Rank'], color='green', label=coaster_1_name)
    ax.plot(coaster_2_rankings['Year of Rank'], coaster_2_rankings['Rank'], color='red', label=coaster_2_name)
    ax.invert_yaxis()
    plt.title("{} vs {} Rankings".format(coaster_1_name, coaster_2_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend()
    plt.show()


plotting_two('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood_rankings)

plt.clf()


# write function to plot top n rankings over time here:
def plotting_n(rankings_df, n):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(10, 10))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    ax.set_yticks([i for i in range(1, 6)])
    ax.invert_yaxis()
    plt.title("Top 10 Rankings")
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend(loc=4)
    plt.show()


roller_coasters = pd.read_csv('roller_coasters.csv')


# print(roller_coasters.head())

# function to plot histogram of column values
def plot_histogram(coaster_df, column_name):
    plt.hist(coaster_df[column_name].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()


plot_histogram(roller_coasters, 'speed')
plt.clf()
plot_histogram(roller_coasters, 'length')
plt.clf()
plot_histogram(roller_coasters, 'num_inversions')
plt.clf()


def plotting_inversions_by_heights(coaster_df, park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(range(len(number_inversions)), number_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=90)
    plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('# of Inversions')
    plt.show()


plotting_inversions_by_heights(roller_coasters, 'Six Flags Great Adventure')
plt.clf()


# write function to plot pie chart of operating status here:

def piechart(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)
    status_counts = [num_operating_coasters, num_closed_coasters]
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.show()


piechart(roller_coasters)

plt.clf()


# write function to create scatter plot of any two numeric columns here:


def plot_scatter(coaster_df, column_x, column_y):
    plt.scatter(coaster_df[column_x], coaster_df[column_y])
    plt.title('Scatter Plot of {} Vs {}'.format(column_y, column_x))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()


def plot_scatter_height_speed(coaster_df):
    coaster_df = coaster_df[coaster_df['height'] < 140]
    plt.scatter(coaster_df['height'], coaster_df['speed'])
    plt.title('Scatter Plot of Speed vs. Height')
    plt.xlabel('Height')
    plt.ylabel('Speed')
    plt.show()


plt.clf()






