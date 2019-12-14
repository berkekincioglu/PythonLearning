#########################################################BLOCKCHAIN########################################################################
import binascii
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import pprint

def create_open_screat_couple_key():
    seed = Crypto.Random.new().read
    screat_key = RSA.generate(1024,seed)
    open_key = screat_key.PublicKey()
    screat_key_hex = binascii.hexlify(screat_key.exportKey(format='DER')).decode('ascii')
    open_key_hex = binascii.hexlify(open_key.exportKey(format='DER')).decode('ascii')
    return (open_key_hex,screat_key_hex)
def couple_key_verify(screat_key_hex,open_key_hex):
    screat_key= RSA.importKey(binascii.unhexlify(screat_key_hex))
    open_key=screat_key.PublicKey()
    return open_key_hex==binascii.hexlify(open_key.exportKey(format='DER')).decode('ascii')
    
def hash(message):
    return SHA.new(str(message).encode('utf-8'))
def sign(screat_key_hex,message):
    screat_key=RSA.importKey(binascii.unhexlify(screat_key_hex))
    signer =PKCS1_v1_5.new(screat_key)
    message_hash = hash(message)
    signature = signer.sign(message_hash)
    return binascii.hexlify(signature).decode('ascii')
def verify(open_key_hex,message,message_signature):
    open_key = RSA.importKey(binascii.unhexlify(open_key_hex))
    message_hash = hash(message)
    message_signature = binascii.unhexlify(message_signature)
    verifier = PKCS1_v1_5.new(open_key)
    return verifier.verify(message_hash,message_signature)













