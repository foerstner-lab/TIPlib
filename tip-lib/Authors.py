from SPARQLWrapper import SPARQLWrapper, JSON


# new class
class Authors:
    def __init__(self, wd_id=None, orcid=None, isni=None):
        self.wd_id = wd_id
        self.orcid = orcid
        self.isni = isni
        self.name = None
        self.affiliation = None
        self.gender = None
        self.parents = None
        self.url = SPARQLWrapper('https://query.wikidata.org/sparql')
        #self.url.setMethod('GET')
        #print(self.url.method)

        # identify authors via orcid, ISNI, wd-id  or doi of article:
        if wd_id is not None:
            self._retrieve_features()
        elif isni is not None:
            self._get_wd_id_by_isni()
            self._retrieve_features()
        elif orcid is not None:
            self._get_wd_id_by_orcid()
            self._retrieve_features()
        else:
            print('Please insert DOI, ORCID, ISNI or Wikidata-ID to retrieve information on Authors of a paper.')

    def _get_wd_id_by_orcid(self):
        query = f'''SELECT distinct ?item
                 WHERE {{ ?item wdt:P496 ?orcid .    
                 Values ?orcid {{ '{self.orcid}' }}. 
                 SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                 }}'''
        q_results = self._get_wd_data(query)
        self.wd_id = q_results['results']['bindings'][0]['item']['value'].rsplit('/', 1)[1]

    def _get_wd_id_by_isni(self):
        query = f'''SELECT distinct ?item
                 WHERE {{ ?item wdt:P213 ?isni .    
                 Values ?isni {{ '{self.isni}' }}. 
                 SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                 }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings'])) > 0:
            self.wd_id = q_results['results']['bindings'][0]['item']['value'].rsplit('/', 1)[1]


    # get wikidata features about authors applying wikidata-id:
    def _retrieve_features(self):
        self._get_gender()
        self._get_name()
        self._get_affiliation()
        self._get_orcid()
        self._get_parents()

    # set general foundation on API:
    def _get_wd_data(self, query):
        self.url.setReturnFormat(JSON)
        self.url.setQuery(query)
        results = self.url.query().convert()
        return results

    # get features on authors (gender, employer, names, parents):
    def _get_gender(self):
        query = f'''SELECT ?genderLabel   
                WHERE {{ VALUES ?item {{ wd:{self.wd_id} }}.  
                    ?item wdt:P21 ?gender .
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.gender = q_results['results']['bindings'][0]['genderLabel']['value']

    def _get_affiliation(self):
        singleemployer = []
        query = f'''SELECT distinct ?employerLabel   
                WHERE {{ VALUES ?item {{ wd:{self.wd_id} }}.    
                    ?item wdt:P108 ?employer .
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        for res in q_results['results']['bindings']:
            singleemployer.append(res['employerLabel']['value'])
        self.affiliation = singleemployer

    def _get_name(self):
        query = f'''SELECT ?itemLabel
                WHERE {{ VALUES ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.name = q_results['results']['bindings'][0]['itemLabel']['value']

    def _get_orcid(self):
        query = f'''SELECT distinct ?orcid
                WHERE {{ ?item wdt:P496 ?orcid .              
                 Values ?item {{ wd:{self.wd_id} }}. SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings'])) > 0:
            self.orcid = q_results['results']['bindings'][0]['orcid']['value']

    def _get_parents(self):
        singleparent = []
        query = f'''SELECT distinct ?parents ?parentsLabel
                WHERE {{  ?parents wdt:P40 ?item .
                Values ?item {{ wd:{self.wd_id} }}. SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings'])) > 0:
            for res in q_results['results']['bindings']:
                singleparent.append(res['parentsLabel']['value'])
                singleparent.append(res['parents']['value'].rsplit('/', 1)[1])
            self.parents = singleparent


    # set up str-function for class author:
    def __str__(self):
        return f'''Author: {self.name}:\n
            Wikidata-ID: {self.wd_id}\n
            ORCID: {self.orcid}\n
            Gender: {self.gender}\n
            Name: {self.name}\n
            Affiliation: {self.affiliation}\n
            Parents: {self.parents}\n'''

if __name__ == '__main__' :
    Alexopoulou = Authors(orcid='0000-0003-4619-697X')
    print(Alexopoulou)