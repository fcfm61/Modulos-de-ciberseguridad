import hashlib
from cryptography.fernet import Fernet 

def encrypt_msg(): #Cambiar el mensaje directamente desde el codigo :)    
    # Generar clave
    key = Fernet.generate_key() 
    cipher_suite = Fernet(key) 

    # Cifrar mensaje
    message = b"Top secret."
    cipher_text = cipher_suite.encrypt(message) 
    print ( f"Encriptar_mensaje: {cipher_text} " ) 

    # Descifrar mensaje
    plain_text = cipher_suite.decrypt(cipher_text) 
    print ( f"Descifrar_mensaje: {plain_text.decode()} " )

    # Aplicar hashing para verificar el mensaje
    message = "Top secret." 
    hash_object = hashlib.sha256(message.encode()) #Generar Hash
    hex_dig = hash_object.hexdigest() 
    print (f"Hash SHA-256: {hex_dig} " )

