import os
import sys
import json


class Permissions:

    filepath = "configs/role.json"
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    @classmethod
    def owner_perm(cls):
        permissions = cls.data["owner"] + cls.data["moderator"] + cls.data["vip"] + cls.data["all"]
        return permissions
    
    @classmethod
    def moderator_perm(cls):
        permissions = cls.data["moderator"] + cls.data["vip"] + cls.data["all"]
        return permissions
    
    @classmethod
    def vip_perm(cls):
        permissions = cls.data["vip"] + cls.data["all"]
        return permissions
    
    @classmethod
    def all_perm(cls):
        permissions = cls.data["all"]
        return permissions
