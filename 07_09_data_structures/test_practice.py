from practice import (get_all_jeeps, get_first_model_each_manufacturer,
                      get_all_matching_models)


def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected


def test_get_all_matching_models():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected
    expected = ['350Z']
    assert get_all_matching_models('350') == expected
