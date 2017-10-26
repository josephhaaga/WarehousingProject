
# coding: utf-8

# In[20]:

import pandas as pd;
import http.client, urllib.request, urllib.parse, urllib.error, base64;
import datetime;


# In[95]:

url = 'https://slickcharts.com/dowjones';
response = urllib.request.urlopen(url).read().decode('utf-8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')

raw_data = []

for row in soup.table.tbody.find_all('tr'):
#     Rank, Company, Symbol, Weight
    cells = row.find_all("td");
    rank = str(cells[0].string)
    company = str(cells[1].string)
    symbol = str(cells[2].find_all('input')[0]['value'])
    weight = str(cells[3].string)
    g = pd.Series(data = {"Rank":rank, "Company":company, "Symbol":symbol, "Weight":weight})
    g.rename(company)
    raw_data.append(g)


# In[97]:

weights = pd.DataFrame(columns=['Rank','Company','Symbol','Weight'], data=raw_data)


# In[99]:

weights


# In[105]:

now = datetime.datetime.now()
nice_now = str(now.month) + "-" + str(now.day) + "--" + str(now.hour) + "-" + str(now.minute);
weights.to_csv(nice_now+".csv")

