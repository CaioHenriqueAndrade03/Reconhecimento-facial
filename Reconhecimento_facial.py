import cv2


cap = cv2.VideoCapture(0)

face_glasses = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

###########################
#regra das letras
cor_do_texto=(255,255,255)
grossura_da_letra = 1
###########################



while True:
    ret, video = cap.read()
    video = cv2.flip(video, 1)
    videoCinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    rostos = face_cascade.detectMultiScale(videoCinza, 1.3, 5)

    for (x, y, w, h) in rostos:
        cv2.rectangle(video, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        
        
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(video, texto_rosto, (x, y - 10), font, 0.5, cor_do_texto, grossura_da_letra, cv2.LINE_AA)

        olhos = face_glasses.detectMultiScale(videoCinza)

        for (gx, gy, gw, gh) in olhos:
            cv2.rectangle(video, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)
            cv2.putText(video, texto_olho, (gx, gy - 10), font, 0.5, cor_do_texto, grossura_da_letra, cv2.LINE_AA)


        #REGRAS DOS TEXTO:
        texto_olho = f"{(gx + gw // 2)}, {(gy + gh // 2)} cordenada olho"
        texto_rosto = f"{(x + w // 2)}, {(y + h // 2)} cordenada rosto"
    cv2.imshow('Reconhecimento Facial', video)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
