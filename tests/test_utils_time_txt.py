import pytest

from gridplayer.utils.time_txt import get_time_txt


@pytest.mark.parametrize(
    "time_int,time_str",
    [
        (0, "0:00.000"),
        (123, "0:00.123"),
        (59000, "0:59.000"),
        (60000, "01:00.000"),
        (3599000, "59:59.000"),
        (3600000, "01:00:00.000"),
        (86399456, "23:59:59.456"),
        (86400000, "1d 0:00.000"),
        ((86400 + 60)*1000, "1d 01:00.000"),
        ((86400 * 2 - 1)*1000, "1d 23:59:59.000"),
        ((86400 * 2)*1000, "2d 0:00.000"),
    ],
)
def test_get_time_txt(time_int, time_str):
    assert get_time_txt(time_int) == time_str
    pass


@pytest.mark.parametrize(
    "time_int,max_time_int,time_str",
    [
        (0, 60000, "00:00.000"),
        (0, 3600000, "00:00:00.000"),
        (0, 86400000, "00:00:00.000"),
    ],
)
def test_get_time_txt_maxtime(time_int, max_time_int, time_str):
    assert get_time_txt(time_int, max_time_int) == time_str
    pass


@pytest.mark.parametrize(
    "time_int,time_str",
    [
        (0, "0:00.000"),
        (59000, "0:59.000"),
        (60000, "1:00.000"),
        (3599000, "59:59.000"),
        (3600000, "1:00:00.000"),
        (86399000, "23:59:59.000"),
        (86400000, "1d 0:00.000"),
        ((86400 + 60)*1000, "1d 1:00.000"),
        ((86400 * 2 - 1)*1000, "1d 23:59:59.000"),
        ((86400 * 2)*1000, "2d 0:00.000"),
    ],
)
def test_get_time_txt_strip(time_int, time_str):
    assert get_time_txt(time_int, strip=True) == time_str
    pass
