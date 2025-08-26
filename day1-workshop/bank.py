import password_utils

def register(username,password):
    valid = password_utils.is_valid_password(password)
    if not valid:
        print("Şifre validasyon kurallarına uymuyor.")

def login(username,password):
    valid = password_utils.is_valid_password(password)
    if not valid:
        print("Şifre validasyon kurallarına uymuyor.")


# Eğer kodlar tekrar ediyorsa ortak bi fonksiyona çevir.
# Eğer fonksiyon farklı bi sorumluluk ise farklı bir modüle ekle.