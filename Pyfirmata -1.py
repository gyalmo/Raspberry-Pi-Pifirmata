#PyFirmata -1

Import pyfirmata
board = pyfirmata.Arduino (‘dev/ttyACMO’)
pin13 = board.get_pin(‘d:13:o’)
pin13 = write(1)
pin13 = write(0)
board.exit()
