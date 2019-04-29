import time
import rtmidi
import random

DEFAULT_PORT_NAME = 'USB2.0-MIDI'
MIDI_CHANNEL = 0x91
midi_port = None

BPM = 60
TAKT = 60 / BPM / 4

def takt_len(bpm, metrum=4):
    return 60 / BPM / metrum

def open_midi_port(default_port_name=DEFAULT_PORT_NAME):
    mo = rtmidi.MidiOut()
    midi_port = None
    for port_no in range(mo.get_port_count()):
        port_name = mo.get_port_name(port_no)
        print("MIDI out:", port_name)
        if port_name.find(default_port_name) > -1:
            midi_port = mo.open_port(port_no)
            return midi_port

# TODO: make it a class... because it is polluting the namespace
def send_midi(msg, port=midi_port):
    port.send_message(msg)
    time.sleep(0.0005)  # musi być, bo inaczej nie gra

def gen_cc_msg(channel, param, value):
    if param == FILTER_Q:
        value = int(min(value, 0.75 * 127))
    return [0xb0 + channel - 1, param, value]

FILTER_Q = 71
FILTER_FREQ = 74
CHANNEL = 3

def xy_to_fq(x, y):
    scaled_x = int(abs(x * 127))
    scaled_y = int(abs(y * 127))
    print(scaled_x, scaled_y)

    send_midi(gen_cc_msg(CHANNEL, FILTER_FREQ, scaled_x), port=midi_port)
    send_midi(gen_cc_msg(CHANNEL, FILTER_Q, scaled_y), port=midi_port)


def main():
    global midi_port 
    

    while True:
        x = random.random()
        y = random.random()
        xy_to_fq(x, y)
        time.sleep(8 * takt_len(BPM))

if __name__ == "__main__":
    main()
else:
    midi_port = open_midi_port()