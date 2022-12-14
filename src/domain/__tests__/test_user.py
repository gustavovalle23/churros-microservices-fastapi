# -*- coding: utf-8 -*-
import pytest

from src.domain.user.entities import User


def test_should_raise_error_when_email_is_empty():
    with pytest.raises(ValueError) as err1:
        User("123", "Test", "", "password", True)

    assert err1.value.args[0] == ['email: Should be a valid e-mail!']


def test_should_raise_error_when_email_is_an_invalid_format():
    with pytest.raises(ValueError) as err:
        User("123", "Test", "invalid_email@", "password", True)
    assert err.value.args[0] == ['email: Should be a valid e-mail!']
