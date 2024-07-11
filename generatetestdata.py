# Generating fake data for {{base_uri}}/api/v1/projections/performance/pipeline filters
# Filters are View Trends, Account Segment, Funnel Lead Source and Funnel Country
# The datafile has 
# dategroup column for View Trends
# as_filter1 and as_filter2 columns for Account Segment
# fls_filter(1-5) columns for Funnel Lead Source
# fc_filters(1-5) for Funnel Country


import random
import csv
import pandas as pd

d = dict()

d['dategroup'] = lambda: random.choice(['quarter', 'month'])
d['as_filter1'] = lambda: random.choice(['','Enterprise'])
d['as_filter2'] = lambda: random.choice(['', 'Mid-Market'])
d['fls_filter1'] = lambda: random.choice(['', 'Field Events'])
d['fls_filter2'] = lambda: random.choice(['', 'Direct'])
d['fls_filter3'] = lambda: random.choice(['', 'Webinar'])
d['fls_filter4'] = lambda: random.choice(['', 'Search'])
d['fls_filter5'] = lambda: random.choice(['', 'Not Available'])
d['fc_filter1'] = lambda: random.choice(['', 'Not Available'])
d['fc_filter2'] = lambda: random.choice(['', 'USA'])
d['fc_filter3'] = lambda: random.choice(['', 'Australia'])
d['fc_filter4'] = lambda: random.choice(['', 'India'])
d['fc_filter5'] = lambda: random.choice(['', 'Canada'])
d['funnel_view'] = lambda: random.choice(['value', 'volume'])
d['funnel_split_by'] = lambda: random.choice(['','Lead Sources', 'Marketing vs Sales', 'Enterprise vs Mid-Market'])


numRows = 15000

header = ['dategroup','as_filter1', 'as_filter2', 'fls_filter1', 'fls_filter2', 'fls_filter3', 'fls_filter4', 'fls_filter5', 'fc_filter1', 'fc_filter2', 'fc_filter3', 'fc_filter4', 'fc_filter5', 'funnel_view', 'funnel_split_by']

f = open('testdata.csv', 'w')

writer = csv.writer(f)

writer.writerow(header)

for _ in range(numRows):
    r=[d[k]() for k in d.keys()]
    writer.writerow(r)

# Removing duplicates if any from the CSV file

df = pd.read_csv("testdata.csv")

df.drop_duplicates(inplace=True)

df.to_csv("testdata.csv", index=False)




