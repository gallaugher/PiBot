# control-pibot.py

# once running, you can test with the shell commands:
# To start the robot:
# mosquitto_pub -h pibot.local -t "pibot/move" -m "forward"
# To stop the robot:
# mosquitto_pub -h pibot.local -t "pibot/move" -m "stop"

import paho.mqtt.client as mqtt

from adafruit_motorkit import MotorKit
kit = MotorKit()

clientName = "PiBot"
serverAddress = "pibot"
mqttClient = mqtt.Client(clientName)

# If the robot veers left or right, add a small amount to the left or right trim, below
# until the bot moves roughly straight. The #s below reflect the bot I'm working with.
# It's probably best to start both trim values at 0 and adjust from there.
# out of 1.0 full power.
LEFT_TRIM   = -0.01
RIGHT_TRIM  = 0.0

leftSpeed = 1.0 + LEFT_TRIM
rightSpeed = 1.0 + RIGHT_TRIM

# This will make turns at 50% of the speed of fwd or backward
slowTurnBy = 0.5

def connectionStatus(client, userdata, flags, rc):
    print("subscribing")
    mqttClient.subscribe("pibot/move")
    print("subscribed")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')
    
    if message == "forward":
        kit.motor1.throttle = leftSpeed
        kit.motor2.throttle = rightSpeed
        print("^^^ moving forward! ^^^")
        print(leftSpeed,rightSpeed)
    elif message == "stop":
        kit.motor1.throttle = 0.0
        kit.motor2.throttle = 0.0
        print("!!! stopping!")
    elif message == "backward":
        kit.motor1.throttle = -leftSpeed
        kit.motor2.throttle = -rightSpeed
        print("\/ backward \/")
        print(-leftSpeed,-rightSpeed)
    elif message == "left":
        kit.motor1.throttle = -leftSpeed * slowTurnBy
        kit.motor2.throttle = rightSpeed * slowTurnBy
        print("<- left")
        print(-leftSpeed * slowTurnBy,rightSpeed * slowTurnBy)
    elif message == "right":
        kit.motor1.throttle = leftSpeed * slowTurnBy
        kit.motor2.throttle = -rightSpeed * slowTurnBy
        print("-> right")
        print(leftSpeed * slowTurnBy,-rightSpeed * slowTurnBy)
    else:
        print("?!? Unknown message?!?")

# Set up calling functions to mqttClient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

# Connect to the MQTT server & loop forever.
# CTRL-C will stop the program from running.
mqttClient.connect(serverAddress)
mqttClient.loop_forever()
