# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import os
from API_Return import ServerAPI


class HostServerStatus:
    def __init__(self):
        self.Command = ""

    def Memory_Used(self):
        return os.system(self.JsonParser["MemoryUsed"])

    def Storage_Used(self):
        return os.system(self.JsonParser["StorageUsed"])


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





