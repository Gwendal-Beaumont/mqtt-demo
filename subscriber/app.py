import paho.mqtt.client as mqtt

broker = "localhost"
topic = "demo/topic"


def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code", rc)
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker)
client.loop_forever()
