import pandas as pd

from collections import defaultdict

PATH_TO_DATA = "../data/20171013111831-SurveyExport.csv"
df = pd.read_csv(PATH_TO_DATA, encoding='iso-8859-1')

# Rename the columns with very long names.
df.rename(columns={'Thinking about a future in which so much of your world is connected to the internet leaves you feeling:':'attitude',
                    'I consider myself:':'user_level'},
                 inplace=True)

# Also replace some of the very long value names.
df["user_level"] = df["user_level"].replace('Average User:.*', "Average User", regex=True)
df["user_level"] = df["user_level"].replace('Technically Savvy:.*', "Technically Savvy", regex=True)
df["user_level"] = df["user_level"].replace('Ultra Nerd:.*', "Ultra Nerd", regex=True)
df["user_level"] = df["user_level"].replace('Luddite:.*', "Luddite", regex=True)

df["attitude"] = df["attitude"].replace('A little wary.*', "A little wary", regex=True)
df["attitude"] = df["attitude"].replace('Cautiously optimistic.*', "Cautiously optimistic", regex=True)
df["attitude"] = df["attitude"].replace('On the fence.*', "On the fence", regex=True)
df["attitude"] = df["attitude"].replace('Super excited!.*', "Super excited!", regex=True)
df["attitude"] = df["attitude"].replace('Scared as hell.*', "Scared as hell", regex=True)

# Rename the device columns with very long names.
df.rename(columns={'WiFi Router:Check all the internet connected devices you currently own:':'WiFi router',
                    'Laptop computer:Check all the internet connected devices you currently own:':'Laptop',
                    'Smart phone:Check all the internet connected devices you currently own:':'Smart phone',
                    'Smart TV:Check all the internet connected devices you currently own:':'Smart TV',
                    'Activity Tracker (ex: Fitbit or Apple Watch):Check all the internet connected devices you currently own:':'Activity tracker',
                    'Smarthome Hub (ex. Amazon Echo, Google Alexa):Check all the internet connected devices you currently own:':'Smarthome hub',
                    'Car that connects to the internet:Check all the internet connected devices you currently own:':'Car that connects to the internet',
                    'Smart Thermostat (ex: Nest):Check all the internet connected devices you currently own:':'Smart thermostat',
                    'Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge):Check all the internet connected devices you currently own:':'Smart appliance',
                    'Smart Door Locks (ex. Door locks for your home you can open via bluetooth):Check all the internet connected devices you currently own:':'Smart door lock',
                    'Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs):Check all the internet connected devices you currently own:':'Smart lighting'
                  },
                 inplace=True)

df_subset = pd.DataFrame()
df_subset['user_level'] = df['user_level']
df_subset['attitude'] = df['attitude']

devices = ['WiFi router', 'Laptop', 'Smart phone', 'Smart TV', 'Activity tracker', 'Smarthome hub', \
           'Car that connects to the internet', 'Smart thermostat', 'Smart appliance', 'Smart door lock', \
           'Smart lighting']

#  Set value to 1 for device owned, to 0 otherwise.
for device in devices:
    device_regex = r'(?i)' + device
    df_subset[device] = df[device].fillna(0).replace(regex=device_regex, value=1)

# Create a skeleton df to which the counts per device will be added.
df_devices = df_subset.groupby(['user_level', 'attitude']).size().reset_index().rename(columns={0:'counts'})

# For each device, count for all the {user attitude x user level} combinations how many of them own the device.
for device in devices:
    column_name = device + ' counts'
    df_temp = df_subset.groupby(['user_level', 'attitude', device]).size().reset_index().rename(columns={0:column_name})
    df_temp = df_temp.loc[df_temp[device] > 0].reset_index()
    df_devices[device] = df_temp[column_name]

# Drop the counts column that was created in the skeleton.
df_devices = df_devices.drop(['counts'], axis=1)

# Create a CSV for the device per user category data.
df_devices.to_csv('temp_devices_per_user_category.csv', index=False)

# Further process the CSV to get the data into the right format.
temp = open('temp_devices_per_user_category.csv', "r+")

device_counts = defaultdict(dict)
subgroups = []

for i, line in enumerate(temp.readlines()):
    if i == 0:
        header = line.strip().split(",")
        header = ["subgroup"] + header[2:]
    else:
        l = line.strip().split(",")
        subgroup = l[0] + " x " + l[1]
        subgroups.append(subgroup)
        l = [subgroup] + l[2:]
        line_dict = {h: l_item for h, l_item in zip(header, l)}
        for device in devices:
            device_counts[device][line_dict["subgroup"]] = line_dict[device]

output = open('devices_per_user_category.csv', "w+")

header = "device, " + ", ".join(subgroups)
output.write(header + "\n")

for device, counts in device_counts.items():
    device_line = device
    for subgroup in subgroups:
        device_line += ", " + counts[subgroup]
    output.write(device_line + "\n")

output.close()
