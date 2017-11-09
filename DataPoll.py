
# coding: utf-8

# In[32]:

import pandas as pd;
import http.client, urllib.request, urllib.parse, urllib.error, base64;
import datetime;


# In[33]:

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


# In[34]:

weights = pd.DataFrame(columns=['Rank','Company','Symbol','Weight'], data=raw_data)


# In[35]:

# weights


# In[36]:

now = datetime.datetime.now()
nice_now = str(now.month) + "-" + str(now.day) + "--" + str(now.hour) + "-" + str(now.minute);
weights.to_csv("weights/"+nice_now+".csv")


# In[37]:

# all_the_tickers = '/'.join(weights['Symbol'])


# In[38]:

import quandl
quandl.ApiConfig.api_key = 'k_u9AcWRLYRjV4KQhh2X';


# In[39]:

individual_tickers = {}
for ticker in weights.Symbol:
    individual_tickers[ticker] = quandl.get("WIKI/"+ticker)[-1:]

    

# individual_tickers


# In[40]:

# pd.DataFrame(individual_tickers['AAPL'].iloc[0])


# In[41]:

parsed = {};
for k in individual_tickers.keys():
    parsed[k] = individual_tickers[k].iloc[0]


# In[42]:

pd.DataFrame(parsed).to_csv("tickers/"+nice_now+".csv")


# In[43]:

# https://finance.yahoo.com/quote/%5EDJI/history/
# DJIA Open & Close Price

