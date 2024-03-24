import pytest
from lab03 import multiply, collectMultiples, countVowels, reverseVowels, removeSubString
def test_multiply():
    assert multiply(5,4) == 20

def test_collectMultiples():
    assert collectMultiples([1,3,5,7,9], 3) == [3,9]

def test_countVowels(s):
    assert countVowels("This Is A String") == 4

def test_reverseVowels(s):
    assert reverseVowels("Eunoia") == "aiouE"

def test_removeSubString(s, sub):
    assert removeSubString("Lolololol", "lol") == "Loo"
