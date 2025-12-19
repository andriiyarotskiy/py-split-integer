import pytest
from typing import Union, List
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected",
        [
            pytest.param(
                8,
                1,
                [8],
                id="Should be list instance"
            ),
            pytest.param(
                6,
                2,
                [3, 3],
                id="Length of the parts is equal to number_of_parts"
            ),
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id="Should be sorted when not equal"
            ),
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="Should be above 0"
            ),
            pytest.param(
                21,
                4,
                [5, 5, 5, 6],
                id="Sum of the parts should be equal to value"
            )
        ])
    def test_split_integer_is_working_properly(
            self,
            value: Union[int, float],
            number_of_parts: Union[int, float],
            expected: List[Union[int, float]]
    ) -> None:
        parts = split_integer(value, number_of_parts)
        assert isinstance(parts, list)
        assert len(parts) == number_of_parts
        assert parts == sorted(parts)
        assert max(parts) - min(parts) <= 1
        assert sum(parts) == value
