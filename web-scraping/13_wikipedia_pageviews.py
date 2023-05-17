#pip install git+https://github.com/Commonists/pageview-api.git
import pageviewapi

result1=pageviewapi.per_article('es.wikipedia', 'Gabriel Boric', '20220101', '20220501',
                        access='all-access', agent='all-agents', granularity='daily')


#print(result1)
for item in result1.items():
    for article in item[1]:
        timestamp=article['timestamp'][:8] #first 8 digits
        views=article['views']
        print(timestamp)
        print(views)