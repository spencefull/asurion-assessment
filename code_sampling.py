import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

calls = pd.read_csv('Call Sample.csv')

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)

print(calls)

# I need to first clean up the wrong names
print(calls['Supervisor'].value_counts())

NAME_CONVERSION = {
    'SAMANTHA': 'Samantha',
    'JOHN': 'John',
    'JOHNATHAN': 'John',
    'MICHAEL': 'Michael',
    'ANDREW': 'Andrew',
    'ADREEW': 'Andrew',
    'JORGE': 'Jorge',
    'JORRGE': 'Jorge',
    'SARAH': 'Sarah',
    'SARA': 'Sarah',
}

calls['Supervisor'] = calls['Supervisor'].apply(lambda x: NAME_CONVERSION[x] if x in NAME_CONVERSION else x)

# First check the missing data against median and mean and see how removing it affects the whole

print('Numeric Column Data:')
print(calls.describe())
print(calls.dropna().describe())
print('Site Value Counts:')
print(calls['Site'].value_counts())
print(calls.dropna()['Site'].value_counts())  # This drops 4, 5, and 6 from North, South, and East respectively
print('Client Value Counts:')
print(calls['Client'].value_counts())
print(calls.dropna()['Client'].value_counts())  # This removes 7 and 8 from B and A respectively
print('Supervisor Value Counts:')
print(calls['Supervisor'].value_counts())
print(calls.dropna()[
          'Supervisor'].value_counts())  # NAs: (Michael, Brian): 3, John: 2, (David, Andrew, Samantha, Eric, Sarah): 1
print('Agent Value Counts:')
print(calls['Agent'].value_counts())
print(calls.dropna()['Agent'].value_counts())  # No agent had more than 1
print('Week Value Counts:')
print(calls['Week'].value_counts())
print(calls.dropna()['Week'].value_counts())  # There are 2 in week 3, 3 in weeks 1, 2 and 4, and 4 in week 5

# Overall this looks to be spread out enough that I can justify removing this data for the exercise
# I would want to form some sort of punishment for not getting a rating though in a real system
# No review does not mean bad, but it doesnt mean good either. I would give them an average rating

# I will bring this data back later if it seems important

calls.dropna(inplace=True)

# It is now time to look out our relationships
# Supervisor to Service Time/Quality Score

print('Supervisor Data by Service Time:')
print(calls.groupby(['Supervisor'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values('service_mean'))

# The highest 3 service times are Andrew, Jorge, and Brian with Julie and Michael not far behind

print('Supervisor Data by Quality Score:')
print(calls.groupby(['Supervisor'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values('quality_mean'))

# The lowest quality scores are Michael, Julie and Samantha

# Andrew has high quality scores so this tells me some tasks can take longer
# and you can still get a high score depending on the task


# Supervisor to Agent to Service Time/Quality Score
print(calls.groupby(['Supervisor', 'Agent'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['Supervisor', 'service_mean']))

# Each agent only reports to one supervisor

# Client to Service Time/Quality Score
print(calls.groupby(['Client'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['service_mean']))

# Client A takes much less time and has a much higher score (thats our expected hypothesis)


# Client to Supervisor to Service/Quality Score
print(calls.groupby(['Client', 'Supervisor'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['Client', 'service_mean']))

# For the most part, we see that the longer a service mean, the lower the quality score. A more in depth look with Agent will help

# Client to Agent to Service/Quality Score
print(calls.groupby(['Client', 'Agent'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['Client', 'service_mean']))

plt_df = calls.groupby(['Client', 'Agent'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median'))[['Client', 'service_mean', 'quality_mean']]

plt.scatter(x=plt_df[plt_df['Client'] == 'A']['service_mean'],
            y=plt_df[plt_df['Client'] == 'A']['quality_mean'],
            color='blue')
plt.scatter(x=plt_df[plt_df['Client'] == 'B']['service_mean'],
            y=plt_df[plt_df['Client'] == 'B']['quality_mean'],
            color='green')

a_linear = np.polyfit(plt_df[plt_df['Client'] == 'A']['service_mean'],
                      plt_df[plt_df['Client'] == 'A']['quality_mean'], 1)
a_slope = np.poly1d(a_linear)
plt.plot(plt_df[plt_df['Client'] == 'A']['service_mean'], a_slope(plt_df[plt_df['Client'] == 'A']['service_mean']),
         color='blue', linestyle="--")
b_linear = np.polyfit(plt_df[plt_df['Client'] == 'B']['service_mean'],
                      plt_df[plt_df['Client'] == 'B']['quality_mean'], 1)
b_slope = np.poly1d(b_linear)
plt.plot(plt_df[plt_df['Client'] == 'B']['service_mean'], b_slope(plt_df[plt_df['Client'] == 'B']['service_mean']),
         color='green', linestyle="--")
plt.show()

# This is very interesting. Here we see that there are 3 batches of general times that occur.
# 400-420, 450-470, and 500-520
# In these batches, we see that the same service time can get vastly different scores.
# If we are just basing things off Service Time, customer B is much less satisfied for the same service time
# We do see lower quality scores as the time increase which we expect


# Site to Service Time/Quality Score
print(calls.groupby(['Site'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['service_mean']))

# This is very interesting. We have significantly longer wait times from the South Site and a lower quality score
# I want to check this with the Supervisors to see if all the longer ones are in the south site

# Site and Supervisor to Service Time/Quality Score
print(calls.groupby(['Site', 'Supervisor'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median')).sort_values(['Site', 'service_mean']))

# Hmmm. Less revealing than I thought. It appears the South site has 4 lower performers
# North Site has 4 all stars
# East site has the two best and two low performers

#I want to compare this with customers to see if South has a lot of Customer B
print(calls.groupby(['Site', 'Client'], as_index=False).aggregate(
    service_mean=('Service Time', 'mean'),
    service_median=('Service Time', 'median'),
    quality_mean=('Quality Score', 'mean'),
    quality_median=('Quality Score', 'median'),
    number_in_group=('Quality Score', 'count')).sort_values(['Site', 'service_mean']))

# There is a pretty even split between client A and B between each location so not as revealing as I thought



# The core of my findings so far, the customer B has a greater opportunity for improvement in service.
    # Usually if a customer is dissatisfied, it is more than just a service time.
    # We should meet with the customer to discuss the issues
        #If its as simple as service time, we need to get our faster/more experienced people \
        # working more consistently with them to make them happy
            # This can come at reduced happiness of the already happy customer, but it depends on priorities
# The South site has a bigger opportunity for improvement on times.
    # This could be handled one of two ways
        # 1. See if two people from the North location would switch to balance the locations.
            # They would be tasked with training/improving the South location people
            # Those that moved from the South into the North site would be trained by the North people
            # It is hard to move people sometimes so this may not be an option
        # 2. Focus efforts/training on the South site to get them faster and more efficient


# Now that I understand the data at a cursory glance, and I have next steps labeled out, some other interesting things to do:
# Build a predictive model that could say, based on the variables given, what quality score should you expect
# Then it could tell you that based on the variables the Agent controls, what they can do to get a higher score
# For the nerds like me out there,
# I would want to use feature reduction to try and simplify the model and remove redundancies with the correlated data
# There is only one variable in their control at this point in time so that is time.
    # It would show the expected score based on the windows seen in the plotted graph
    # I also know better than to make the expected score an exact value. It would be an "expected" range

