#"¿Cuáles fueron las páginas más vistas el "19 diciembre 2021" en el wikipedia español?"
import pageviewapi
result=pageviewapi.top('es.wikipedia', 2021, 12, "19", access='all-access')

limit=10

count=0
for items in result.items():
    for item in items[1]:
        for article in item['articles']:
            if (count<limit):
                print(article["article"])
                print(article["views"])
                count=count+1

