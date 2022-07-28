# VigenereDaL2
Trabalho de Segurança Computacional - UnB - 2022/1.

Gustavo Tomás de Paula - 190014148  
Mateus de Paula Rodrigues - 190015793

## Execução
Rode o programa usando `python3 src/main.py`.

## Funcionamento
Primeiro, escolha o modo de uso (0 - cifrar, 1 - decifrar ou 2 - recuperar a chave de um texto cifrado).

Segundo, escolha um arquivo da pasta input (como _input/message.txt_).

Depois, escolha de acordo com o modo:

- Se o modo escolhido for cifrador/decifrador, escolha um arquivo com a chave (como _input/key.txt_).

- Se o modo escolhido for recuperação de senha, escolha a língua em que o texto foi escrito (inglês ou português). Por fim, escolha um índice válido na lista de tamanhos mostrados que gere uma chave coesa.

Em todos os modos, serão gerados arquivos de saída. Um para cifrador/decifrador, dois para recuperação da chave (a chave em si e o arquivo decifrado).