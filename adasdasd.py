class OgrenciIslemleri:
    def my_function(self):
        studentNum = int(input("Öğrenci sayısını giriniz."))
        thislist = []

        for i in range(0, studentNum):
            name = input("Öğrenci adını giriniz.")
            thislist.append(name)

        thislist.sort()

        for i in thislist:
            print(i)

    def call_fonk(self):
        boolVal = 1
        while(boolVal == 1):
            self.my_function()
            boolVal = int(input("Sınıf kaydı girmek ister misiniz?  0/1"))


""" User  Interface """
ogrenciIslemi = OgrenciIslemleri()
ogrenciIslemi.call_fonk()
