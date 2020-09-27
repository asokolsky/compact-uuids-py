import uuid
import unittest

from compact_uuids import (
    uuid_to_str26, 
    str26_to_int,
    uuid_to_str22,
    str22_to_int,
)

class compact_uuids_test( unittest.TestCase ):

    @classmethod
    def setUpClass( cls ):
        cls.uuids = []
        # generate uuids to play with... 40 of those.
        for _ in range( 40 ):
            cls.uuids.append( uuid.uuid4() )
        return

    def test_26( self ):
        '''
        Test 26-char representation
        '''
        print( '\n12345678901234567890123456789012 12345678901234567890123456')
        for u1 in self.uuids:
            self.assertEqual( len( str(u1) ), 36 )
            str26 = uuid_to_str26( u1 )
            self.assertEqual( len( str26 ), 26 )
            int26 = str26_to_int( str26 )
            self.assertEqual( u1.int, int26 )
            print( f'{u1.hex} {str26}')
        return

    def test_22( self ):
        '''
        Test 22-char representation
        '''
        print( '\n12345678901234567890123456789012 1234567890123456789012')
        for u1 in self.uuids:
            self.assertEqual( len( str(u1) ), 36 )
            str22 = uuid_to_str22( u1 )
            self.assertEqual( len( str22 ), 22 )
            int22 = str22_to_int( str22 )
            self.assertEqual( u1.int, int22 )
            print( f'{u1.hex} {str22}')
        return

    def test_both( self ):
        '''
        Compare uuid representation
        '''
        print( '\n12345678901234567890123456789012 12345678901234567890123456 1234567890123456789012')
        for u1 in self.uuids:
            str26 = uuid_to_str26( u1 )
            self.assertEqual( len( str26 ), 26 )
            int26 = str26_to_int( str26 )
            self.assertEqual( u1.int, int26 )

            str22 = uuid_to_str22( u1 )
            self.assertEqual( len( str22 ), 22 )
            int22 = str22_to_int( str22 )
            self.assertEqual( u1.int, int22 )

            print( f'{u1.hex} {str26} {str22}')
        return

if __name__ == '__main__':
    unittest.main()
