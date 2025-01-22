#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import List, Callable
from os import path, makedirs, PathLike


# In[ ]:


__all__ = [
    'shot',
    'clean',
    'lclean',
    'ensure_path'
]


# In[ ]:


def shot(f: Callable[[str], str], s: str, times: int) -> str:
    for _ in range(times): s = f(s)
    return s


# In[ ]:


def lclean(l: List[str]) -> List[str]:
    for line in l:
        line = clean(line)
        if (len(line) >= 12):
            yield line


# In[ ]:


def clean(line: str) -> str:
    line = shot(f=(lambda s: s.replace('  ', ' ')), s=line, times=6)
    line = shot(f=(lambda s: s.replace('\n\n', '\n')), s=line, times=6)
    line = line.replace("<|startoftext|>", '')
    return line


# In[ ]:


def ensure_path(directory: PathLike, *args: PathLike) -> PathLike:
    if args: directory = path.join(directory, *args)
    if not path.exists(directory): makedirs(directory)
    return directory

