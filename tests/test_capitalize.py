from capitalize import capitalize

def test_capitalize(capitalize):
    assert capitalize('hello') == 'Hello'
    assert capitalize('') == ''


if __name__ == '__main__':
    test_capitalize(capitalize)
