from uni_extract import extract_groups, extract_unique_group_strings

def test_extract(pages = ['tests/hieropage.html']):
    groups = extract_unique_group_strings(pages)
    print(groups)

    groups = extract_groups(pages)
    print(groups)

if __name__ == '__main__':
    test_extract()
