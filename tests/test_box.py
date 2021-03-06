#!/usr/bin/env python
"""
   Copyright 2016 beardypig, Copyright 2021 CodeShop B.V. 

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import logging
import unittest

from construct import Container
from pymp4.parser import Box
from pymp4.util import BoxUtil

log = logging.getLogger(__name__)

 # sample table of 4 seconds audio file
l_stbl_audio_4s = b'\x00\x00\x04\x00stbl\x00\x00\x004stsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00$mp4a\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x10\x00\x00\x00\x00\xbb\x80\x00\x00\x00\x00\x006esds\x00\x00\x00\x00\x03\x80\x80\x80%\x00\x01\x00\x04\x80\x80\x80\x17@\x15\x00\x00\x00\x00\x02\tP\x00\x02\tP\x05\x80\x80\x80\x05\x11\x90V\xe5\x00\x06\x80\x80\x80\x01\x02\x00\x00\x00 stts\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\xbc\x00\x00\x04\x00\x00\x00\x00\x01\x00\x00\x02\x00\x00\x00\x00\x1cstsc\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\xbd\x00\x00\x00\x01\x00\x00\x03\x08stsz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbd\x00\x00\x00\x17\x00\x00\x01\xe5\x00\x00\x02\xda\x00\x00\x02\xdc\x00\x00\x02\xc6\x00\x00\x02\xe4\x00\x00\x02\xe7\x00\x00\x01\xdc\x00\x00\x01\xdf\x00\x00\x01\xb4\x00\x00\x01\x80\x00\x00\x01\x7f\x00\x00\x01\x8b\x00\x00\x01\\\x00\x00\x01k\x00\x00\x01\x85\x00\x00\x01t\x00\x00\x01p\x00\x00\x01^\x00\x00\x01e\x00\x00\x01f\x00\x00\x01j\x00\x00\x01N\x00\x00\x01c\x00\x00\x01b\x00\x00\x01S\x00\x00\x01\\\x00\x00\x01Y\x00\x00\x01W\x00\x00\x01W\x00\x00\x01<\x00\x00\x01N\x00\x00\x01@\x00\x00\x01I\x00\x00\x01g\x00\x00\x01b\x00\x00\x01]\x00\x00\x01>\x00\x00\x01^\x00\x00\x01D\x00\x00\x01a\x00\x00\x01`\x00\x00\x01c\x00\x00\x01W\x00\x00\x01T\x00\x00\x01Y\x00\x00\x01c\x00\x00\x01Z\x00\x00\x01Y\x00\x00\x01Y\x00\x00\x01U\x00\x00\x01Q\x00\x00\x01S\x00\x00\x01Y\x00\x00\x01A\x00\x00\x01F\x00\x00\x01[\x00\x00\x01{\x00\x00\x01c\x00\x00\x01_\x00\x00\x01S\x00\x00\x01f\x00\x00\x018\x00\x00\x01@\x00\x00\x01Z\x00\x00\x01e\x00\x00\x01^\x00\x00\x01W\x00\x00\x01Q\x00\x00\x01Q\x00\x00\x01V\x00\x00\x01T\x00\x00\x01W\x00\x00\x01Y\x00\x00\x01?\x00\x00\x01F\x00\x00\x01_\x00\x00\x01\\\x00\x00\x01B\x00\x00\x01c\x00\x00\x01d\x00\x00\x01>\x00\x00\x01i\x00\x00\x01\\\x00\x00\x01\\\x00\x00\x01B\x00\x00\x01J\x00\x00\x01e\x00\x00\x01@\x00\x00\x01]\x00\x00\x01]\x00\x00\x01M\x00\x00\x01^\x00\x00\x01^\x00\x00\x01X\x00\x00\x01?\x00\x00\x01e\x00\x00\x01`\x00\x00\x01Y\x00\x00\x01D\x00\x00\x01]\x00\x00\x01=\x00\x00\x01i\x00\x00\x01h\x00\x00\x01C\x00\x00\x01]\x00\x00\x01a\x00\x00\x01S\x00\x00\x01b\x00\x00\x01`\x00\x00\x01@\x00\x00\x01\\\x00\x00\x01Z\x00\x00\x01e\x00\x00\x01Z\x00\x00\x01B\x00\x00\x01<\x00\x00\x01P\x00\x00\x01e\x00\x00\x01[\x00\x00\x01f\x00\x00\x01]\x00\x00\x01X\x00\x00\x01a\x00\x00\x01T\x00\x00\x01V\x00\x00\x01<\x00\x00\x01_\x00\x00\x01`\x00\x00\x01^\x00\x00\x01\\\x00\x00\x01]\x00\x00\x01S\x00\x00\x01=\x00\x00\x01X\x00\x00\x01a\x00\x00\x01X\x00\x00\x01^\x00\x00\x01:\x00\x00\x01a\x00\x00\x01E\x00\x00\x01b\x00\x00\x01Z\x00\x00\x01^\x00\x00\x01V\x00\x00\x01?\x00\x00\x01i\x00\x00\x01[\x00\x00\x01[\x00\x00\x01V\x00\x00\x019\x00\x00\x01D\x00\x00\x01Y\x00\x00\x01f\x00\x00\x01:\x00\x00\x01j\x00\x00\x01a\x00\x00\x01^\x00\x00\x01S\x00\x00\x01]\x00\x00\x01U\x00\x00\x01c\x00\x00\x01R\x00\x00\x01U\x00\x00\x01Z\x00\x00\x01U\x00\x00\x01^\x00\x00\x01>\x00\x00\x01B\x00\x00\x01e\x00\x00\x01Z\x00\x00\x01^\x00\x00\x01B\x00\x00\x01D\x00\x00\x01l\x00\x00\x01e\x00\x00\x01\\\x00\x00\x01A\x00\x00\x01a\x00\x00\x01X\x00\x00\x01E\x00\x00\x01g\x00\x00\x01i\x00\x00\x01V\x00\x00\x01d\x00\x00\x01X\x00\x00\x019\x00\x00\x01A\x00\x00\x01H\x00\x00\x00\x14stco\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00,\x00\x00\x00\x1asgpd\x01\x00\x00\x00roll\x00\x00\x00\x02\x00\x00\x00\x01\xff\xff\x00\x00\x00\x1csbgp\x00\x00\x00\x00roll\x00\x00\x00\x01\x00\x00\x00\xbd\x00\x00\x00\x01'
l_movie_box_audio = b'\x00\x00\x05\xefmoov\x00\x00\x00lmvhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe8\x00\x00\x0f\xb6\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x05\x19trak\x00\x00\x00\\tkhd\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x0f\xb6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$edts\x00\x00\x00\x1celst\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x0f\xa0\x00\x00\x04\x00\x00\x01\x00\x00\x00\x00\x04\x91mdia\x00\x00\x00 mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\x80\x00\x02\xf2\x00\x15\xc7\x00\x00\x00\x00\x00-hdlr\x00\x00\x00\x00\x00\x00\x00\x00soun\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00SoundHandler\x00\x00\x00\x04<minf\x00\x00\x00\x10smhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$dinf\x00\x00\x00\x1cdref\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0curl \x00\x00\x00\x01\x00\x00\x04\x00stbl\x00\x00\x004stsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00$mp4a\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x10\x00\x00\x00\x00\xbb\x80\x00\x00\x00\x00\x006esds\x00\x00\x00\x00\x03\x80\x80\x80%\x00\x01\x00\x04\x80\x80\x80\x17@\x15\x00\x00\x00\x00\x02\tP\x00\x02\tP\x05\x80\x80\x80\x05\x11\x90V\xe5\x00\x06\x80\x80\x80\x01\x02\x00\x00\x00 stts\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\xbc\x00\x00\x04\x00\x00\x00\x00\x01\x00\x00\x02\x00\x00\x00\x00\x1cstsc\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\xbd\x00\x00\x00\x01\x00\x00\x03\x08stsz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbd\x00\x00\x00\x17\x00\x00\x01\xe5\x00\x00\x02\xda\x00\x00\x02\xdc\x00\x00\x02\xc6\x00\x00\x02\xe4\x00\x00\x02\xe7\x00\x00\x01\xdc\x00\x00\x01\xdf\x00\x00\x01\xb4\x00\x00\x01\x80\x00\x00\x01\x7f\x00\x00\x01\x8b\x00\x00\x01\\\x00\x00\x01k\x00\x00\x01\x85\x00\x00\x01t\x00\x00\x01p\x00\x00\x01^\x00\x00\x01e\x00\x00\x01f\x00\x00\x01j\x00\x00\x01N\x00\x00\x01c\x00\x00\x01b\x00\x00\x01S\x00\x00\x01\\\x00\x00\x01Y\x00\x00\x01W\x00\x00\x01W\x00\x00\x01<\x00\x00\x01N\x00\x00\x01@\x00\x00\x01I\x00\x00\x01g\x00\x00\x01b\x00\x00\x01]\x00\x00\x01>\x00\x00\x01^\x00\x00\x01D\x00\x00\x01a\x00\x00\x01`\x00\x00\x01c\x00\x00\x01W\x00\x00\x01T\x00\x00\x01Y\x00\x00\x01c\x00\x00\x01Z\x00\x00\x01Y\x00\x00\x01Y\x00\x00\x01U\x00\x00\x01Q\x00\x00\x01S\x00\x00\x01Y\x00\x00\x01A\x00\x00\x01F\x00\x00\x01[\x00\x00\x01{\x00\x00\x01c\x00\x00\x01_\x00\x00\x01S\x00\x00\x01f\x00\x00\x018\x00\x00\x01@\x00\x00\x01Z\x00\x00\x01e\x00\x00\x01^\x00\x00\x01W\x00\x00\x01Q\x00\x00\x01Q\x00\x00\x01V\x00\x00\x01T\x00\x00\x01W\x00\x00\x01Y\x00\x00\x01?\x00\x00\x01F\x00\x00\x01_\x00\x00\x01\\\x00\x00\x01B\x00\x00\x01c\x00\x00\x01d\x00\x00\x01>\x00\x00\x01i\x00\x00\x01\\\x00\x00\x01\\\x00\x00\x01B\x00\x00\x01J\x00\x00\x01e\x00\x00\x01@\x00\x00\x01]\x00\x00\x01]\x00\x00\x01M\x00\x00\x01^\x00\x00\x01^\x00\x00\x01X\x00\x00\x01?\x00\x00\x01e\x00\x00\x01`\x00\x00\x01Y\x00\x00\x01D\x00\x00\x01]\x00\x00\x01=\x00\x00\x01i\x00\x00\x01h\x00\x00\x01C\x00\x00\x01]\x00\x00\x01a\x00\x00\x01S\x00\x00\x01b\x00\x00\x01`\x00\x00\x01@\x00\x00\x01\\\x00\x00\x01Z\x00\x00\x01e\x00\x00\x01Z\x00\x00\x01B\x00\x00\x01<\x00\x00\x01P\x00\x00\x01e\x00\x00\x01[\x00\x00\x01f\x00\x00\x01]\x00\x00\x01X\x00\x00\x01a\x00\x00\x01T\x00\x00\x01V\x00\x00\x01<\x00\x00\x01_\x00\x00\x01`\x00\x00\x01^\x00\x00\x01\\\x00\x00\x01]\x00\x00\x01S\x00\x00\x01=\x00\x00\x01X\x00\x00\x01a\x00\x00\x01X\x00\x00\x01^\x00\x00\x01:\x00\x00\x01a\x00\x00\x01E\x00\x00\x01b\x00\x00\x01Z\x00\x00\x01^\x00\x00\x01V\x00\x00\x01?\x00\x00\x01i\x00\x00\x01[\x00\x00\x01[\x00\x00\x01V\x00\x00\x019\x00\x00\x01D\x00\x00\x01Y\x00\x00\x01f\x00\x00\x01:\x00\x00\x01j\x00\x00\x01a\x00\x00\x01^\x00\x00\x01S\x00\x00\x01]\x00\x00\x01U\x00\x00\x01c\x00\x00\x01R\x00\x00\x01U\x00\x00\x01Z\x00\x00\x01U\x00\x00\x01^\x00\x00\x01>\x00\x00\x01B\x00\x00\x01e\x00\x00\x01Z\x00\x00\x01^\x00\x00\x01B\x00\x00\x01D\x00\x00\x01l\x00\x00\x01e\x00\x00\x01\\\x00\x00\x01A\x00\x00\x01a\x00\x00\x01X\x00\x00\x01E\x00\x00\x01g\x00\x00\x01i\x00\x00\x01V\x00\x00\x01d\x00\x00\x01X\x00\x00\x019\x00\x00\x01A\x00\x00\x01H\x00\x00\x00\x14stco\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00,\x00\x00\x00\x1asgpd\x01\x00\x00\x00roll\x00\x00\x00\x02\x00\x00\x00\x01\xff\xff\x00\x00\x00\x1csbgp\x00\x00\x00\x00roll\x00\x00\x00\x01\x00\x00\x00\xbd\x00\x00\x00\x01\x00\x00\x00budta\x00\x00\x00Zmeta\x00\x00\x00\x00\x00\x00\x00!hdlr\x00\x00\x00\x00\x00\x00\x00\x00mdirappl\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00-ilst\x00\x00\x00%\xa9too\x00\x00\x00\x1ddata\x00\x00\x00\x01\x00\x00\x00\x00Lavf58.43.100'
class BoxTests(unittest.TestCase):
    ## some child boxes of the movie header box
    l_stsd1 = b'\x00\x00\x00\x98stsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x88avc1\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\xd0\x00H\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xff\xff\x00\x00\x002avcC\x01d\x00\x1f\xff\x01\x00\x1agd\x00\x1f\xac\xd9@P\x05\xbb\x01\x10\x00\x00\x03\x00\x10\x00\x00\x03\x03 \xf1\x83\x19`\x01\x00\x05h\xeb\xec\xb2,'
    l_stsd2 = b'\x00\x00\x00ustsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00eencv\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\xd0\x00H\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xff\xff\x00\x00\x00\x0favcC\x01d\x00\x1f\xff\x00\x00'
    l_pssh = b'\x00\x00\x002pssh\x00\x00\x00\x00\xed\xef\x8b\xa9y\xd6J\xce\xa3\xc8\'\xdc\xd5\x1d!\xed\x00\x00\x00\x12"\nholy_grailH\xe3\xdc\x95\x9b\x06'
    l_btrt1 = b'\x00\x00\x00\x14btrt\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xae`'
    l_mvex_1 =b'\x00\x00\x00(mvex\x00\x00\x00 trex\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    l_dinf = b'\x00\x00\x00$dinf\x00\x00\x00\x1cdref\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0curl \x00\x00\x00\x01'
    l_mvhd = b'\x00\x00\x00lmvhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'
    l_vmhd = b'\x00\x00\x00\x14vmhd\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
    l_tkhd = b'\x00\x00\x00\\tkhd\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x05\x00\x00\x00\x02\xd0\x00\x00'
    l_mdhd = b'\x00\x00\x00 mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01_\x90\x00\x00\x00\x00U\xc4\x00\x00'
    l_hdlr = b'\x00\x00\x002hdlr\x00\x00\x00\x00\x00\x00\x00\x00vide\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00USP Video Handler\x00'
    l_tenc = b'\x00\x00\x00 tenc\x00\x00\x00\x00\x00\x00\x01\x08N-P\x9au?^&\xb2S\xcb}!\xc3\xbf\x05'
    
    ## some child boxes of event message track
    l_stsd_emsg1 = b'\x00\x00\x00Estsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005urim\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00%uri \x00\x00\x00\x00urn:mpeg:dash:event:2012\x00'
    l_mvex_emsg1 = b'\x00\x00\x00(mvex\x00\x00\x00 trex\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00'
    l_mvhd_emsg1 = b'\x00\x00\x00lmvhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'
    l_mdhd_emsg1 = b'\x00\x00\x00 mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x00\x00U\xc4\x00\x00'
    l_hdlr_emsg1 = b'\x00\x00\x001hdlr\x00\x00\x00\x00\x00\x00\x00\x00meta\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00USP Meta Handler\x00'
   
    l_ststd_emsg2 = b'\x00\x00\x00Estsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005urim\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00%uri \x00\x00\x00\x00urn:mpeg:dash:event:2012\x00'
    l_mvex_emsg2 = b'\x00\x00\x008mvex\x00\x00\x00\x10mehd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 trex\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    l_dinf_emsg = b'\x00\x00\x00$dinf\x00\x00\x00\x1cdref\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0curl \x00\x00\x00\x01'
    l_mvhd_emsg2 = b'\x00\x00\x00lmvhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0fB@\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff'
    l_mdhd_emsg2 =  b'\x00\x00\x00 mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0fB@\x00\x00\x00\x00\x14\xa0\x00\x00'
    l_hdlr_emsg2 = b'\x00\x00\x008hdlr\x00\x00\x00\x00\x00\x00\x00\x00meta\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Bento4 metadata Handler\x00'

    ## some child boxes in the movie fragment box
    l_prft_emsg = b'\x00\x00\x00 prft\x01\x00\x00\x18\x00\x00\x00\x01\x83\xaa~\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    l_tfdt_emsg = '\x00\x00\x00\x14tfdt\x01\x00\x00\x00\x00\x00\x83\xdf\xa3H\x9ap'
    l_trun_emsg =  b'\x00\x00\x00\x1ctrun\x00\x00\x03\x01\x00\x00\x00\x01\x00\x00\x00p\x00\x00d\x00\x00\x00\x00\x08'
    l_mfhd_emsg =  b'\x00\x00\x00\x10mfhd\x00\x00\x00\x00\x00\x00\x00\x01'
    l_tfhd_emsg = b'\x00\x00\x00 tfhd\x00\x02\x00:\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x05\xdd\x00\x00\x00\x08\x01\x01\x00\x00'
    l_prft2_emsg = b'\x00\x00\x00 prft\x01\x00\x00\x18\x00\x00\x00\x01\x83\xaa~\x82\x04\x9c^o\x00\x00\x00\x00\x00\x02\xc5u'
    l_tfdt2_emsg =  b'\x00\x00\x00\x14tfdt\x01\x00\x00\x00\x00\x00\x83\xdf\xa3K_\xe5'
    l_trun2_emsg = b'\x00\x00\x00\x1ctrun\x00\x00\x03\x01\x00\x00\x00\x01\x00\x00\x00p\x00\x03\x90\x00\x00\x00\x00Z'
    l_mfhd2_emsg = b'\x00\x00\x00\x10mfhd\x00\x00\x00\x00\x00\x00\x00\x02'
    
    ## some event message boxes 
    l_emsg1 =b'\x00\x00\x00Zemsg\x00\x00\x00\x00urn:scte:scte35:2013:bin\x00\x00\x00\x002\x00\x00\x00\x00\x00\x00\x03\x90\x00\x00\x00\x03+\xfc0!\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x10\x05\x00\x00\x03+\x7f\xef\x7f\xfe\x00\x1a\x17\xb0\xc0\x00\x00\x00\x00\x00\xe4a$\x02'
    l_emsg2 =b'\x00\x00\x00Zemsg\x00\x00\x00\x00urn:scte:scte35:2013:bin\x00\x00\x00\x002\x00\x00\x00\x00\x00\x00\x03\x90\x00\x00\x00\x03,\xfc0!\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x10\x05\x00\x00\x03,\x7f\xef\x7f\xfe\x00\x1a\x17\xb0\xc0\x00\x00\x00\x00\x00\xfe\xcc\xb92'
    l_embe = b'\x00\x00\x00\x08embe'
    l_emeb = b'\x00\x00\x00\x08emeb'
    
    def test_ftyp_parse(self):
        self.assertEqual(
            Box.parse(b'\x00\x00\x00\x18ftypiso5\x00\x00\x00\x01iso5avc1'),
            Container(offset=0)
            (type=b"ftyp")
            (major_brand=b"iso5")
            (minor_version=1)
            (compatible_brands=[b"iso5", b"avc1"])
            (end=24)
        )

    def test_ftyp_build(self):
        self.assertEqual(
            Box.build(dict(
                type=b"ftyp",
                major_brand=b"iso5",
                minor_version=1,
                compatible_brands=[b"iso5", b"avc1"])),
            b'\x00\x00\x00\x18ftypiso5\x00\x00\x00\x01iso5avc1')

    def test_mdhd_parse(self):
        self.assertEqual(
            Box.parse(
                b'\x00\x00\x00\x20mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0fB@\x00\x00\x00\x00U\xc4\x00\x00'),
            Container(offset=0)
            (type=b"mdhd")(version=0)(flags=0)
            (creation_time=0)
            (modification_time=0)
            (timescale=1000000)
            (duration=0)
            (language="und")
            (end=32)
        )

    def test_mdhd_build(self):
        mdhd_data = Box.build(dict(
            type=b"mdhd",
            creation_time=0,
            modification_time=0,
            timescale=1000000,
            duration=0,
            language=u"und"))
        self.assertEqual(len(mdhd_data), 32)
        self.assertEqual(mdhd_data,
                         b'\x00\x00\x00\x20mdhd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0fB@\x00\x00\x00\x00U\xc4\x00\x00')

        mdhd_data64 = Box.build(dict(
            type=b"mdhd",
            version=1,
            creation_time=0,
            modification_time=0,
            timescale=1000000,
            duration=0,
            language=u"und"))
        self.assertEqual(len(mdhd_data64), 44)
        self.assertEqual(mdhd_data64,
                         b'\x00\x00\x00,mdhd\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0fB@\x00\x00\x00\x00\x00\x00\x00\x00U\xc4\x00\x00')

    def test_moov_build(self):
        moov = \
            Container(type=b"moov")(children=[  # 96 bytes
                Container(type=b"mvex")(children=[  # 88 bytes
                    Container(type=b"mehd")(version=0)(flags=0)(fragment_duration=0),  # 16 bytes
                    Container(type=b"trex")(track_ID=1),  # 32 bytes
                    Container(type=b"trex")(track_ID=2),  # 32 bytes
                ])
            ])

        moov_data = Box.build(moov)

        self.assertEqual(len(moov_data), 96)
        self.assertEqual(
            moov_data,
            b'\x00\x00\x00\x60moov'
            b'\x00\x00\x00\x58mvex'
            b'\x00\x00\x00\x10mehd\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x20trex\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x20trex\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        )

    def test_smhd_parse(self):
        in_bytes = b'\x00\x00\x00\x10smhd\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(
            Box.parse(in_bytes + b'padding'),
            Container(offset=0)
            (type=b"smhd")(version=0)(flags=0)
            (balance=0)(reserved=0)(end=len(in_bytes))
        )

    def test_smhd_build(self):
        smhd_data = Box.build(dict(
            type=b"smhd",
            balance=0))
        self.assertEqual(len(smhd_data), 16),
        self.assertEqual(smhd_data, b'\x00\x00\x00\x10smhd\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_stsd_parse(self):
        tx3g_data = b'\x00\x00\x00\x00\x01\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x12\xFF\xFF\xFF\xFF\x00\x00\x00\x12ftab\x00\x01\x00\x01\x05Serif'
        in_bytes = b'\x00\x00\x00\x50stsd\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x40tx3g\x00\x00\x00\x00\x00\x00\x00\x01' + tx3g_data
        self.assertEqual(
            Box.parse(in_bytes + b'padding'),
            Container(offset=0)
            (type=b"stsd")(version=0)(flags=0)
            (entries=[Container(format=b'tx3g')(data_reference_index=1)(data=tx3g_data)])
            (end=len(in_bytes))
        )
    
    def test_parse_trun(self):
        trun_box1 = Box.parse(self.l_trun_emsg) 
        self.assertEqual(trun_box1["type"],b'trun')
        self.assertEqual(trun_box1["version"],0)
        self.assertEqual(trun_box1["flags"]["sample_composition_time_offsets_present"], False)
        self.assertEqual(trun_box1["flags"]["sample_flags_present"], False)
        self.assertEqual(trun_box1["flags"]["sample_size_present"], True)
        self.assertEqual(trun_box1["flags"]["sample_duration_present"], True)
        self.assertEqual(trun_box1["flags"]["first_sample_flags_present"], False)
        self.assertEqual(trun_box1["flags"]["data_offset_present"], True)
        self.assertEqual(trun_box1["sample_count"],1)
        self.assertEqual(trun_box1["data_offset"],112)
        self.assertEqual(len(trun_box1["sample_info"]),1)
        self.assertEqual(trun_box1["sample_info"][0]["sample_duration"], 25600)
        self.assertEqual(trun_box1["sample_info"][0]["sample_size"], 8)
        
        trun_box2 = Box.parse(self.l_trun2_emsg)
        self.assertEqual(trun_box2["type"],b'trun')
        self.assertEqual(trun_box2["version"],0)
        self.assertEqual(trun_box2["flags"]["sample_composition_time_offsets_present"], False)
        self.assertEqual(trun_box2["flags"]["sample_flags_present"], False)
        self.assertEqual(trun_box2["flags"]["sample_size_present"], True)
        self.assertEqual(trun_box2["flags"]["sample_duration_present"], True)
        self.assertEqual(trun_box2["flags"]["first_sample_flags_present"], False)
        self.assertEqual(trun_box2["flags"]["data_offset_present"], True)
        self.assertEqual(trun_box2["sample_count"],1)
        self.assertEqual(trun_box2["data_offset"],112)
        self.assertEqual(len(trun_box2["sample_info"]),1)
        self.assertEqual(trun_box2["sample_info"][0]["sample_duration"], 233472)
        self.assertEqual(trun_box2["sample_info"][0]["sample_size"], 90)


    def test_parse_stbl_progressive(self):
        stbl = Box.parse(l_stbl_audio_4s) 
        self.assertNotEqual(stbl, None)
        stsd = BoxUtil.find_and_return_first(stbl,b'stsd')
        self.assertEqual(len(stsd["entries"]), 1) 
        self.assertEqual(stsd["entries"][0]["format"], b"mp4a")
        mp4a = stsd["entries"][0] 
        self.assertEqual(mp4a["channels"], 2) 
        self.assertEqual(mp4a["sampling_rate"], 48000) 
        stsz = BoxUtil.find_and_return_first(stbl,b'stsz')
        self.assertNotEqual(stsz, None)
        self.assertEqual(stsz["sample_count"],189)
        stco = BoxUtil.find_and_return_first(stbl,b'stco')
        self.assertNotEqual(stco, None)
        self.assertEqual(len(stco["entries"]),1)
        stts = BoxUtil.find_and_return_first(stbl,b'stts')
        self.assertNotEqual(stts, None)
        self.assertEqual(len(stts["entries"]),2)

    def test_parse_emsg(self):
        emsg1 = Box.parse(self.l_emsg1) 
        self.assertEqual(emsg1["type"],b'emsg')
        self.assertEqual(emsg1["version"],0)
        self.assertEqual(emsg1["id"],811)
        self.assertEqual(emsg1["event_duration"],233472)
        self.assertEqual(emsg1["scheme_id_uri"], b'urn:scte:scte35:2013:bin')
        self.assertEqual(emsg1["message_data"], b'\xfc0!\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x10\x05\x00\x00\x03+\x7f\xef\x7f\xfe\x00\x1a\x17\xb0\xc0\x00\x00\x00\x00\x00\xe4a$\x02')

        emsg2 = Box.parse(self.l_emsg2) 
        self.assertEqual(emsg2["type"],b'emsg')
        self.assertEqual(emsg2["version"],0)
        self.assertEqual(emsg2["id"],812)
        self.assertEqual(emsg2["event_duration"],233472)
        self.assertEqual(emsg2["scheme_id_uri"], b'urn:scte:scte35:2013:bin')
        self.assertEqual(emsg2["message_data"],b'\xfc0!\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x10\x05\x00\x00\x03,\x7f\xef\x7f\xfe\x00\x1a\x17\xb0\xc0\x00\x00\x00\x00\x00\xfe\xcc\xb92')
        
        embe1 = Box.parse(self.l_embe)
        self.assertEqual(embe1["type"], b'embe')

    def test_build_emsg(self):
        emsg_b = Box.build(dict(
            type=b"emsg",
            version=1,
            presentation_time=1000,
            value=b'',
            id=1,
            scheme_id_uri=b"my_test_scheme",
            event_duration=20,
            timescale=1,
            message_data=b"asdfdasgfaghhgsdgh"))

        emsg_b_p = Box.parse(emsg_b)
        self.assertEqual(emsg_b_p["type"], b'emsg')
        self.assertEqual(emsg_b_p["version"], 1)
        self.assertEqual(emsg_b_p["presentation_time"], 1000)
        self.assertEqual(emsg_b_p["value"],b'' )
        self.assertEqual(emsg_b_p["id"], 1)
        self.assertEqual(emsg_b_p["scheme_id_uri"], b"my_test_scheme")
        self.assertEqual(emsg_b_p["event_duration"], 20)
        self.assertEqual(emsg_b_p["timescale"], 1)
        self.assertEqual(emsg_b_p["message_data"],b"asdfdasgfaghhgsdgh")

    def test_build_emib(self):
        emib_b = Box.build(dict(
            type=b"emib",
            version=0,
            reserved=1,
            presentation_time_delta=-1000,
            value=b'',
            id=1,
            scheme_id_uri=b"my_test_scheme",
            duration=2000,
            message_data=b"asdfdasgfaghhgsdgh"))

        emib_b_p = Box.parse(emib_b)
        self.assertEqual(emib_b_p["type"], b'emib')
        self.assertEqual(emib_b_p["presentation_time_delta"], -1000)
        self.assertEqual(emib_b_p["value"],b'' )
        self.assertEqual(emib_b_p["id"], 1)
        self.assertEqual(emib_b_p["scheme_id_uri"], b"my_test_scheme")
        self.assertEqual(emib_b_p["duration"], 2000)
        self.assertEqual(emib_b_p["reserved"], 1)
        self.assertEqual(emib_b_p["message_data"],b"asdfdasgfaghhgsdgh")

    def test_build_evte(self):
        evte = Box.build(dict(type=b"evte", children=[]))

    #TODO there is still something nasty when parsing uri box the type is set to b'uri' instead of b'uri ', i did a workaround for this by having two aliases uri and uri '
    def test_parse_stsd_urim(self):    
        urim_sample_entry = Box.parse(self.l_stsd_emsg1)
        self.assertEqual( len(urim_sample_entry["entries"]),1)
        for entry in urim_sample_entry["entries"]: 
            self.assertEqual(entry["format"],b"urim") 
            for l_child in entry["children"]:
                if l_child["type"] != b"uriI":
                    self.assertEqual(l_child["type"][0:3], b'uri')
                    self.assertEqual(l_child["theURI"], b"urn:mpeg:dash:event:2012")
    

    def test_parse_edit_list(self):
        elst_b = Box.parse( b'\x00\x00\x00\x1celst\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x0f\xa0\x00\x00\x04\x00\x00\x01\x00\x00')
        [Container(edit_duration=4000)(media_time=1024)]                  
        self.assertEqual(elst_b["type"], b"elst")
        self.assertEqual(len(elst_b["entries"]), 1)
        self.assertEqual(elst_b["entries"][0]["edit_duration"], 4000)
        self.assertEqual(elst_b["entries"][0]["media_time"], 1024)
        self.assertEqual(elst_b["entries"][0]["media_rate_integer"], 1)
        self.assertEqual(elst_b["entries"][0]["media_rate_fraction"], 0)

        t = dict(
             type=b"elst",
             version=1,
             flags=0,
             entries=[dict(edit_duration=1,media_time=1, media_rate_integer=1, media_rate_fraction=1)\
                 ,dict(edit_duration=2,media_time=2, media_rate_integer=1,
             media_rate_fraction=1)  ],
             
            )
        elst_b = Box.build(t)
        t2 = Box.parse(elst_b)
        self.assertEqual(len(t["entries"]), len(t2["entries"]))
        #self.assertEqual(t["media_rate_integer"], t2["media_rate_integer"] )

class SampleTests(unittest.TestCase):

    def test_parse_stbl_parse_samples_progressive(self):

        moov_a = Box.parse(l_movie_box_audio)
        res = BoxUtil.find_samples_progressive(moov_a , moov_a)

        self.assertEqual(len(res), 189)
        #self.assertEqual(res[0], {'decode_time': 1024, 'size': 23, 'chunk': 1, 'chunk_offset': 44, 'offset': 44})
        #self.assertEqual(res[1], {'decode_time': 2048, 'size': 485, 'chunk': 1, 'chunk_offset': 44, 'offset': 67})
        #self.assertEqual(res[2], {'decode_time': 3072, 'size': 730, 'chunk': 1, 'chunk_offset': 44, 'offset': 552})
        #self.assertEqual(res[3], {'decode_time': 4096, 'size': 732, 'chunk': 1, 'chunk_offset': 44, 'offset': 1282})   
        #self.assertEqual(res[-1],{'decode_time': 193024, 'size': 328, 'chunk': 1, 'chunk_offset': 44, 'offset': 66800})      