import time
import paho.mqtt.client as mqtt

broker = "mqtt"
topic = "demo/topic"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    message = "Hello from publisher!"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(5)
