import pytest

from Search_substring import direct_passage, RK, BMH, KMP


@pytest.mark.parametrize('str,substr,result', [('a', 'a', 0),
                                               ('acba', 'a', 0),
                                               ('abcde', 'e', 4),
                                               ('smart people review more', 'review', 13)])
def test_with_substr(str, substr, result):
    assert direct_passage.substr_search(str, substr) == result
    assert RK.substr_search(str, substr) == result
    assert BMH.substr_search(str, substr) == result
    assert KMP.substr_search(str, substr) == result


@pytest.mark.parametrize('str,substr,result', [('a', 'good', -1),
                                               ('acba', 'r', -1),
                                               ('abcde', 'kuk', -1),
                                               ('smart people review more', 'less', -1)])
def test_without_substr(str, substr, result):
    assert direct_passage.substr_search(str, substr) == result
    assert RK.substr_search(str, substr) == result
    assert BMH.substr_search(str, substr) == result
    assert KMP.substr_search(str, substr) == result


@pytest.mark.parametrize('str,substr,result', [('a', 12, -1),
                                               (12, 'a', -1),
                                               (1.5, 'b', -1),
                                               ('smart people review more', None, -1)])
def test_with_exception(str, substr, result):
    with pytest.raises(TypeError):
        assert direct_passage.substr_search(str, substr) == result
        assert RK.substr_search(str, substr) == result
        assert BMH.substr_search(str, substr) == result
        assert KMP.substr_search(str, substr) == result
