import pytest

from tip import Authors
from tip import Institution
from tip import Journal



'''check the input to get wikidata_IDs'''
@pytest.
def test_orcid_input(self):
    result = _get_wd_id_by_orcid(Authors(orcid='0000-0003-4619-697X'))
    assert type(result) == dict
    assert result == result([' Wikidata-ID'],Q40466811)

@pytest.
def test_isni_input(self):
    result_Author = _get_wd_id_by_isni(Authors(isni='0000 0001 2117 8244'))
    result_Institution = _get_wd_id_by_isni(Institution(isni='0000 0001 2165 487X'))
    assert type(result_Author) == dict
    assert result_Author == result_Author(['Wikidata-ID'], Q1325)
    assert type(result_Institution) == dict
    assert result_Institution == result_Institution(['Wikidata-ID'], 546118)

@pytest.
def test_issn_input(self):
    result = _get_wd_id_by_issn(Journal(issn='1532-2882'))
    assert type(result) == dict
    assert result == result(['Wikidata-ID'], Q152040)




'''check the retrieval of features'''
@pytest.
def test_get_gender(self):
    result = _get_gender(Authors('Q40904'))
    assert type (result) == dict
    assert result == result(['Gender'], male)

@pytest.
def test_get_affiliation(self):
    result = _get_affiliation(Authors('Q2395341'))
    assert type (result) == dict
    assert result == result(['Affiliation'], [University of Tokyo, Kyoto University, Osaka University, Hirosaki University])

@pytest.
def test_get_name(self):
    result_Authors = _get_name(Authors('Q2395341'))
    result_Journal = _get_name(Journal('Q180445'))
    assert type(result_Authors) == dict
    assert result_Authors(['Name'] )
    assert type(result_Journal) == dict
 
@pytest.
def test_get_orcid(self):
    result = _get_orcid(Authors('Q40904'))
    assert type(result) == dict

@pytest.
def test_get_parents(self):
    result = _get_parents(Authors('Q40904'))
    assert type(result) == dict

@pytest.
def test_get_country(self):
    result = _get_country(Institution('Q251061'))
    assert type(result) == dict

@pytest.
def test_get_country_of_origin(self):
    result = _get_country_of_origin(Journal('Q180445'))
    assert type(result) == dict

@pytest.
def test_get_publisher(self):
    result = _get_publisher(Journal('Q180445'))
    assert type(result) == dict

@pytest.
def test_get_review_score(self):
    result = _get_review_score(Journal('Q180445'))
    assert type(result) == dict

@pytest.
def test_get_main_subject(self):
    result = _get_main_subject(Journal('Q180445'))
    assert type(result) == dict

@pytest.
def test_get_type(self):
    result = _get_type(Institution('Q251061'))
    assert type(results) == dict

@pytest.
def test_get_students_count(self):
    result = _get_students_count(Institution('Q251061'))
    assert type(results) == dict

@pytest.
def test_get_tuition(self):
    result = _get_tuition(Institution('Q251061'))
    assert type(results) == dict













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