# TIPlib
TAKE IT PERSONALLY (TIP) - A Python library for data enrichment for infometrical applications

## Basic Idea:
As every other social sphere, science is influenced by social structures. The Python library TIP is developed to improve the data foundation for scientiometric investigations Applying TIP will allow people to enrich publication data with information on the authors such as affiliation, gender or academic family background.

By providing identifiers (e.g. DOI or ORCID) information can be retrieved via TIP library from Wikidata. In the future we aim for further integration of other databases as CrossRef. The information can be retrieved using the Wikidata API and SPARQLWrapper for SPARQL queries.

* Three classes are provided: authors, journals and institutions
* So far, the enrichment can be performed using DOI, ORCID, ISNI, VIAF, ISSN
* Attributes that can be sought:
** Authors: identifiers, gender, affiliations history, parents
** Institution: country, type, students_count, tuition
** Journals: country of origin, publisher, review score, main subject
* Data hub for information is currently Wikidata
