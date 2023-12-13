Reconhecimento Facial para Controle de Acesso
Este script Python utiliza a biblioteca face_recognition para implementar um sistema simples de reconhecimento facial para controle de acesso. O código é projetado para ser executado em uma Raspberry Pi, utilizando a GPIO para controlar uma trava de porta.

Requisitos
Python 3.x
Bibliotecas: face_recognition, opencv-python, numpy, RPi.GPIO
Configuração Inicial
Certifique-se de ter todas as bibliotecas instaladas. Você pode instalá-las executando:

bash
Copy code
pip install face_recognition opencv-python numpy RPi.GPIO
Configure a GPIO (pino 11 no modo BOARD) para controlar a trava da porta.

Adicione as imagens dos rostos autorizados à lista authorized_faces, fornecendo os caminhos corretos das imagens.

Uso
Execute o script:

bash
Copy code
python seu_script.py
O script captura o vídeo da câmera e verifica se os rostos detectados correspondem aos rostos autorizados na lista.

Se um rosto autorizado for detectado, a trava da porta é ativada por 5 segundos, indicando uma porta destravada. Caso contrário, é exibida a mensagem "Rosto não autorizado."

O vídeo capturado é exibido em tempo real, com retângulos ao redor dos rostos detectados.

O script pode ser encerrado pressionando a tecla 'q'.

Observações
Segurança: Este script é um exemplo básico e não deve ser usado em ambientes críticos de segurança. Considere aprimorar a segurança usando métodos adicionais.

Raspberry Pi: Certifique-se de ter as bibliotecas necessárias instaladas na Raspberry Pi. O script pode precisar de ajustes dependendo do modelo da câmera.

Limpeza da GPIO: O script limpa a configuração da GPIO ao ser encerrado para evitar problemas.
