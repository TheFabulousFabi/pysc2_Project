import downloder


class UI:

    def __init__(self):

        self.Europa = False
        self.Nordamerika = False
        self.Korea = False
        self.ligen = [self.Europa, self.Nordamerika, self.Korea]
        self.qualitaetsstufen = ["gr", "ma", "di", "pl", "go", "si", "br"]
        self.mindestqualitaetsstufen = []
        self.version = ""

    def ligafestlegen(self):

        # welche Ligen sollen gedownloaded werden
        print(
            " Welche Liegen sollen gedownloaded werden\n Falls mehrere gedownloaded werden sollen muss die Eingabe durch ein Leerzeichen getrennt werden\n z.B. 1 2 3 ")
        print(" <1> Europa\n <2> Nordamerika\n <3> Korea\n <4> Alle\n ")
        eingabe = [int(i) for i in input().split()]

        for i in eingabe:
            if i == 4:

                for liga in range(len(self.ligen)):
                    self.ligen[liga] = True

            else:

                self.ligen[int(i) - 1] = True

        print(self.ligen)

    def qualifestlegen(self):

        index = 0
        print("Bitte waelen Sie die Mindestqualitaet der Replays aus.\n")
        print(" <1> Grandmaster\n <2> Master\n <3> Diamant\n <4> Platin\n <5> Gold\n <6> Silber\n <7> Bronze\n")
        eingabe = input()

        while (index < int(eingabe)):

            self.mindestqualitaetsstufen.append(self.qualitaetsstufen[index])
            index += 1

        print(self.mindestqualitaetsstufen)

    def version_festlegen(self):

        versionen = ["4.0", "3.19", "3.18", "3.17"]
        print(" Welche vrsion moechten Sie festlegen?\n\n <1> 4.0\n <2> 3.19\n <3> 3.18\n <4> 3.17\n")
        eingabe = input()
        self.version = versionen[int(eingabe) - 1]

    def vorgang(self):

        self.ligafestlegen()
        self.qualifestlegen()
        self.version_festlegen()
        Downloade = downloder.downloder(self.ligen[0], self.ligen[1], self.ligen[2], self.mindestqualitaetsstufen,
                                        self.version)
        Downloade.vorgang()


test = UI()
test.vorgang()
