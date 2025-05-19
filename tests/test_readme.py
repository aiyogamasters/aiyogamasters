import os

def test_readme_and_license_exist():
    assert os.path.isfile('README.md'), 'README.md file is missing.'
    assert os.path.isfile('LICENSE'), 'LICENSE file is missing.'
