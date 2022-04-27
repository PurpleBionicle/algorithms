import pytest

from Sort.Some_bubble import Bubble, Shaker, Comb



@pytest.mark.parametrize('list,result', [([15, 4, 3, 2, 1], [1, 2, 3, 4, 15]),
                                             ([515, 0, True, 616, 1.2], [0, 1, 1.2, 515, 616]),
                                             ([-1, -5, 61, 135], [-5, -1, 61, 135])])
def test_with_substr(list, result):
    assert Bubble.sort(list) == result
    assert Comb.sort(list) == result
    assert Shaker.sort(list) == result

@pytest.mark.parametrize('list,result', [(True, [1, 2, 3, 4, 15]),
                                             ((515, 0, True, 616, 1.2), [0, 1, 1.2, 515, 616])])
def test_with_exception(list, result):
    with pytest.raises(TypeError):
        assert Bubble.sort(list) == result
        assert Comb.sort(list) == result
        assert Shaker.sort(list) == result
