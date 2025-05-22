import time
import paho.mqtt.client as mqtt

broker = "localhost"
topic = "demo/topic"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker)

while True:
    message = "Hello from publisher!"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(5)
