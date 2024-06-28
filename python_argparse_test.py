#!/usr/bin/env python3
# argparse 를 이용하여 python 으로 php 처럼 한줄 cli 코드를 쉽게 실행하기 위한 연구
import argparse
import sys
from subprocess import call

__arg_parser = argparse.ArgumentParser(
    prog="PrintHello",
    description="인사하는 파이썬 CLI"
)

__arg_parser.add_argument("-v", "--version", action="store_true")
__arg_parser.add_argument("-u", "--username", default="")
__arg_parser.add_argument("-mh", "--host", default="")
__arg_parser.add_argument("-mu", "--user", default="")
__arg_parser.add_argument("-mp", "--password", default="")

__argv = __arg_parser.parse_args(sys.argv[1:])

host: str = __argv.host
user: str = __argv.user
password: str = __argv.password
username: str = __argv.username
call('/usr/bin/mysql -uroot -ppassword mysql -e "select * from user"')

show_version: bool = __argv.version

hello: str = f"안녕{f', {username}' if username else ''}. Python 으로부터"
version: str = f" - python version : {sys.version_info.major}.{sys.version_info.minor}" if show_version else ""

print(f"{hello}{version}")
