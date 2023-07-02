# PyTorch Perf

## Install

```
pip install -U pytorch-perf
```

## Usage

```python
import torch
from torchperf import perf, info

info.show()

N = 100
x = torch.rand(N, N, device="cuda")
results = []
repeats = 100

@perf(o=results, n=repeats)
def mul(x, y):
    return x * y

z = mul(x, x)
print(results[:5])
print("avg:", sum(results)/len(results))


@perf(n=repeats)
def mul(x, y):
    return x * y

z = mul(x, x)

```

