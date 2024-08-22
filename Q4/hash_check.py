import hashlib

voucher_code = '6218b6f3f429c2fa1d20e2b04daed3bb'

hash = hashlib.md5(b'jj7910939=#').hexdigest()

print("Voucher Code:", voucher_code)
print ("Calculated Hash:", hash)
