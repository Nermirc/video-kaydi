import cv2

# Video kaydetme işlemi için kamerayı açıyoruz
cap = cv2.VideoCapture(0)

# Kameranın çözünürlüğünü alıyoruz (genişlik ve yükseklik)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Frame genişliği (genellikle ekran genişliği)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Frame yüksekliği (genellikle ekran yüksekliği)
print(width, height)  # Kameradan alınan çözünürlük bilgilerini ekrana yazdırıyoruz

# Video kaydını başlatıyoruz.
# "video_kaydı.mp4" adında bir dosya oluşturulacak ve "DIVX" codec'i ile video kaydedilecektir.
# 20, saniye başına kaç kare (frame) kaydedileceğini belirtir (fps).
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))

while True:
    # Kameradan bir kare (frame) okuyalım
    ret, frame = cap.read()
    
    # Eğer kare alınabilirse, video penceresinde gösterelim
    if ret:
        cv2.imshow("Video", frame)
    
        # Kareyi video dosyasına kaydedelim
        writer.write(frame)
    
    # 'q' tuşuna basıldığında döngüden çıkıp videoyu durduracağız
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kamera ve video yazıcıyı serbest bırakıyoruz, işlem bittiğinde kaynakları temizliyoruz
cap.release()
writer.release()

# Açılan tüm pencereleri kapatıyoruz
cv2.destroyAllWindows()

