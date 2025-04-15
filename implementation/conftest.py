import pytest

@pytest.fixture(scope='function', autouse=True)
def hook(request):
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("before suite")
    yield
    print("after suite")

