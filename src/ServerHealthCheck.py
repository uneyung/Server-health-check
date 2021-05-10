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

import time
from Report import SendServerStatusforDiscord

if __name__ == '__main__':
    DateTime = time.localtime()
    DiscordReport = SendServerStatusforDiscord(
        WebHook_URL="840869197374291968/avpWEpIJNXhYO9XfIHw0-KzD7DCD_bkV3ALW2AjW1DxxE7fO5p5jVnoFGc7Yib51Ad3q",
        Response="",
        Report_Title="",
        Date=str(DateTime.tm_year) + "-" + str(DateTime.tm_mon) + "-" + str(DateTime.tm_mday) + " " + str(DateTime.tm_hour) + ":" + str(DateTime.tm_min) + ":" + str(DateTime.tm_sec),
        Report_Message="server die",
        ServerStatusCode="",
        Error_Point="",
        Error_Log=""
    )

    DiscordReport.SendDiscordMessage()