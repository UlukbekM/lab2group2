import rsa

pubkey,privkey = rsa.newkeys(384)
print(pubkey.save_pkcs1('PEM').decode('UTF-8'))
print(privkey.save_pkcs1('PEM').decode('UTF-8'))
