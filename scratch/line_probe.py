#!/usr/bin/env python3
"""Простейший TCP-пробник для проверки старых устройств."""

import argparse
import socket


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port", type=int)
    parser.add_argument("--send", default="", help="строка, unicode_escape")
    args = parser.parse_args()

    with socket.create_connection((args.host, args.port), timeout=3) as sock:
        if args.send:
            sock.sendall(args.send.encode().decode("unicode_escape").encode())
        sock.settimeout(1.5)
        chunks = []
        try:
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                chunks.append(data)
        except socket.timeout:
            pass

    print(b"".join(chunks).decode("utf-8", "replace"))


if __name__ == "__main__":
    main()
