import itertools
import binascii

"""This program is to encrypt the following text using a key 'ICE'
Text to be encrypted: “We didn't start the fire, It was always burning, Since the
world's been turning, We didn't start the fire, No we didn't
light it, But we tried to fight it”

    Author : Harish Kommineni
    Date : September 1, 2016
"""

# xor key with data, repeating key as and when necessary
def xor_data(solution, text):
    if len(solution) == 1:
        key = ord(solution)
        return ''.join(chr(ord(x) ^ key) for x in text)
    series = itertools.cycle(solution)
    return ''.join(chr(ord(x) ^ ord(y)) for x,y in zip(text, series))

# This method is to compare the encrypted text with expected output.
def key_encrypt():

    output = '1e26652d2a2127643169303128313169372d2c632320312065630c3d6332283065282f32283a366921303b2d2c27246969102c27202069372d2c63322631292d64366921202c2d653d3637272a2b2e6f651e26652d2a2127643169303128313169372d2c632320312065630b2663322c632120272b6e3765252a222137652037696901303d63322c63313b2a202d633126632320242d3d632c3d'
    plain_text = """We didn't start the fire, It was always burning, Since the world's been turning, We didn't start the fire, No we didn't light it, But we tried to fight it"""

    cipher_text = xor_data('ICE', plain_text)

    # Convert the cipher text to byte array.
    bytes = str.encode(cipher_text)

    #Convert the to hex decimal output
    binascii.hexlify(bytes)

    # Compare the output with expected output.
    print ('Output is matched to expected output' if cipher_text == output else 'Output not matched')
    print ('ICE: %s...' % cipher_text[:64])

# Main method for the program to encrypt the text with key 'ICE'
if __name__ == '__main__':
    key_encrypt();
