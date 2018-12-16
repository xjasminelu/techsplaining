import wikipediasummary

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

def getWiki(query):
    document = types.Document(
                content=query,
                type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    """sentiment = client.analyze_sentiment(document=document).document_sentiment
    print('Text: {}'.format(query))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    """
    
    entities = client.analyze_entities(document).entities
    
    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    for entity in entities:
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
        #print(u'{:<16}: {}'.format('metadata', entity.metadata))
        #print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        if len(entity.metadata.get('wikipedia_url', '-')) > 2:
            return '' + wikipediasummary.getsumm(entity.name)

