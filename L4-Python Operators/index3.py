"""
Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
"""
import math
Maths=40
Science=70
Hindi=50
English=60
Raj_Marks=(Maths+Science+Hindi+English)
percentage=math.floor((Raj_Marks/400)*100)
print("Raj's percentage is:",percentage)