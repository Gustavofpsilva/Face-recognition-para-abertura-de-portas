import face_recognition
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# Configuração da GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Use o pino GPIO que controla a trava da porta

# Lista de rostos autorizados (adicione os caminhos das imagens correspondentes)
authorized_faces = ["path/to/authorized_face_1.jpg", "path/to/authorized_face_2.jpg"]

def unlock_door():
    GPIO.output(11, GPIO.HIGH)  # Ativar a trava da porta
    time.sleep(5)  # Manter a trava ativada por 5 segundos
    GPIO.output(11, GPIO.LOW)   # Desativar a trava da porta

def main():
    # Carregar imagens autorizadas
    known_faces = [face_recognition.load_image_file(img_path) for img_path in authorized_faces]
    known_encodings = [face_recognition.face_encodings(img)[0] for img in known_faces]

    # Inicializar a câmera
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capturar frame da câmera
        ret, frame = video_capture.read()

        # Encontrar rostos no frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            # Verificar se o rosto reconhecido é autorizado
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            if True in matches:
                unlock_door()
                print("Porta destravada. Bem-vindo!")
            else:
                print("Rosto não autorizado.")

        # Exibir o frame com retângulos ao redor dos rostos
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Exibir o frame
        cv2.imshow('Video', frame)

        # Sair do loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar os recursos
    video_capture.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()  # Limpar configurações da GPIO

if __name__ == "__main__":
    main()
