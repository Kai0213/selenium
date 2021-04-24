# selenium
For autotest

Prepare environment

asdf lives in https://github.com/asdf-vm/asdf

Follow its installation instructions at https://asdf-vm.com/#/core-manage-asdf?id=install

On a new terminal, install Python plugin:
$ asdf plugin-add python
Then install Python 3.9.4:
$ asdf install python 3.9.4
Set system version
$ asdf global python 3.9.4

Check the result
$ python --version
Python 3.9.4

Prepare SeleniumBase
Create a folder
$ mkdir sbase
Using venv
$ python -m venv sbase_env
$ source sbase_env/bin/activate
You may need upgrade pip
$ python -m pip install --upgrade pip
Check pip version
$ pip --version
pip 21.0.1 from /Users/kao/dev/pentium/sbase/sbase_env/lib/python3.9/site-packages/pip (python 3.9)

Install SeleniumBase
$ pip install seleniumbase
Check it works successfully
$ sbase

Download a webdriver
SeleniumBase can download webdrivers to the seleniumbase/drivers folder with the install command:
sbase install chromedriver

Let’s do something
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basics(self):
        url = "https://store.xkcd.com/collections/posters"
        self.open(url)
        self.type('input[name="q"]', "xkcd book")
        self.click('input[value="Search"]')
        self.assert_text("xkcd: volume 0", "h3")
        self.open("https://xkcd.com/353/")
        self.assert_title("xkcd: Python")
        self.assert_element('img[alt="Python"]')
        self.click('a[rel="license"]')
        self.assert_text("free to copy and reuse")
        self.go_back()
        self.click_link("About")
        self.assert_exact_text("xkcd.com", "h2")
        
        
 Run it by
 $ pytest my_first_test.py
 or
 $ pytest my_first_test.py --demo
