













print("\\documentclass[11pt,a4paper]{article}")

import requests 
latools = "https://raw.githubusercontent.com/BigThonkers/LaTools/master/tool%20kit.tex"
print(requests.get(latools).text)

print("\\begin{document}")


	
print("{")
print("\\centering")
print("\\large")
print("Physiklabor für Anfänger*innen \\\\")
print("Ferienpraktikum im Sommersemester 2018 \\\\[4mm]")
print("\\textbf{\\LARGE ")
print("	Versuch 75: Lichtmikroskop")
print(")} \\\\[3mm]")
print("(durchgeführt am 02.10.2018 bei Daniel Bartle) \\\\")
print("Ye Joon Kim, Marouan Zouari\\\\")
print("\\today \\\[10mm]")
print("}")

print("\\section{Einleitung}")
print("\\section{Aufbau}")
print("\\section{Durchführung}")
print("\\section{Auswertung und Fehleranalyse}")
print("\\section{Diskussion der Ergebnisse}")
print("\\section{Literatur}")


