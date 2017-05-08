import wikipedia

wikipedia.set_lang("fr")
page = wikipedia.search("Bangladesh")
print(page)