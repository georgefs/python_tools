import collections


def convert(data, encode='utf-8'):
    """
        decode dict unicode type value convert to str 
        
        shell demo

        >>a={"a":u"value"}
        >>convert(a)
        {"a":"value"}

    """
    
    if isinstance(data, unicode):
        return data.encode(encode)
    elif isinstance(data, str):
        return data
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

    
