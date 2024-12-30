import pytest

from genstr import Genstr
from genstr import Mode


class TestMode2:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mode = Mode.PURE_LETTERS

    def test_a_to_z(self):
        list = Genstr(
            length=1,
            mode=self.mode
        ).combine().list()
        assert list[0] == 'a'
        length = len(list)
        assert length == 26
        assert list[length - 1] == 'z'

    def test_aa_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode
        ).combine().list()
        assert list[0] == 'aa'
        length = len(list)
        assert length == 676
        assert list[length - 1] == 'zz'

    def test_a_to_zz(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True
        ).combine().list()
        assert list[0] == 'a'
        length = len(list)
        assert length == 702
        assert list[length - 1] == 'zz'

    def test_between_one(self):
        list = Genstr(
            length=2,
            mode=self.mode,
            is_range=True,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aa'
        length = len(list)
        assert length == 26
        assert list[length - 1] == 'az'


    def test_between_two(self):
        list = Genstr(
            length=3,
            mode=self.mode,
            prefix='a'
        ).combine().list()
        assert list[0] == 'aaa'
        length = len(list)
        assert length == 676
        assert list[length - 1] == 'azz'
