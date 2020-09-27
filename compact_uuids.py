#
# Compact 26-char URL-safe representation of UUIDs
#
import uuid
import base64
from base32_crockford import encode, decode
import sys

def uuid_to_str26( _uuid: uuid ) -> str:
    '''
    In: uuid
    Returns: 26-char representation of uuid
    '''
    res = encode( _uuid.int )
    l = len( res )
    if l < 26:
        prefix = ''.join( '0' for _ in range ( 26-l ) )
        res = prefix + res
    return res

def str26_to_int( string: str ) -> int:
    '''
    In: string, 26char encoding of uuid
    Returns: Int of uuid
    '''
    return decode( string )

def uuid_to_str22( _uuid: uuid ) -> str:
    '''
    In: uuid, 16 bytes
    Returns 22 char representationof uuid.
    '''
    barray = _uuid.int.to_bytes( 16, byteorder=sys.byteorder )
    res = base64.urlsafe_b64encode( barray )
    strres = res.decode()
    # discard padding '='
    return strres[:-2]

def str22_to_int( string: str ) -> int:
    '''
    In: 22char encoding of uuid
    Returns Int of uuid
    '''
    # restore padding and make a byte array
    ba = bytearray( string + '==', encoding="utf-8" )
    barray = base64.urlsafe_b64decode( ba )
    return int.from_bytes( barray, byteorder=sys.byteorder )

