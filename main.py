import glob
import os
from string import ascii_uppercase
# import http.client
import stun


def check_environment():
    for file in glob.glob(f'**/.env.template', recursive=True):
        with open(file) as f:
            while line := f.readline():
                if line[0] in ascii_uppercase:
                    if not os.getenv(f"{line.split('=')[0].strip()}"):
                        # Внешний IP средствами python
                        # conn = http.client.HTTPConnection("ifconfig.me")
                        # conn.request("GET", "/ip")
                        # ip = conn.getresponse().read()
                        # error_message = f"{line.split('=')[0].strip()} is None"

                        # Внешний IP через библиотеку pystun3
                        nat_type, external_ip, external_port = stun.get_ip_info()
                        error_message = f"{line.split('=')[0].strip()} is None. nat_type: {nat_type}, external_ip: {external_ip}, external_port={external_port}"

                        raise Exception(error_message)
                        # print(error_message)


if __name__ == '__main__':
    check_environment()
