# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import smtplib
import datetime
from email.mime.text import MIMEText
from API_Return import *
from discord_webhook import DiscordWebhook


class SendServerStatusforDiscord:

    """
        Report for Server Status

        Discord Bot Token: "ODM4MTMxMDQzOTE0NjEyNzM2.YI2oXA.gw_lh5ia5ZBoKa8Lm3goRZmeznY"
        Web Hook URL: "https://discord.com/api/webhooks/838673129533866004/6g2A5rW6xI5rKycJxfx4YvINs9F4PEl7D4-2qiWit63t84237MZnHAIfAxE7vpWKU50m"
    """

    def __init__(self, WebHook_URL, **kwargs):
        """
        Init Report for Server Status
        :param WebHook_URL: LOGOS discord channel web-hook url
        :type WebHook_URL: str
        :keyword Response: Server response message
        :keyword Report_Title: Server health check report title
        :keyword Date: Server health check report time
        :keyword Report_Message: report message
        :keyword ServerStatusCode: server status code
        :keyword Error_Point: error point
        :keyword Error_Log: error log
        """

        self.webhook_url = "https://discord.com/api/webhooks/" + WebHook_URL
        self.Response = kwargs.get("Response")
        self.Report_Title = kwargs.get("Report_Title")
        self.Date = kwargs.get("Date")
        self.Report_Message = kwargs.get("Report_Message")
        self.ServerStatusCode = kwargs.get("ServerStatusCode")
        self.Error_Point = kwargs.get("Error_Point")
        self.Error_Log = kwargs.get("Error_Log")

        """
        from discord_webhook import DiscordWebhook

        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/838953823451480134/xPbLNRqT-Rg4k_H7a3kQJUQsRHx8X8yvh3Hl3-auxDIJLScML-GdKhI9ncsHiUxiNsvG', content='Webhook Message')
        response = webhook.execute()
        """
        self.webhook = DiscordWebhook(
            url=self.webhook_url,
            context=self.Report_Message
        )

    def SendDiscordMessage(self):
        return self.webhook.execute()


class SendServerStatusforMail:
    def __init__(
            self, ServerName="",
            Title="LOGOS Server Health",
            Date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            Message=None,
            Status=None
    ):
        self.ServerName = ServerName
        self.Title = Title
        self.Message = Message
        self.Status = Status
        self.date = Date

        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.msg = MIMEText(self.Message)

        self.sender = list()
        self.receive = None

    def SendMailCredential(self):
        self.sender = (ServerAPI.MailReportCredential(True, False))
        return self.sender

    def ReceiveMailCredential(self):
        self.receive = (ServerAPI.MailReportCredential(False, True))
        return self.receive

    def SendMail(self):
        self.smtp.ehlo()  # say Hello
        self.smtp.starttls()  # TLS 사용시 필요
        self.smtp.login(self.SendMailCredential()[0], self.SendMailCredential()[1])

        self.msg['Subject'] = self.Title
        self.msg['To'] = self.ReceiveMailCredential()

        self.smtp.sendmail(self.SendMailCredential()[0], self.ReceiveMailCredential(), self.msg.as_string())
        self.smtp.quit()
