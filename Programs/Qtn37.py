import time

try:
  while True:
    print ('='*50)
    print ("If you want to stop, press 'CTRL + C'")
    time.sleep(1)
except KeyboardInterrupt:
  print ("So you finally pressed, 'CTRL + C'.. Good!!.")
except Exception as error:
  print ("Got new error!! -->", error)