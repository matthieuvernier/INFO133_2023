#pip install wikipedia
import wikipedia

#print(wikipedia.search("Trump"))    

page = wikipedia.page("Donald Trump")

#print(page.title)
#print(page.url)
#print(page.content)
#print(page.links)

print(wikipedia.summary("Donald Trump", sentences=2))