from typing import Optional

SEC_MS = 1000
MIN_MS = SEC_MS * 60
HOUR_MS = MIN_MS * 60
DAY_MS = HOUR_MS * 24


def get_time_txt(
    ms: int, max_ms: Optional[int] = None, strip: bool = False,
    show_days: bool = True
) -> str:

    if max_ms and max_ms < ms:
        max_ms = None

    max_ms = max_ms or ms

    n_day, ms = divmod(ms, DAY_MS)
    n_hour, ms = divmod(ms, HOUR_MS)
    n_min, ms = divmod(ms, MIN_MS)
    n_sec, ms = divmod(ms, SEC_MS)

    if show_days:
        n_hour += n_day * 24
        n_day = 0

    if max_ms >= HOUR_MS:
        clock = f'{n_hour:02d}:{n_min:02d}:{n_sec:02d}.{ms:03d}'
    elif max_ms >= MIN_MS:
        clock = f'{n_min:02d}:{n_sec:02d}.{ms:03d}'
    else:
        clock = f'0:{n_sec:02d}.{ms:03d}'

    if strip and max_ms >= MIN_MS:
        clock = clock.lstrip("0")

    if n_day > 0:
        clock = f'{n_day}d {clock}'

    return clock
