import uuid
import unittest

from compact_uuids import (
    uuid_to_str26, 
    str26_to_int,
    uuid_to_str22,
    str22_to_int,
)

class compact_uuids_test( unittest.TestCase ):
    def test_26( self ):
        print( '\n12345678901234567890123456789012 12345678901234567890123456')
        for _ in range( 30 ):
            u1 = uuid.uuid4()
            self.assertEqual( len( str(u1) ), 36 )
            str26 = uuid_to_str26( u1 )
            self.assertEqual( len( str26 ), 26 )
            int26 = str26_to_int( str26 )
            self.assertEqual( u1.int, int26 )
            print( f'{u1.hex} {str26}')
        return

    def test_22( self ):
        print( '\n12345678901234567890123456789012 1234567890123456789012')
        for _ in range( 30 ):
            u1 = uuid.uuid4()
            self.assertEqual( len( str(u1) ), 36 )
            str22 = uuid_to_str22( u1 )
            self.assertEqual( len( str22 ), 22 )
            int22 = str22_to_int( str22 )
            self.assertEqual( u1.int, int22 )
            print( f'{u1.hex} {str22}')
        return

if __name__ == '__main__':
    unittest.main()
