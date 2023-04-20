#!/usr/bin/python3
"""
Description:    Python3 Port Scanner
Maintainer:     Lee
version:        v0.1.0
"""
import argparse
import socket
import textwrap
import threading


def connection_scan(target_ip, target_port):
    try:
        conn_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
        conn_socket.connect((target_ip, target_port))
        print("[+] {}/tcp open".format(target_port))
    except OSError:
        print("[-] {}/tcp closed".format(target_port))
    finally:
        conn_socket.close()


def port_scan(target, port_num):
    try:
        target_ip = socket.gethostbyname(target)
    except OSError:
        print("[^] Cannot resolve {}: Unknown host".format(target))
        return

    try:
        target_name = socket.gethostbyaddr(target_ip)
        print('[*] Scan Results for: {}'.format(target_name[0]))
    except OSError:
        print('[*] Scan Results for: {}'.format(target_ip))

    t = threading.Thread(target=connection_scan, args=(target, int(port_num)))
    t.start()


def argument_parser():
    parser = argparse.ArgumentParser(
        prog='port_scanner.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Python3 TCP port scanner
            ------------------------
            Python3 TCP port scanner helps you find TCP/IP open ports.
            You can scan your target instance with multiply ports. It's 
            fast, lightweight, easy to use.
            '''))
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80,8080'")

    var_args = vars(parser.parse_args())

    return var_args


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",")
        for port in port_list:
            port_scan(host, port)
    except AttributeError:
        print("Error. Please provide the correct arguments.")