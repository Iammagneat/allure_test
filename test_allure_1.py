# import allure
import pytest


def test_success():
    """this 1 ok"""
    assert 1


# def test_fail():
#     """this 1 bad"""
#     assert 0
#
#
# def test_skip():
#     """skip dat"""
#     pytest.skip('sorry')


# def test_broken():
#     raise Exception('oops')


# @allure.title("Passing Test")
# def test_pass():
#     with allure.step("Step 1"):
#         pass
#
# @allure.title("Failing Test")
# def test_fail():
#     with allure.step("Step 1"):
#         assert 1 == 2


# @allure.title("Hello, World!")
# @pytest.mark.parametrize("name", ["Alice", "Bob"])
# def test_hello_world(name):
#     with allure.step("Greet the user"):
#         greeting = f"Hello, {name}!"
#         allure.attach(greeting, name="Greeting", attachment_type=allure.attachment_type.TEXT)
#         assert greeting == "Hello, Alice!"
