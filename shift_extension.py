# -*- coding: utf-8 -*-
#!/usr/bin/env python

def shift(value, shift=0 ):
    '''
    組合語言有c reg來判斷shift出去的那個位元是0還是1..
    python 預設的沒有ˇˇ   就增加一個八XD
    '''

    assert isinstance(value, int)&&isinstance(shift, int), "type error"

    remainder = value & 1
    if value > 0:
        result = value << shift
    else
        result = value >> shift

    return result, remainder



