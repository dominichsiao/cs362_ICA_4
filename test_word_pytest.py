import pytest
import word_count

#class TestPal:
def test_count_sentence():
	assert word_count.count ("I was wondering after all these years if you'd like to meet") == 12

def test_count_single_letter_word():
	assert word_count.count ("A") == 1

def test_count_not_a_word():
	assert word_count.count ("_") == 0

def test_count_comma_no_space():
	assert word_count.count ("General,Kenobi") == 2