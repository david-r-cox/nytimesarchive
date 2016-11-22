from nytimesarchive import ArchiveAPI 
from textstat.textstat import textstat
import pandas as pd 

key = 'adbbd909ff7241929e6a6c6a5e938f3f'
archive = ArchiveAPI(key)
data = []
for year in range(1950,2016):
	for month in range(1,13):
		contents = archive.query(year,month)
		date = str(year) + '-' + str(month)
		print date
		headlines = []
		total = 0.0
		count = 0.0
		length = 0.0
		for articles in contents ['response']['docs']:
			#print articles
			count = count + 1
			length = length +  textstat.lexicon_count(str(articles['headline']))
			total = total + textstat.flesch_reading_ease(str(articles['headline']))
		data.append((date,total/count, length/count))
		print count 
print data
labels = ['date','flesch_reading_ease', 'average_length']
df = pd.DataFrame.from_records(data,columns = labels)
df.to_csv('headlines.csv')
print df
#print data['1950-12']



#if articles['news_desk'] == 'National Desk'or articles['news_desk'] == None:
