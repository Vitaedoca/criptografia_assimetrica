from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Função para gerar chaves pública e privada
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    # Serializa as chaves para salvar em arquivos ou enviar
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

# Função para cifrar uma mensagem com a chave pública
def encrypt_message(message, public_key):
    public_key = serialization.load_pem_public_key(public_key)
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Função para decifrar uma mensagem com a chave privada
def decrypt_message(ciphertext, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

def main():
    print("=== Criptografia Assimétrica RSA ===")
    
    # Gera as chaves pública e privada
    private_key, public_key = generate_rsa_keys()

    print("\nChave Pública (Base64):")
    print(public_key.decode('utf-8'))

    # Solicita a mensagem ao usuário
    message = input("\nDigite a mensagem que deseja cifrar: ")

    # Cifra a mensagem
    ciphertext = encrypt_message(message, public_key)
    print("\nTexto Cifrado (em bytes):")
    print(ciphertext)

    # Decifra a mensagem
    decrypted_message = decrypt_message(ciphertext, private_key)
    print("\nTexto Decifrado:")
    print(decrypted_message)

if __name__ == "__main__":
    main()
