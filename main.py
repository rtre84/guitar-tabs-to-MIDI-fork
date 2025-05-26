#!/usr/bin/python3
from read_tabs import Tabs
from midi_generator import *
import os
import argparse


def main():

    # In the interest of making this debuggable and runnable in a Collab notebook
    # fname = input("Enter file location: ")
    # fname = "basic_pitch_transcription_changed.txt"
    fname = "basic_pitch_transcription.txt"

    # In the interest of making this debuggable and runnable in a Collab notebook
    # tempo = input("Enter tempo of song: ")
    tempo = ""

    if tempo == "":
        tempo = 100

    t = Tabs(fname)
    t.preprocess()
    t.displayTabs()
    t.convertNotes()

    outputTrack = Track(int(tempo))
    outputTrack.midiGenerator(t.a)
    command = "timidity output.mid"
    os.system(command)

if __name__ == '__main__':
    main()
