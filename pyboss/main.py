import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file)

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

df['state_abbr']= df['State'].map(us_state_abbrev)

df['First_Name'], df['Last_Name'] = zip(*df['Name'].map(lambda x: x.split(' ')))

df['SSN'] = df['SSN'].str.slice(start=7, stop=11, step=None).map(lambda x: "***-**-" + x)

df['DOB'] = pd.to_datetime(df.DOB)
df['DOB'] = df['DOB'].dt.strftime('%m/%d/%Y')

df = df.drop(columns =['State','Name'])

df = df[['Emp ID', 'First_Name', 'Last_Name', 'DOB', 'SSN', 'state_abbr']]

print(df.head())

#TODO export this data to DIFFERENT CSV
exported_file = sys.argv[2]

df.to_csv(exported_file)
