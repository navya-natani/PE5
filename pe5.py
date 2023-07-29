import pprint

n=12
multi_table = [ [i*j if i*j > 0 else max(i,j) if i != j else 'X' for i in range(0,13)] for j in range(0,13)]
pprint.pprint(multi_table)

def test_1():
    print (multi_table)
    assert multi_table[10][10]==100

