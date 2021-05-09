# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import json


class ServerAPI:
    def __init__(self):
        with open('API/ReportCredential.json', 'r') as JsonParsing:
            self.ReportCredential = json.load(JsonParsing)

        with open('API/ServerLog.json', 'r') as JsonParsing:
            self.ServerLog = json.load(JsonParsing)

        with open('API/Command.json', 'r') as JsonParsing:
            self.Command = json.load(JsonParsing)

    def MailReportCredential(self):
        """
        :return: json
        """
        return {
            "sender": self.ReportCredential["send"]["E-mail-Address"],
            "sender-password": self.ReportCredential["send"]["E-mail-Password"],
            "receive": self.ReportCredential["receive"]
        }

    def ServerLogPath(self, LogType=None, ServerType=None, LogName=None):
        """
        :type LogType: str
        :type ServerType: str
        :type LogName: str
        :return: json
        """
        if LogType is None or ServerType is None or LogName is None:
            return {
                "LogType": None,
                "ServerType": None,
                "LogName": None,
                "LogPath": None
            }

        return {
            "LogType": LogType,
            "ServerType": ServerType,
            "LogName": LogName,
            "LogPath": self.ServerLog[ServerType][LogType][LogName]
        }

    def ExecuteCommand(self, CMDType=None, UsedType=None, CMDName=None):
        """
        :type CMDType: str
        :type UsedType: str
        :type CMDName: str
        :return: json
        """
        if CMDType is None or UsedType is None or CMDName is None:
            return {
                    "CMDType": None,
                    "UsedType": None,
                    "CMDName": None,
                    "Command": None
            }

        return {
            "CMDType": CMDType,
            "UsedType": UsedType,
            "CMDName": CMDName,
            "Command": self.Command[CMDType][UsedType][CMDName]
        }


