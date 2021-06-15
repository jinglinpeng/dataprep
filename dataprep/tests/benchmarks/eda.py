#%%
from functools import partial
import time
from ...datasets import load_dataset
from ...eda import create_report

def report_func(df, **kwargs):
    time.sleep(10)
    create_report(df, **kwargs)


def test_create_report(benchmark):
    df = load_dataset("titanic")
    benchmark(partial(report_func), df)
