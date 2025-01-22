#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import Enum


# In[ ]:


__all__ = [
    'Runs',
    'Actions',
    'Models',
    'Keys',
]


# In[ ]:


class Runs(str, Enum):
    mauri  = "Mauri Priest"
    pony   = "Pony_txt"
    umbrum = "UmbrumML"
    alicorn = "AlicornML"
    bible_es = "BibleButAI-es"
    bible_en = "BibleButAI-en"
    bible_en_plus = "BibleButAI-en+"

class Actions(int, Enum):
    TRAIN = 0
    GENERATE = 1
    LOAD = 2
    SAVE = 3
    SAVE_REC = 4
    EXTRA = 5
    GRAPH = 6
    GRAPH_TXT = 7
    PULL = 8
    
class Models(str, Enum):
    M1558 = "1558M"
    M774  = "774M"
    M355  = "355M"
    M345  = "345M"
    M124  = "124M"
    M117  = "117M"

class Keys(str, Enum):
    START_KEY = "<|startoftext|>"
    END___KEY = "<|endoftext|>"

