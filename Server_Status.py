# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import os
from API_Return import ServerAPI


class HostServerStatus:
    def __init__(self):
        self.api = ServerAPI  # .ExecuteCommand(CMDType=None, UsedType=None, CMDName=None)

        self.CMDType = ["MemoryUsed", "StorageUsed", "network", "docker-inspect"]
        self.UsedType = ["network-interface", "docker-container"]
        self.CMDName = []
        self.Command = self.api.ExecuteCommand(CMDType="MemoryUsed")

    def Memory_Used(self):
        pass

    def Storage_Used(self):
        pass


class DockerServerStatus:
    def __init__(self):
        pass

    def Container_IDorName(self):
        pass

    def WEBorWAS_Server_Alive(self):
        pass

    def Container_Network(self):
        pass

    def Memory_Used(self):
        pass

    def Storage_Used(self):
        pass

    def Process_List(self):
        pass





