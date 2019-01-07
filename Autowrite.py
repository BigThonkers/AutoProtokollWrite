
RawText = []
with open("input.txt") as f:
    for i in f:
        i = i.strip("\n")
        RawText.append(i)
Infos = RawText[1::2]
print(Infos)
Name = Infos[0]
Dozent = Infos[1]
ExperimentNum = Infos[2]
ExpTitle = Infos[3]
Date = Infos[4]

Goal = Infos[5]
Goal = Goal.split()
GoalVerb = Goal[-1]
Goalrest = Goal[0:-1]
Goalrest = " ".join(Goalrest)



print("\\documentclass[11pt,a4paper]{article}")

print("\\usepackage[utf8]{inputenc}")
print("\\usepackage[T1]{fontenc}")
print("\\usepackage{lmodern}")
print("\\usepackage{tcolorbox}")


print("\\usepackage[german]{babel}")


print("\\setlength{\parindent}{0pt}")
print("\\setlength{\parskip}{1ex plus 0.5ex minus 0.5ex}")

print("\\usepackage{amsmath}")


print("\\usepackage{graphicx}")

print("\\usepackage[section]{placeins}")
print("\\usepackage{booktabs}")
print("\\begin{document}")


	
print("{")
print("\\centering")
print("\\large")
print("Physiklabor für Anfänger*innen \\\\")
print("Ferienpraktikum im Wintersemester 2019 \\\\[4mm]")
print("\\textbf{\\LARGE ")
print("	Versuch ", ExperimentNum, ":" ,ExpTitle)
print(")} \\\\[3mm]")
print("(durchgeführt am ", Date, " bei",  Dozent, "\\\\")
print(Name, "\\\\")
print("\\today \\\[10mm]")
print("}")

print("\\section{Einleitung}")
print("Das Ziel des Versuchs ist es, ", Goalrest, " zu ", GoalVerb)
print("\\section{Aufbau}")
print("\\section{Durchführung}")
print("\\section{Auswertung und Fehleranalyse}")
print("\\section{Diskussion der Ergebnisse}")
print("\\section{Literatur}")


