import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.subscribe("sensor/data")
client.loop_forever()
