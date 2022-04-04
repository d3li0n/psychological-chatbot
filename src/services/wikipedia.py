import wikipediaapi
import random

class Wikipedia:
    """
        Constructor method to initialize the class variables.
        Wikipedia Library is set uo and looking for the articles in English.
    """
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')

    """
        Method takes an argument of string, and based on the sentence, it finds a relative
        article in the Wikipedia. Then, it returns a shorten version of the article with the link to it.
    """
    def getResponse(self, query):

        if len(query.strip()) == 0:
            return None
        try:
            result = self.wiki.page(query)
            summary = (result.summary).split('. ')
            fullText = ""

            for i in range(random.randint(1, len(summary))):
                fullText += summary[i]
            return f"{fullText}...\n\nRead more at {result.fullurl}"
        except:
            return "Sorry, I couldn't find any article about that."
        