# @Author: drxos
# @Date:   2016-08-15T13:04:57+01:00
# @Email:  drxost@gmail.com
# @Project: zbraaku
# @Last modified by:   drxos
# @Last modified time: 2016-08-15T13:06:10+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



import random
import string


def gen_secret_key():
    key = ''
    for i in range(100):
        key += random.SystemRandom().choice(string.digits + string.letters + string.punctuation)
    return key
