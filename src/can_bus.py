import struct
import board
import canio
import digitalio

def setup():
    global listener
    # If the CAN transceiver has a standby pin, bring it out of standby mode
    if hasattr(board, 'CAN_STANDBY'):
        standby = digitalio.DigitalInOut(board.CAN_STANDBY)
        standby.switch_to_output(False)

    # If the CAN transceiver is powered by a boost converter, turn on its supply
    if hasattr(board, 'BOOST_ENABLE'):
        boost_enable = digitalio.DigitalInOut(board.BOOST_ENABLE)
        boost_enable.switch_to_output(True)

    can = canio.CAN(rx=board.CAN_RX, tx=board.CAN_TX, baudrate=500_000, silent=True, auto_restart=True)
    listener = can.listen(matches=[canio.Match(0x3c9)])

gear_is_reverse = False

def receive_gearbox_message(message):
    # PID 0x3c9: [6] .. .. X. .. .. ..
    # X: Transmission Gear
    # 1 -> R 0001
    # 2 -> N 0010
    # 4 -> 4 0100
    # 5 -> 3 0101
    # 6 -> 2 0110
    # 7 -> 1 0111
    # c -> 6 1010
    # e -> 5 1110
    global gear_is_reverse
    gearbox_state = struct.unpack("xxBxxx", message.data)[0] >> 4
    gear_is_reverse = (gearbox_state) is 1

def debug_message(message):
    print("%x: " % message.id + ' '.join("%02x" % x for x in message.data))

def receive():
    in_waiting = listener.in_waiting()
    while in_waiting > 0:
        message = listener.receive()
        if message.id is 0x3c9:
            receive_gearbox_message(message)
        else:
            debug_message(message)
        in_waiting = in_waiting - 1
