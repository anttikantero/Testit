### Yksinkertainen pytest harjoitus ###

import pytest
def test_file1_method1():
	x=100
	y=101
	assert x+1 == y,"Testi epäonnistui"
def test_file1_method2():
	x=10
	y=10
	assert x*y == 100,"Testi epäonnistui" 