


import pytest

@pytest.fixture()

def fixt_01():

    print('fixture_01')

    yield

    print('fixture 01 finished')


@pytest.fixture()

def fixt_02():

    print('fixture_02')

    yield

    print('fixture_02 finished')