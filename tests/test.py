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
__description__ = 'test of tip-library components'

import pytest

from tip_lib.Authors import Authors
from tip_lib.Institution import Institution
from tip_lib.Journal import Journal

'''check the input to get wikidata_IDs'''

def test_orcid_input():
    obj = Authors(orcid='0000-0003-4619-697X')
    result = Authors._get_wd_id_by_orcid(obj)
    print('result')
    print(result)
    assert isinstance(result, dict)
    assert result['Wikidata-ID'] == 'Q40466811'
test_orcid_input()



def test_isni_input():
    obj_Authors = Authors(isni='0000 0001 2117 8244')
    result_Authors= obj_Authors._get_wd_id_by_isni()
    obj_Institution = obj_Institution(isni='0000 0001 2165 487X')
    result_Institution = obj_Institution._get_wd_id_by_isni()
    assert type(result_Authors) == dict
    assert result_Authors == result_Authors(['Wikidata-ID'], 'Q1325')
    assert type(result_Institution) == dict
    assert result_Institution == result_Institution(['Wikidata-ID'], '546118')
test_isni_input()

def test_issn_input():
    obj = Journal(issn='1532-2882')
    result = obj._get_wd_id_by_issn()
    assert type(result) == dict
    assert result == result(['Wikidata-ID'], 'Q152040')
test_issn_input()



'''check the retrieval of features'''

def test_get_gender():
    obj = Authors('Q40904')
    result = obj._get_gender()
    assert type (result) == dict
    assert result == result(['Gender'], 'male')
test_get_gender()

def test_get_affiliation():
    obj = Authors('Q2395341')
    result = obj._get_affiliation()
    assert type (result) == dict
    assert result == result(['Affiliation'], ['University of Tokyo', 'Kyoto University', 'Osaka University', 'Hirosaki University'])
test_get_affiliation()

def test_get_name():
    obj_Authors = Authors('Q2395341')
    obj_Journal = Journal('Q180445')
    result_Authors = obj_Authors._get_name()
    result_Journal = obj_Journal._get_name()
    assert type(result_Authors) == dict
    assert result_Authors(['Name'], 'Tasuku Honjo')
    assert type(result_Journal) == dict
    assert result_Journal(['Name'], 'Nature')
test_get_name()

def test_get_orcid():
    obj = Authors('Q40466811')
    result = obj._get_orcid()
    assert type(result) == dict
    assert result(['ORCID'], 'Q40466811')
test_get_orcid()

def test_get_parents():
    obj = Authors('Q40904')
    result = obj._get_parents()
    assert type(result) == dict
    assert result(['Parents'], ['August Heisenberg', 'Annie Heisenberg'])
test_get_parents()

def test_get_country():
    obj = Institution('Q251061')
    result = obj._get_country()
    assert type(result) == dict
    assert result(['Country'], 'Germany')
test_get_country()

def test_get_country_of_origin():
    obj = Journal('Q180445')
    result = obj._get_country_of_origin()
    assert type(result) == dict
    assert result(['Country'], 'United Kingdom')
test_get_country_of_origin()

def test_get_publisher():
    obj = Journal('Q180445')
    result = obj._get_publisher()
    assert type(result) == dict
    assert result(['Publisher'], 'Nature Publishing Group')
test_get_publisher()

def test_get_review_score():
    obj = Journal('Q180445')
    result = obj._get_review_score()
    assert type(result) == dict
    assert type(result(['Review_score'], int))
test_get_review_score()

def test_get_main_subject():
    obj = Journal('Q180445')
    result = obj._get_main_subject()
    assert type(result) == dict
    assert result(['Main subjecct'], 'science')
test_get_main_subject()

def test_get_type():
    obj = Institution('Q251061')
    result = obj._get_type()
    assert type(result) == dict
    assert result(['Type'], 'research institute')
test_get_type()

def test_get_students_count():
    obj = Institution('Q251061')
    result = obj._get_students_count()
    assert type(result) == dict
    assert result(['Students count'], '11574')
test_get_students_count()

def test_get_tuition():
    obj = Institution('Q251061')
    result = obj._get_tuition()
    assert type(result) == dict
    assert result(['Tuition'], ['54,000,000 Indonesian Rupiah', '19,500,000 Indonesian Rupiah'])
test_get_tuition()













'''
Honja = Authors(wd_id='Q2395341')
print(Honja)
        Heisenberg = Authors('Q40904')
        print(Heisenberg)
        Alexopoulou = Authors(orcid='0000-0003-4619-697X')
        print(Alexopoulou)
        Hayek = Authors(isni='0000 0001 2117 8244')
        print(Hayek)

        # instanciate an instance for class institution:
        PotsdamInstitut = Institution('Q251061')
        print(PotsdamInstitut)
        Sorbonne = Institution(isni='0000 0001 2165 487X')
        print(Sorbonne)
        UniversityFaisalabad = Institution('Q7895389')
        print(UniversityFaisalabad)
        MIT = Institution('Q49108')
        print(MIT)
        SwissGermanUniversity = Institution(isni='0000 0004 0387 1442')
        print(SwissGermanUniversity)

        # instanciate an instance for class Journal:

        Nature = Journal('Q180445')
        print(Nature)
        JASIST = Journal(issn='1532-2882')
        print(JASIST)
'''