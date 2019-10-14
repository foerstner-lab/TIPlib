#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Eva Seidlmayer"
__copyright__ = ""
__credits__ = ["Eva Seidlmayer", "Konrad U. Foerstner"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Eva Seidlmayer"
__github__ = "https://github.com/foerstner-lab/TIP-lib"
__status__ = "Production"
__description__ = "Extraction of DOI and PubMed-ID from XML and retierval of Wikidata-identificators (q-numbers) for authors"


from SPARQLWrapper import SPARQLWrapper, JSON

user_agent = "TakeItPersonally, https://github.com/foerstner-lab/TIP-lib"

class article:
    def __init__(self, doi = None, pmid = None):
        self.doi = doi
        self.pmid = pmid
        self.author_qnr = None
        self.article_qnr = None
        self.url = SPARQLWrapper("https://query.wikidata.org/sparql", agent=user_agent)

        # identify dois from articles:
        if doi is not None:
            self._get_article_qnr_by_doi()
            self._get_pmid_by_doi()
            self._get_article_qnr_by_doi()
        elif pmid is not None:
            self._get_qnr_by_pmid()
            self._get_doi_by_pmid()
            self._get_article_qnr_by_pmid()
        else:
            print("Please insert DOI or PubMed-ID to retrieve information.")



    def _get_wd_data(self, query):
        self.url.setReturnFormat(JSON)
        self.url.setQuery(query)
        results = self.url.query().convert()
        return results




    def _get_article_qnr_by_doi(self):
        query = f'''SELECT distinct ?item
                     WHERE {{ ?item wdt:P356 ?doi .    
                     Values ?doi {{ '{self.doi}' }}. 
                     SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                     }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if (len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']:
                     self.article_qnr = (res['item']['value'].rsplit('/', 1)[1])
        else:
            pass



    def _get_author_qnr_by_doi(self):
        authors = []
        query = f'''SELECT distinct ?author
                     WHERE {{ ?item wdt:P356 ?doi .    
                     Values ?doi {{ '{self.doi}' }}. 
                     {{ ?item wdt:P50 ?author }}. 
                     SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                     }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if (len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']:
                authors.append(res['author']['value'].rsplit('/', 1)[1])
                self.author_qnr = authors

        else:
            pass

    def _get_pmid_by_doi(self):
        query= f''' SELECT distinct ?pmid
                     WHERE {{ ?item wdt:P356 ?doi .    
                     Values ?doi {{ '{self.doi}' }}. 
                     {{ ?item wdt:P698 ?pmid }}. 
                     SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                     }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if(len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']: \
                    self.pmid = res['pmid']['value']
        else:
            pass



    def _get_article_qnr_by_pmid(self):
        query = f'''SELECT distinct ?item
                     WHERE {{ ?item wdt:P698 ?pmid .    
                     Values ?pmid {{ '{self.pmid}' }}. 
                     SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                     }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if (len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']:
                     self.article_qnr = (res['item']['value'].rsplit('/', 1)[1])
        else:
            pass


    def _get_qnr_by_pmid(self):
        authors = []
        query = f'''SELECT distinct ?author ?authorLabel
                     WHERE {{ ?item wdt:P698 ?pmid .    
                     Values ?pmid {{ '{self.pmid}' }}. 
                     {{ ?item wdt:P50 ?author }}. 
                     SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                     }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if (len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']: \
                    authors.append(res['author']['value'].rsplit('/', 1)[1])
            self.author = authors
        else:
            pass

    def _get_doi_by_pmid(self):
        doi = []
        query= f''' SELECT distinct ?doi
                    WHERE {{ 
                    ?item wdt:P698 ?pmid .    
                    Values (?pmid) {{("{self.pmid}")}}.
                    ?item wdt:P356 ?doi.
                    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                    }}'''
        #print(query)
        results = self._get_wd_data(query)
        #print(results)
        if(len(results['results']['bindings'])) > 0:
            for res in results['results']['bindings']: \
                doi.append(res['doi']['value'])
            self.doi = doi

        else:
            pass




    # set up str-function for class author:
    def __str__(self):
        return f"""Wikidata-Q-Nr: {self.article_qnr}
                   DOI: {self.doi}\n
                   PubMed-ID: {self.pmid}\n
                   Author-Wikidata-ID Q-Number: {self.author_qnr}"""


if __name__ == "__main__":
    some_article = article(doi='10.1002/14651858.CD002020.PUB3')
    print(some_article)

    other_article = article(doi='10.1128/GENOMEA.01316-16')
    print(other_article)

    one_more_article = article(pmid='22238442')
    print(one_more_article)
