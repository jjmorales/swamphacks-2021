from typing import Tuple
import pandas
import json

#####################
# ticker processing #
#####################

ticker_sheet = pandas.read_csv('nasdaq.csv')

tickers = {}
for sym in ticker_sheet.iterrows():
    tickers[sym[1][1]] = sym[1][2]

# upper/remove special/match ticker/ if match -> tickername else -> check company name
# scrub, ticker/companyname -> return ticker name / else NaT (not a ticker)

from collections import Counter
with open('posts.csv') as f:
    words = f.read().upper().split()

#symbols = [word for word in words if ((len(word) > 1 and word[1:].isalpha() and word[0]=='$') or fuzzy.isCompany(word,tickers))]
symbols=[]
for word in words:
	if (len(word) > 1 and word[1:].isalpha() and word[0]=='$'):
		symbols.append(word)
		continue
	#val = fuzzy.isCompany(word,tickers)
	#if val != 'NaT' :
		#symbols.append(tickers[val[1:]])

freqs = Counter(symbols)

data={}
data['watchlist'] = []
for key in sorted(freqs):
		if(key[1:] in tickers.keys()):
			data['watchlist'].append({
				'ticker':key,
				'company':tickers[key[1:]],
				'frequency':freqs[key]
				})
			#print('%-8s : %3i' % (key, freqs[key]))

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
