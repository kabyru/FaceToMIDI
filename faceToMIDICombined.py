import subprocess
import os
os.system("pip install pretty_midi")
import pretty_midi
import csv

cwd = os.getcwd()
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg")], title='Select the image you would like to convert to MIDI.') # show an "Open" dialog box and return the path to the selected file
print(filename)
subprocess.run(["OpenFace_2.0.5_win_x64/FaceLandmarkImg.exe", "-f", filename, "-out_dir", cwd, "-of", "ProcessedImage.jpg", "-2Dfp", "-pose", "-gaze", "-tracked"])

facePiano = pretty_midi.PrettyMIDI()
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

with open("processedImage.csv", newline = '') as csvfile:
    next(csvfile)
    data = list(csv.reader(csvfile))

dataParse = data[0]

timePlay = 0

for dataRange in range(296,431):
    notePlay = float(dataParse[dataRange])
    while notePlay >= 108:
        notePlay = notePlay/2
    notePlayInt = int(notePlay)
    print(notePlayInt)

    note = pretty_midi.Note(velocity=100, pitch=notePlayInt, start=timePlay, end=timePlay+.25)
    timePlay = timePlay + .25
    piano.notes.append(note)

facePiano.instruments.append(piano)
facePiano.write('processedMIDI.mid')

#The next step is modifying the software to handle the X&Y locations at the same time