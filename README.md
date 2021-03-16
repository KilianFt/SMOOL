# SMOOL
SMart rOs schoOL

Generic control system with GUI for different smart home features like controlling light and shutter

Potenzielle Pins für Rollläden:
  - LED auf GPIO Pin 14+15 für hoch/runter von Rollladen 1
  - LED auf GPIO Pin 16+17 für hoch/runter von Rollladen 2
 
 
## openhab
openhab muss eingerichtet mit einem MQTT Broker eingerichtet, welcher auf der gleichen IP wie openhab läuft. 
[openhab](https://www.openhab.org/)
[MQTT auf openhab](https://www.youtube.com/watch?v=RWpH9KjFYxw)

Dann können Things hinzugefügt werden, die auf einer MQTT Topic publishen oder subscriben.
Hizugefügt sind bis jetzt drei Kontrol-Schalter: Hoch, Runter, Stop.
Darunter sieht man eine Statusanzeige, welche vom MQTT client zurück geschickt wird.

## MQTT client script
Das MQTT client script kann in der branch MQTT gefunden werden.

Für die Anwendung später sollte das script automatisch gestartet werden, das kann durch folgendes gemacht werden:
- systemd service
- crontab
