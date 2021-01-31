import os

from gendiff.scripts.gendiff import generate_diff


DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def test_plain_json():
    diff = generate_diff(DIR_PATH + '/fixtures/file1.json', DIR_PATH + '/fixtures/file2.json')
    assert diff == '{\n    + follow: False\n    host: hexlet.io\n    - proxy: 123.234.53.22\n    - timeout: 50\n ' \
                   '   + timeout: 20\n    + verbose: None\n}'
