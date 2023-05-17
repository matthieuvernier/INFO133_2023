#pip install wikipedia
import wikipedia

wikipedia.set_lang("es")

page = wikipedia.page("Donald Trump")

#print(page.title)
#print(page.url)
#print(page.content)
#print(page.links)
print(wikipedia.summary("Donald Trump", sentences=1))