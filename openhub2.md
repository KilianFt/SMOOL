# SMOOL with openhub
Openhub2 (OH2) will be the main platform to control all smart home devices. It can also be setup so that it works as a MQTT broker. To control a shutter, therefore only a server is needed which comunicates with the broker.
## MQTT server
- should subscribe to the MQTT control topic published by OH2
- should publish to the MQTT state topic subscibed by OH2