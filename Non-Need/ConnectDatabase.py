# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon

import pymysql
import sys
import sqlite3


class ConnectDatabase:
    def __init__(self):
        self.EncodingCheck = sys.stdin.encoding

        self.HostServerHealth_DBConnect = sqlite3.connect('HostServerHealth.db')
        self.DockerServerHealth_DBConnect = sqlite3.connect('DockerServerHealth.db')

        self.HostServerHealth_cursor = self.HostServerHealth_DBConnect.cursor()
        self.DockerServerHealth_cursor = self.DockerServerHealth_DBConnect.cursor()

        self.DBData = dict(TableName=["Server", "Health", "Data"], Columns=["world"])
        self.ColumnsCount = self.DBData.get('Columns')

        self.Insert = """INSERT INTO %s (%s) VALUES (%s)"""
        self.Select = """INSERT INTO %s (%s) VALUES (%s)"""
        self.Update = """INSERT INTO %s (%s) VALUES (%s)"""
        self.Delete = """INSERT INTO %s (%s) VALUES (%s)"""

        self.HostServerHealth_execute = self.HostServerHealth_cursor.execute()
        self.DockerServerHealth_execute = self.DockerServerHealth_cursor.execute()

    def ConnectDB(self):
        pass

    def CreateDB(self):
        pass

    def InsertDB(self):
        pass

    def UpdateDB(self):
        pass

    def DeleteDB(self):
        pass

    def SelectDB(self):
        pass

    def returnData(self):
        pass


