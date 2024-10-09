toplam_fiyat = float(input("lütfen bir fiyat giriniz."))
sipariş_günü = input("lütfen bir gün giriniz.")
kullanıcı_tipi = input("lütfen bir kullanıcı tipi giriniz.")
if sipariş_günü == "pazartesi" or sipariş_günü == "cuma" and kullanıcı_tipi == "premium" and toplam_fiyat < 500 :
  print(toplam_fiyat * 0.10)
elif sipariş_günü == "pazartesi" or sipariş_günü == "cuma" and kullanıcı_tipi == "premium" and toplam_fiyat < 500 :
  print(toplam_fiyat * 0.15)
if sipariş_günü == "salı" or sipariş_günü == "çarşamba" or sipariş_günü == "perşembe" and kullanıcı_tipi == "premium" and kullanıcı_tipi == "normal" :
  print(toplam_fiyat * 0.10)
if sipariş_günü == "cumartesi" or sipariş_günü == "pazar" and kullanıcı_tipi == "premium" and toplam_fiyat < 750 :
  print(toplam_fiyat * 0.10)
elif sipariş_günü == "cumartesi" or sipariş_günü == "pazar" and kullanıcı_tipi == "premium" and toplam_fiyat > 750 :
  print(toplam_fiyat * 0.20)
if sipariş_günü == "pazartesi" or sipariş_günü == "cuma" and kullanıcı_tipi == "normal"  toplam_fiyat > 500 :
  print(toplam_fiyat * 0.5)
if sipariş_günü == "cumartesi" or sipariş_günü == "pazar" and kullanıcı_tipi == "normal" and toplam_fiyat > 750 
  print(toplam_fiyat * 0.10)
elif kullanıcı_tipi == "normal" and toplam_fiyat > 1500 :
  print(toplam_fiyat * 0.3)

