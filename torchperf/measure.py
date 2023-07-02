import torch
from functools import wraps, partial


def perf(_func=None, *, o=None, n=1):
    if not _func:
        return partial(perf, o=o, n=n)

    @wraps(_func)
    def measure_time(*args, **kwargs):
        tot, cnt = 0.0, 0
        for _ in range(n):
            stt = torch.cuda.Event(enable_timing=True)
            end = torch.cuda.Event(enable_timing=True)
            stt.record()
            rst = _func(*args, **kwargs)
            end.record()
            torch.cuda.synchronize()
            tim = stt.elapsed_time(end)
            if o is None:
                tot += tim
                cnt += 1
            else:
                o.append(tim)
        if o is None:
            print(tot / cnt)
        return rst

    return measure_time
