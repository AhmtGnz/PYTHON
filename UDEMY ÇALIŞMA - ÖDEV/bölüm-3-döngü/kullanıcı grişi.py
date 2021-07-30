print("""
Kullanıcı Girişi Programı
""")

sys_kullanıcı_adı = "ahmet"

sys_şifre = "246380"
giriş_hakkı = 3

while True:

    kullanıcı_adı = input("Kullanıcı Adı:")
    şifre = input("Şifre:")

    if (kullanıcı_adı != sys_kullanıcı_adı and şifre == sys_şifre):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and şifre != sys_şifre):
        print("Şifre Hatalı")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and şifre != sys_şifre):
        print("Kullanıcı Adı ve Şifre Hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme Başarıyla Giriş Yaptınız.")
        break
    if giriş_hakkı == 0:
        print("Giriş Hakkınız Kalmadı.")
        break