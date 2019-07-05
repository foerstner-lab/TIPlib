#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__=  'Eva Seidlmayer'
__copyright__ = ''
__credits__ = ['Eva Seidlmayer', 'Konrad U. Foerstner']
__license__ = ''
__version__ = '1.0'
__maintainer__ = 'Eva Seidlmayer'
__github__ = 'https://github.com/foerstner-lab/TIP-lib'
__status__ = 'Production'
__description__ = 'Extraction of information on journals from Wikidata'


from SPARQLWrapper import SPARQLWrapper, JSON

user_agent = 'TakeItPersonally, https://github.com/foerstner-lab/TIP-lib'


# new class Journal

class Journal:
    def __init__(self, wd_id=None, issn=None):
        self.wd_id = wd_id
        self.issn = issn
        self.name = None
        self.country_of_origin = None
        self.publisher = None
        self.review_score = None
        self.main_subject = None
        #self.open_licence = None
        #self.peer_reviewed = None
        #self.web_of_science = None
        self.url = SPARQLWrapper('https://query.wikidata.org/sparql', agent=user_agent)

# identify journal by wd_id or ISSN

        if wd_id is not None:
            self._retrieve_features()
        elif issn is not None:
            self._get_wd_id_by_issn()
            self._retrieve_features()
        else: 
            print('Please insert ISSN or Wikidata-ID to retrieve information on journals.')


    def _get_wd_id_by_issn(self):
        query = f'''SELECT distinct ?item
                 WHERE {{ ?item wdt:P236 ?ISSN .    
                 Values ?ISSN {{ '{self.issn}' }}. 
                 SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
              }}'''
        q_results = self._get_wd_data(query)
        self.wd_id = q_results['results']['bindings'][0]['item']['value'].rsplit('/', 1)[1]


# get wikidata features about journals applying wikidata-id:         
    def _retrieve_features(self):
        self._get_name()
        self._get_country_of_origin()
        self._get_publisher()
        self._get_review_score()
        self._get_main_subject()

# set general foundation on API:         
    def _get_wd_data(self, query):
        self.url.setReturnFormat(JSON)
        self.url.setQuery(query)
        results = self.url.query().convert()
        return results

# get features on journals

    def _get_name(self):
        query = f'''SELECT ?itemLabel
                WHERE {{ VALUES ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.name = q_results['results']['bindings'][0]['itemLabel']['value']

    
    def _get_country_of_origin(self):
        query = f'''SELECT distinct ?countryLabel
                WHERE {{ ?item wdt:P495 ?country .              
                Values ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''   
        q_results = self._get_wd_data(query)
        self.country_of_origin = q_results['results']['bindings'][0]['countryLabel']['value']
     
    def _get_publisher(self):
        query = f'''SELECT ?PublisherLabel
                WHERE {{ ?item wdt:P123 ?Publisher .              
                Values ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.publisher = q_results['results']['bindings'][0]['PublisherLabel']['value']

    def _get_review_score(self):
        query = f'''SELECT ?ReviewScoreLabel
                WHERE {{ ?item wdt:P444 ?ReviewScore .              
                Values ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings']))>0:
            self.review_score = q_results['results']['bindings'][0]['ReviewScoreLabel']['value']
        
    def _get_main_subject(self):
        query = f'''SELECT ?mainSubjectLabel
                WHERE {{ ?item wdt:P921 ?mainSubject .              
                Values ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                }}'''
        q_results = self._get_wd_data(query)
        self.main_subject = q_results['results']['bindings'][0]['mainSubjectLabel']['value']
    

        
# set up str-function for class Journal:    
    def __str__(self):
        return f'''Journal: {self.name}:\n
            Country: {self.country_of_origin}\n
            Publisher: {self.publisher}\n
            Review_score: {self.review_score}\n
            Main_subject: {self.main_subject}\n'''

if __name__ == '__main__':
    Nature = Journal('Q180445')
    print(Nature)