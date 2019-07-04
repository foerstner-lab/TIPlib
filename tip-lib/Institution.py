from SPARQLWrapper import SPARQLWrapper, JSON
import user_agent

User-Agent: TakeItPersonally (https://github.com/foerstner-lab/TIP-lib; seidlmayer@zbmed.de)

# new class Institution

class Institution:
    def __init__(self, wd_id=None, ror=None, isni = None):
        self.wd_id = wd_id
        #self.ror = ror
        self.isni = isni
        self.name = None
        self.country = None
        self.type = None
        self.students_count = None
        self.tuition = None
        self.url = SPARQLWrapper('https://query.wikidata.org/sparql', agent=user_agent)


# identify institution via ISNI or wd_id; in fututre ROR 
        if wd_id is not None:
            self._retrieve_features()
        elif isni is not None:
            self._get_wd_id_by_isni()
            self._retrieve_features()
        elif ror is not None:
            self._get_wd_id_by_ror()
            self._retrieve_features()
        else: 
            print('Please insert ISNI or Wikidata-ID to retrieve information on Institutions.')
        
    #def _get_wd_id_by_ror(self):
    
    def _get_wd_id_by_isni(self):
        query = f'''SELECT distinct ?item
                 WHERE {{ ?item wdt:P213 ?isni .    
                 Values ?isni {{ '{self.isni}' }}. 
                 SERVICE wikibase:label {{ bd:serviceParam wikibase:language '[AUTO_LANGUAGE],en'. }}
                 }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings']))>0:
            self.wd_id = q_results['results']['bindings'][0]['item']['value'].rsplit('/', 1)[1]
        
# get wikidata features about institutions applying wikidata-id:         
    def _retrieve_features(self):
        self._get_name()
        self._get_country()
        self._get_type()
        self._get_students_count()
        self._get_tuition()

# set general foundation on API:         
    def _get_wd_data(self, query):
        self.url.setReturnFormat(JSON)
        self.url.setQuery(query)
        results = self.url.query().convert()
        return results

# get features on institutions

    def _get_name(self):
        query = f'''SELECT ?itemLabel
                WHERE {{ VALUES ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.name = q_results['results']['bindings'][0]['itemLabel']['value']

    
    def _get_country(self):
        query = f'''SELECT distinct ?countryLabel
                WHERE {{ ?item wdt:P17 ?country .              
                Values ?item {{ wd:{self.wd_id} }}. 
                SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". 
                }} }}'''   
        q_results = self._get_wd_data(query)
        self.country = q_results['results']['bindings'][0]['countryLabel']['value']
     
    def _get_type(self):
        query = f'''SELECT distinct ?instanceofLabel
                WHERE {{ ?item wdt:P31 ?instanceof .              
                Values ?item {{ wd:{self.wd_id} }}. SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        self.type = q_results['results']['bindings'][0]['instanceofLabel']['value']

        
    def _get_students_count(self):
        query = f'''SELECT ?studentscountLabel
                WHERE {{ ?item wdt:P2196 ?studentscount .              
                Values ?item {{ wd:{self.wd_id} }}. SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }} 
                }}'''
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings']))>0:
            self.students_count = q_results['results']['bindings'][0]['studentscountLabel']['value']

    def _get_tuition(self):
        query = f'''SELECT ?tuitionLabel
                WHERE {{ ?item wdt:P5894 ?tuition .              
                Values ?item {{ wd:{self.wd_id} }}. SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                }}''' 
        q_results = self._get_wd_data(query)
        if (len(q_results['results']['bindings']))>0:
            self.students_count = q_results['results']['bindings'][0]['tuitionLabel']['value']

            
        
# set up str-function for class institution:    
    def __str__(self):
        return f'''Institution: {self.name}:\n
            Country: {self.country}\n
            Type: {self.type}\n
            Students_count: {self.students_count}\n
            Tuition: {self.tuition}\n'''


if __name__ == '__main__':
    PotsdamInstitut = Institution('Q251061')
    print(PotsdamInstitut)