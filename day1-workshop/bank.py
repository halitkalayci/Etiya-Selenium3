import password_utils

def register(username,password):
    password_utils.is_valid_password(password)

def login(username,password):
    password_utils.is_valid_password(password)


# Eğer kodlar tekrar ediyorsa ortak bi fonksiyona çevir.
# Eğer fonksiyon farklı bi sorumluluk ise farklı bir modüle ekle.