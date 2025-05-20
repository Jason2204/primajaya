grade = ''
nilai = int(input('Masukkan Nilai: '))
if nilai >= 90 and nilai == 100:
    grade = 'A'
elif nilai >= 80 and nilai <= 89:
    grade = 'B'
elif nilai >= 60 and nilai <= 79:
    grade = 'C'
elif nilai >= 100:
    grade = 'Error!'
else:
    grade = 'D'

print("Grade nilaimu adalah: " + grade)