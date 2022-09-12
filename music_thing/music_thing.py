import enum
import itertools


WHOLE = 2
HALF = 1
MAJOR = (WHOLE, WHOLE, HALF, WHOLE, WHOLE, WHOLE, HALF)
MINOR = MAJOR[5:] + MAJOR[:5]
PENTATONIC = (WHOLE, WHOLE, HALF+WHOLE, WHOLE)
MAJOR_CHORD_INTERVALS = (0, 4, 7)
MINOR_CHORD_INTERVALS = (0, 3, 7)


class Note(enum.IntEnum):
    A = 0
    Bb = 1
    B = 2
    C = 3
    Db = 4
    D = 5
    Eb = 6
    E = 7
    F = 8
    Gb = 9
    G = 10
    Ab = 11

    def __str__(self):
        return self.name


def make_major_scale(tonic):
    next_note = tonic
    for step in itertools.cycle(MAJOR):
        yield Note(next_note)
        next_note = (next_note + step) % 12


def make_minor_scale(tonic):
    next_note = tonic
    for step in itertools.cycle(MINOR):
        yield Note(next_note)
        next_note = (next_note + step) % 12


def make_major_scale_with_octaves(tonic, starting_octave):
    next_note, octave = tonic, starting_octave
    for step in itertools.cycle(MAJOR):
        yield Note(next_note), octave
        next_note = next_note + step
        if next_note >= 12:
            octave += 1
            next_note %= 12


def make_major_pentatonic_scale(tonic):
    next_note = tonic
    for step in itertools.cycle(PENTATONIC):
        yield Note(next_note)
        next_note = (next_note + step) % 12


def make_major_chord(tonic):
    return [Note((tonic+x)%12) for x in MAJOR_CHORD_INTERVALS]


def make_minor_chord(tonic):
    return [Note((tonic+x)%12) for x in MINOR_CHORD_INTERVALS]
