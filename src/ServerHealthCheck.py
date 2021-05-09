# ! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

"""
    This script checks the health of the docker server and sends it to the administrator.

    How to use...
        1. Define administrator mail. - ContactMailAddress.json (path : /root/Contact/ContactMailAddress.json)
        2. Define this script in the crontab scheduler. - crontab (path : /etc/crontab or cmd : crontab -e)
        3.
        4.
        5.
"""

from datetime import datetime
import os



