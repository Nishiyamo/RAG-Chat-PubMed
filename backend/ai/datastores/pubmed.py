from langchain.document_loaders import JSONLoader
from langchain_community.document_loaders.pubmed import PubmedLoader

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata['year'] = record.get('pub_date').get('year')
    metadata['month'] = record.get('pub_date').get('month')
    metadata['day'] = record.get('pub_date').get('day')
    metadata['title'] = record.get('article_title')

    return metadata


# Create a new loader, we should pass to him the query and the maximum number of documents to load
# TODO: Change the query to a more specific one and also use it inside functions
PubmedLoader()