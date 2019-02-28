
RawText = []
with open("input.txt") as f:
    for i in f:
        i = i.strip("\n")
        RawText.append(i)
Infos = RawText[1::2]

Name = Infos[0]
Dozent = Infos[1]
ExperimentNum = Infos[2]
ExpTitle = Infos[3]
Date = Infos[4]



Goal = Infos[5]
for i in Goal:
    if i == ",":
        MultipleGoals = True
        break
    else:
        MultipleGoals = False

#Goal = Goal.split()
#GoalVerb = Goal[-1]
#Goalrest = Goal[0:-1]
#Goalrest = " ".join(Goalrest)
#print(Goals)
if MultipleGoals == False:
    Goal = Goal.split()
    GoalVerb = Goal[-1]
    Goalrest = Goal[0:-1]
    Goalrest = " ".join(Goalrest)
    FinalFinalPhrase = Goalrest, " zu ", GoalVerb
if MultipleGoals == True:
    Goals = Goal.split(",")
    FinalPhrase = []
    for i in Goals:
        i = i.split()
        GoalVerb = i[-1]
        Goalrest = i[0:-1]
        Phrase2 = " ".join(Goalrest), " zu ", GoalVerb
        Phrase = "".join(Phrase2)
        FinalPhrase.append(" ".join(Phrase2))
        FinalFinalPhrase = ", ".join(FinalPhrase[0:-1]), " und ", FinalPhrase[-1]


Materials = Infos[6]
Materials = Materials.split(",")
MaterialsList = []
for i in Materials:
    MaterialsList.append("\\item "+ i)
MaterialsList = "\n".join(MaterialsList)




        
 #   PhraseRest = ",".join(Goals[0:-1])
  #  LastGoal = Goals[-1]
   # LastGoal = LastGoal.split()
   # GoalVerb = LastGoal[-1]
   # Goalrest = LastGoal[0:-1]
   # Goalsrest = " ".join(Goalrest)
   # Phrase = PhraseRest," und ", Goalrest[0], " zu ", GoalVerb

#PhraseFinal = "".join(Phrase)


import requests 
latools = "https://raw.githubusercontent.com/BigThonkers/AutoProtokollWrite/master/defpack.tex"
print(requests.get(latools).text)

print("\\begin{document}")


	
print("{")
print("\\centering")
print("\\large")
print("Physiklabor für Anfänger*innen \\\\")
print("Ferienpraktikum im Wintersemester 2019 \\\\[4mm]")
print("\\textbf{\\LARGE ")
print("	Versuch ", ExperimentNum, ":" ,ExpTitle)
print("} \\\\[3mm]")
print("(durchgeführt am ", Date, " bei",  Dozent, ")\\\\")
print(Name, "\\\\")
print("\\today \\\[10mm]")
print("}")
print("\\tableofcontents")
print("\\newpage")
print("\\section{Versuchsziel}")
print("Das Ziel des Versuchs ist es,", "".join(FinalFinalPhrase))
print("\\section{Aufbau}")
print("Für diesen Versuch wurden die folgenden Apparaten verwendet:")
print("\\begin{itemize}")
print(MaterialsList)
print("\\end{itemize}")
print("\\section{Durchführung}")
print("\\section{Auswertung und Fehleranalyse}")
print("\\section{Diskussion der Ergebnisse}")
print("\\section{Literatur}")
print("\\end{document}")

