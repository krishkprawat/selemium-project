# we have a common requirement for all test cases so i made this file glovally .
import pytest


@pytest.fixture()
def test_global():
    print("iam global first from fixture")
    yield
    print("i am secind from gloval fixture")


@pytest.fixture(params=[("krishna","goes","to"),("rawat","ji"),("devops","qa")])
def crossBrowser(request):
    return request.param
