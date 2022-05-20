import json
import os
import socket
import tempfile
from testapi.settings import CERTIFICATE, PRIVATE_KEY
import ssl
import http.client


def call_api(url, method):
    headers = {'content-type': 'application/json'}
    json_data = {'method': method, 'jsonrpc': 2.0, 'id': 1}
    host = 'slb.medv.ru'

    try:
        with tempfile.TemporaryFile(mode='w+t', delete=False) as temp_crt_file:
            with tempfile.TemporaryFile(mode='w+t', delete=False) as temp_key_file:
                temp_crt_file.write(CERTIFICATE)
                temp_key_file.write(PRIVATE_KEY)
                temp_crt_file.flush()
                temp_key_file.flush()

                context = ssl.create_default_context()
                context.load_cert_chain(certfile=temp_crt_file.name, keyfile=temp_key_file.name)

                connection = http.client.HTTPSConnection(host=host, context=context)
                connection.request(method='POST', url=url, headers=headers, body=json.dumps(json_data))
                response = connection.getresponse().read()
                connection.close()

        os.remove(temp_crt_file.name)
        os.remove(temp_key_file.name)

    except BaseException as e:
        response = e

    return response
