from server import pig_latin, zip_code_pop

def test_create_phrase(app,client):
    res = client.get('/create_phrase')
    assert res.status_code == 200
    
def test_pig_latin():
    inp = 'Rohit Chouhan'
    expected = 'Ohitray Ouhanchay'
    assert pig_latin(inp) == expected

def test_pig_latin_numerical_input():
    inp = 'R0h1t 6h0uhan'
    assert pig_latin(inp) == inp

def test_zip_code_pop():
    inp = '02115'
    expected = ['Suffolk', 28652]
    c,p = zip_code_pop(inp)
    assert c==expected[0] and p==expected[1]
