#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# coding: utf-8


# In[2]:


from IPython.utils.capture import capture_output
import gpt_2_simple as gpt2
from tqdm.auto import tqdm
from random import randint
from pprint import pprint
import tensorflow as tf
from enum import Enum
import os


# In[3]:


class Actions(Enum):
    TRAIN = 0
    GENERATE = 1


# In[4]:


config = {
    "action":          Actions.GENERATE,
    "run_name":        "BibleButAI-en+",
    "model_name":      ["1558M", "774M", "355M", "345M", "124M", "117M"][1],
}


# In[5]:


corpus = os.path.join('corpus', config["run_name"], f'{config["run_name"]}.{config["model_name"]}.npz').replace('+', '')


# In[6]:


config_train = {
    "dataset":                       corpus,
    "steps":                         500,
    "model_name":                    config["model_name"],
    "batch_size":                    1,
    "learning_rate":                 0.00001,
    "accumulate_gradients":          10,
    "run_name":                      config["run_name"],
    "sample_every":                  50,
    "sample_length":                 1023,
    "sample_num":                    5,
    "save_every":                    50,
    "print_every":                   1,
    "max_checkpoints":               2,
}


# In[7]:


config_gen = {
    "run_name":          config["run_name"],
    "model_name":        config["model_name"],
    "return_as_list":    True,
    "prefix":            '<|startoftext|> ',
    "truncate":          ' <|endoftext|>',
    "sample_delim":      '--------- SEPARATOR ---------',
    "nsamples":          12,
    "batch_size":        1,
    "length":            120,
    "temperature":       0.7,
    "include_prefix":    True,
}


# In[8]:


def clean(t: str) -> str:
    return(t.replace('<|startoftext|>', '').replace('<|endoftext|>', '').replace('oftext|>', '').replace('text|>', '').replace('<|>', '').replace('\n', '').strip().replace('\n', ''))


# In[9]:


def lclean(l: list):
    for t in l:
        yield clean(t)


# In[10]:


if not os.path.isdir(os.path.join("models", config["model_name"])):
    gpt2.download_gpt2(model_name=config["model_name"])


# In[11]:


if not(os.path.isfile(corpus)):
    gpt2.encode_dataset(
        file_path=os.path.join('corpus', config["run_name"], f'{config["run_name"]}.txt'),
        out_path=os.path.join('corpus', config["run_name"], f'{config["run_name"]}.{config["model_name"]}.npz'),
        model_name=config["model_name"],
    )


# In[12]:


if (config["action"] == Actions.GENERATE):
    outputs = []
    cleaned_ = []


# In[13]:


if (config["action"] == Actions.GENERATE):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=config["run_name"])
    for heat in tqdm(range(0, 9)):
        heat = (heat + randint(0, 9)) / 10
        outputs.append({
            "text":   gpt2.generate(sess, temperature=heat, **config_gen),
            "config": config,
            "heat": heat,
        })
        pprint(list(lclean(outputs[-1]["text"])))


# 

# In[ ]:


if (config["action"] == Actions.TRAIN):
    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess, **config_train)


# In[ ]:




