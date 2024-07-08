from OpenSSL import crypto, SSL
from socket import gethostname
from os.path import exists, join

CERT_FILE = "server.crt"
KEY_FILE = "server.key"

def create_self_signed_cert(cert_dir):
    if not exists(join(cert_dir, CERT_FILE)) or not exists(join(cert_dir, KEY_FILE)):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)
        
        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "US"
        cert.get_subject().ST = "California"
        cert.get_subject().L = "San Francisco"
        cert.get_subject().O = "My Company"
        cert.get_subject().OU = "My Organizational Unit"
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')
        
        with open(join(cert_dir, CERT_FILE), "wb") as cert_file:
            cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        with open(join(cert_dir, KEY_FILE), "wb") as key_file:
            key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

create_self_signed_cert(".")
