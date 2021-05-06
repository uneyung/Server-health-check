# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import json


class ServerAPI:
    def __init__(self):
        with open('API/ReportCredential.json', 'r') as JsonParsing:
            self.ReportCredential = json.load(JsonParsing)

        with open('API/ServerLog-Information.json', 'r') as JsonParsing:
            self.ServerLog = json.load(JsonParsing)

        with open('API/Command.json', 'r') as JsonParsing:
            self.Command = json.load(JsonParsing)

    def MailReportCredential(self, send=None, receive=None):
        """

        :param send: BOOL
        :param receive: BOOL
        :return: json(String)
        """
        if send is None or receive is None:
            return {"sender": None, "receive": None}

        if send is True:
            return {
                "sender": self.ReportCredential["send"]["E-mail-Address"],
                "sender-password": self.ReportCredential["send"]["E-mail-Password"]
                    }
        elif receive is True:
            return {
                "sender": None,
                "receive": self.ReportCredential["receive"]
            }
        else:
            return {"sender": None, "receive": None}

    def ServerLogPath(self, ServerType=None, LogType=None, LogName=None):
        """

        :param ServerType: String
        :param LogType: String
        :param LogName: String
        :return: json(String)
        """
        if ServerType is None or LogType is None or LogName is None:
            return {
                "LogServerType": None,
                "LogType": None,
                "LogName": None,
                "LogPath": None
                }
        return {
            "LogServerType": ServerType,
            "LogType": LogType,
            "LogName": LogName,
            "LogPath": self.ServerLog[ServerType][LogType][LogName]
        }

    def ExecuteCommand(self, CMDType=None, UsedType=None, CMDName=None):
        """

        :param CMDType: String
        :param UsedType: String
        :param CMDName: String
        :return: json(String)
        """
        if CMDType is None or UsedType is None or CMDName is None:
            return None

        if CMDType is "MemoryUsed" or CMDType is "StorageUsed":
            CMDName = CMDType
            return {
                "CMDType": CMDType,
                "UsedType": None,
                "CMDName": CMDName,
                "Command": self.Command[CMDType]
            }
        else:
            if UsedType is "network-interface" or \
                    UsedType is "docker-network" or \
                    UsedType is "docker-container":
                return {
                    "CMDType": CMDType,
                    "UsedType": UsedType,
                    "CMDName": CMDName,
                    "Command": self.Command[CMDType][UsedType][CMDName]
                }
