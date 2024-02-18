from langchain.document_loaders import JSONLoader
from langchain_community.document_loaders.pubmed import PubmedLoader

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata['year'] = record.get('pub_date').get('year')
    metadata['month'] = record.get('pub_date').get('month')
    metadata['day'] = record.get('pub_date').get('day')
    metadata['title'] = record.get('article_title')

    return metadata

PubmedLoader()