class Okul():
    tip = "egitimhane"

    def __init__(self, calisan=3, bina=1, idaribina=1, önbahce=True):
        self.calisan = calisan
        self.bina = bina
        self.idaribina = idaribina
        self.önbahce = önbahce


okul1 = Okul(50, 1, 1, True)
okul2 = Okul(20, 1, 2, False)
okul3 = Okul(calisan=12, idaribina=1)
print(okul3.calisan)
print(okul1.__class__.tip)
