from practice_day3 import (NAMES, dedup_and_title_case_names,
                           sort_by_surname_desc, shortest_first_name,
                           filter_bites, exclude_bites)


def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Julian Sequeira') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'


def test_shortest_first_name():
    shortest_name = shortest_first_name(NAMES)
    assert shortest_name == 'Al'


def test_filter_bites():
    result = filter_bites()
    assert type(result) == dict
    assert len(result) == 10
    for bite in exclude_bites:
        assert bite not in result, 'Bite {} should not be in result'.format(bite)
