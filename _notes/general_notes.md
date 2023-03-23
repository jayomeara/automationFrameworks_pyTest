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
- regression suite, smoke suite, integration suite
- Tox

**DO NOT MANUALLY MAINTAIN TEST SUITES**
    Organize tests in directories
    Split them out
    Don't comment out tests

--
**Markers:**

from pytest import mark

@mark.engine
def...

ADD TO pytest.ini:
markers = engine: mark a test as engine

--

**FIXTURES**
Don't need to be imported - pytest does it automatically

**Skips and Failures**
    @mark.skip(reason="test")
    mark skip and give reason
run pytest arguments = -rs

    @mark.xfail

**Parameterize**
- multiple parameters per test
- fixtures

**PYTEST-XDIST**
– run tests at the same time
- multiple threads and tests at same time
- n option for number of threads (use -nauto)
- via LoadScheduling
- must write tests isolated - new user per test for example - allows parallelization - allows better bug tracking

**Concurrent vs Parallel**
- global interpreter lock
- threads vs process (i/o bound vs cpu bound)
- where is the slow down? external or logical(cpu?)
- xdist uses processes and threads

**Tox**
- creates virtual environment automatically to run tests
- maintains separate testing structure from the unit logic

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



 