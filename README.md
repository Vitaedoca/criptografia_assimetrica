# Criptografia Assimétrica com RSA

Este projeto implementa um algoritmo de criptografia assimétrica usando RSA, onde as mensagens são cifradas e decifradas utilizando as chaves pública e privada.

## Como usar
1. O programa gera automaticamente as chaves pública e privada.
2. O usuário insere uma mensagem a ser cifrada.
3. A mensagem é cifrada utilizando a chave pública e decifrada utilizando a chave privada.

## Dependências
- `cryptography`

## Execução
Execute o script `main.py` para interagir com o sistema de criptografia.

## Demonstração

### 1. O Sistema Iniciando
Aqui você verá a execução inicial do sistema, onde as chaves são geradas automaticamente.

![Início do Sistema](./start.png)

### 2. Entrada da Mensagem
Após a execução, o programa solicita que o usuário insira a mensagem a ser criptografada.

![Digite sua frase](./frase.png)

### 3. Resultado Final
A chave pública gerada e o texto cifrado são exibidos, seguidos pela decodificação da mensagem original com a chave privada.

![Chave Pública e Texto Cifrado](./end.png)

## Contribuição
Sinta-se à vontade para fazer melhorias ou enviar pull requests. Caso tenha alguma dúvida ou sugestão, entre em contato!
