
# coding: utf-8

# In[1]:


from traitlets.utils.bunch import Bunch


# In[ ]:


def append_new_map(tmp_bunch: Bunch, map_name: str, url: str, max_zoom: int,
                   attribution: str, name: str) -> Bunch:
    tmp_bunch.__setattr__(map_name, dict(
        url = url,
        max_zoom = max_zoom,
        attribution = attribution,
        name = name
    ))
    return tmp_bunch

