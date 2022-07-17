localText = "Localdeki veriler"
stageText = "2"
version = ""
gitRepo = []
head = ""
val = 0


class GitHUB:
    """ 3 değişken olacak local stage version +
    push / add / commit methodları olacak
    ersiyon push olunca listeye yeni versiyonu ekleyecek
    head değişkeni olacak güncel versiyonu gösterek
    checkout adlı bir method olacak head de bulunan versiyonalrı değiştirecek."""

    def localChanges(self):
        localText = input("locale değişiklikleriniz ekleyiniz.")

    def git_add(self):
        stageText = localText

    def my_commit(self):
        version = stageText

    def git_push(self):
        gitRepo.append(version)

    def checkOut(versionNum):
        head = gitRepo[versionNum]
    while(val == 0):
        localChanges()
        git_add()
        my_commit()
        git_push()
        versionCh = int(input("Versiyon değiştirmek ister misiniz y=0 "))
        if(versionCh == 0):
            versionNum = int(input("Gidilecek versiyon numarasını giriniz"))
            checkOut(versionNum)
            print(head)
        val = int(input("Değişikliklere devam etmek ister misiniz? y=0"))
