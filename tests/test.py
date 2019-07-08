#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Eva Seidlmayer'
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
    result = obj.wd_id
    assert result == 'Q40466811'
    assert isinstance(obj, Authors)


test_orcid_input()


def test_isni_input():
    obj_Authors = Authors(isni='0000 0001 2117 8244')
    result_Authors = obj_Authors.wd_id
    assert isinstance(obj_Authors, Authors)
    assert result_Authors == 'Q1325'

    obj_Institution = Institution(isni='0000 0001 2165 487X')
    result_Institution = obj_Institution.wd_id
    assert isinstance(obj_Institution, Institution)
    assert result_Institution == 'Q546118'


test_isni_input()


def test_issn_input():
    obj = Journal(issn='1532-2882')
    result = obj.wd_id
    assert isinstance(obj, Journal)
    assert result == 'Q152040'


test_issn_input()

'''check the retrieval of features'''


def test_get_gender():
    obj = Authors(wd_id='Q40904')
    result = obj.gender
    assert isinstance(obj, Authors)
    assert result == 'male'
    assert isinstance(result, str)


test_get_gender()


def test_get_affiliation():
    obj = Authors('Q2395341')
    result = obj.affiliation
    assert isinstance(obj, Authors)
    assert result == ['University of Tokyo', 'Osaka University', 'Hirosaki University', 'Kyoto University']


test_get_affiliation()


def test_get_name():
    obj_Authors = Authors('Q2395341')
    obj_Journal = Journal('Q180445')
    result_Authors = obj_Authors.name
    result_Journal = obj_Journal.name
    assert isinstance(obj_Authors, Authors)
    assert result_Authors == 'Tasuku Honjo'
    assert isinstance(obj_Journal, Journal)
    assert result_Journal == 'Nature'


test_get_name()


def test_get_orcid():
    obj = Authors('Q40466811')
    result = obj.orcid
    assert isinstance(obj, Authors)
    assert result == '0000-0003-4619-697X'


test_get_orcid()


def test_get_parents():
    obj = Authors('Q40904')
    result = obj.parents
    assert isinstance(obj, Authors)
    assert result == ['August Heisenberg', 'Q72885', 'Annie Heisenberg', 'Q27908660']


test_get_parents()


def test_get_country():
    obj = Institution('Q251061')
    result = obj.country
    assert isinstance(obj, Institution)
    assert result == 'Germany'


test_get_country()


def test_get_country_of_origin():
    obj = Journal('Q180445')
    result = obj.country_of_origin
    assert isinstance(obj, Journal)
    assert result == 'United Kingdom'


test_get_country_of_origin()


def test_get_publisher():
    obj = Journal('Q180445')
    result = obj.publisher
    assert isinstance(obj, Journal)
    assert result == 'Nature Publishing Group'


test_get_publisher()


def test_get_review_score():
    obj = Journal('Q180445')
    result = obj.review_score
    assert isinstance(obj, Journal)
    assert isinstance(result, str)


test_get_review_score()


def test_get_main_subject():
    obj = Journal('Q180445')
    result = obj.main_subject
    assert isinstance(obj, Journal)
    assert result == 'science'


test_get_main_subject()


def test_get_type():
    obj = Institution('Q251061')
    result = obj.type
    assert isinstance(obj, Institution)
    assert result == 'research institute'


test_get_type()


def test_get_students_count():
    obj = Institution('Q49108')
    result = obj.students_count
    print(result)
    assert isinstance(obj, Institution)
    assert result == '11574'


test_get_students_count()


def test_get_tuition():
    obj = Institution('Q151510')
    result = obj.tuition
    assert isinstance(obj, Institution)
    assert result == '1,500'


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
        Heidelberg university= Q151510

# instanciate an instance for class Journal:
        Nature = Journal('Q180445')
        print(Nature)
        JASIST = Journal(issn='1532-2882')
        print(JASIST)
'''
