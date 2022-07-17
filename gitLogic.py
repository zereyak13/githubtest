

class GitHUB:
    """ 3 değişken olacak local stage version +
    push / add / commit methodları olacak
    ersiyon push olunca listeye yeni versiyonu ekleyecek
    head değişkeni olacak güncel versiyonu gösterek
    checkout adlı bir method olacak head de bulunan versiyonalrı değiştirecek."""
    localText = "Localdeki veriler"
    stageText = "2"
    version = ""
    gitRepo = []
    head = ""
    val = 0

    def localChanges(self):
        self.localText = input("locale değişiklikleriniz ekleyiniz.")

    def git_add(self):
        self.stageText = self.localText

    def my_commit(self):
        self.version = self.stageText

    def git_push(self):
        self.gitRepo.append(self.version)

    def checkOut(self, versionNum):
        self.head = self.gitRepo[versionNum]

    def startGit(self):
        while(self.val == 0):
            self.localChanges()
            self.git_add()
            self.my_commit()
            self.git_push()
            versionCh = int(input("Versiyon değiştirmek ister misiniz y=0 "))
            if(versionCh == 0):
                versionNum = int(
                    input("Gidilecek versiyon numarasını giriniz"))
                self.checkOut(versionNum)
                print("verison: " + str(versionNum) + self.head)
            self.val = int(
                input("Değişikliklere devam etmek ister misiniz? y=0"))
            if(self.val != 0):
                for i in range(len(self.gitRepo)):
                    print("version {0}: içerik:{1} ".format(
                        i, self.gitRepo[i]))


accesGit = GitHUB()
accesGit.startGit()
