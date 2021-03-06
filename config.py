# Accessing the API ffrom the OS
import os

class Config:
    '''
    General configuration parent class
    '''

    API_KEY = os.environ.get('API_KEY')
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(API_KEY)
    EVERYTHING_API_BASE_URL = 'https://newsapi.org/v2/everything?domains=wsj.com&apikey={}'.format(API_KEY)
    TOP_HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?apiKey={}'.format(API_KEY)
    TECH_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}'.format(API_KEY)

class ProdConfig(Config):
    '''
    Production configuration chuld class

    Args:
        Config: The parent configuration class with General Configuration settings
    '''

    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with Gen config Settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}