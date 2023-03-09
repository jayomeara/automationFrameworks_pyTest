Python Testing Frameworks:
- unittest (basic but useful)
- nose (extends functionality of unittest)
- behave (uses gerkin language)
- robot framework
- pytest (compatible with unittest)

**PyTest Benefits:**
- test search
- concurrency
- code re-use
- plugins

Questions:
- regression suit, smoke suite, integration suite

**DO NOT MANUALLY MAINTAIN TEST SUITES**
    Organize tests in directories
    Split them out
    Don't comment out tests

--
Markers:

from pytest import mark

@mark.engine
def...

ADD TO pytest.ini:
markers = engine: mark a test as engine

--

**FIXTURES**
Don't need to be imported - pytest does it automaticly


**Virtual Environment:**

jayomeara@jHack_01 bin % python3.10 -m venv ~/venvs/frameworkenv

cd /Users/jayomeara/_code/automationFrameworks_pyTest/bin
source activate

deactivate

============================= test session starts ==============================
platform darwin -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/jayomeara/_code/automationFrameworks_pyTest/bin
collected 1 item                                                               

test_widget.py .                                                         [100%]

============================== 1 passed in 0.01s ===============================

test_ = tells pytest this is a test

config file ->
touch pytest.ini

content ->

[pytest]
python_files = test_*
python_classes = *Tests
python_functions = test_*



 