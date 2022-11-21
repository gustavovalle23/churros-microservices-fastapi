# -*- coding: utf-8 -*-
import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def email_is_valid(email: str) -> bool:
    return bool(re.search(regex, email))
