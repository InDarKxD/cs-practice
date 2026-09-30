MaxTemp, NotesCount, Notes, ErrorsCount = float(input()), int(input()), [], 0
for i in range(NotesCount):
    Inp = input()
    if Inp == 'error': ErrorsCount += 1
    else: Notes.append(float(Inp))