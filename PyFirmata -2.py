#Pyfirmata -2

Import pyfirmata
Import time
board = pyfirmata.Arduino (‘dev/ttyACMO’)
analog _pin = board.get_pin(‘a:1:i’)
it=pyfirmata.util.Iterator(board)
it.start()
analog_pin.enable_reporting()
while True:
  reading = analog_pin.read()
  If reading!=None:
     voltage = reading = 5.0
     print (“Reading = %f\t voltage= %f%(reading,Voltage))
time.sleep(1)
