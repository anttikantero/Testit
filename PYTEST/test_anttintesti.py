### Yksinkertainen pytest harjoitus ###

import pytest
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"Testi epäonnistui"
def test_file1_method2():
	x=5
	y=20
	assert x*y == 100,"Testi epäonnistui" 