MaxTemp, NotesCount, Notes, ErrorsCount, Exceeding = float(input()), int(input()), [], 0, 0
for i in range(NotesCount):
    Inp = input()
    if Inp == 'error': ErrorsCount += 1
    else: Notes.append(float(Inp))
for i in Notes: Exceeding += 1 if i > MaxTemp else 0