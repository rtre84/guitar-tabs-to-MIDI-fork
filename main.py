#!/usr/bin/python3
from read_tabs import Tabs
from midi_generator import *
import os
import argparse


def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Convert guitar tabs to MIDI')
    parser.add_argument('fname', help='Path to the tab file')
    parser.add_argument('--tempo', '-t', type=int, default=100, help='Tempo of the song (default: 100)')
    parser.add_argument('--output', '-o', help='Output where the midi will be written')

    # Parse the arguments
    args = parser.parse_args()

    fname = args.fname
    tempo = args.tempo

    t = Tabs(fname)
    t.preprocess()
    t.displayTabs()
    t.convertNotes()

    outputTrack = Track(int(tempo))
    outputTrack.midiGenerator(t.a)
    command = "timidity output.mid"
    os.system(command)

    # For Colab: Convert MIDI to WAV and play using IPython
    try:
        # Try to convert MIDI to WAV file
        command = "timidity output.mid -Ow -o output.wav"
        result = os.system(command)

        if result == 0:  # Success
            print("MIDI converted to WAV successfully!")
            # Play the WAV file in Colab
            from IPython.display import Audio, display
            display(Audio("output.wav"))
        else:
            print("Error converting MIDI to WAV")

    except Exception as e:
        print(f"Error: {e}")
        # Fallback: just inform user that MIDI file was created
        print("MIDI file 'output.mid' has been created successfully!")
        print("You can download it and play it with any MIDI player.")


if __name__ == '__main__':
    main()
