import wikipediaapi
import random

class Wikipedia:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')

    def getResponse(self, query):
        result = self.wiki.page(query)
        summary = (result.summary).split('. ')
        fullText = ""

        for i in range(random.randint(1, len(summary))):
            fullText += summary[i]
        return f"{fullText}...\n\nRead more at {result.fullurl}"
        
if __name__ == '__main__':
    wiki = Wikipedia()
    result = wiki.getResponse('Social support')
    print(result)