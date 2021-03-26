# SMOOL
SMart schOOL

Generic control system with GUI for different smart home features like controlling light and shutter

## Quickstart
Wenn der Raspberry Pi soweit konfiguriert ist, müssen nur die GPIO pins wie folgend angeschlossen werden:

1. Rollläden verbinden 


|   | Rollladen 1 | Rollladen 2  | Button (alle zusammen) |
|---|---|---|---|
| Hoch | GPIO17 | GPIO23 | GPIO20 |
| Runter | GPIO27 | GPIO24 | GPIO21 |
| Erdung | Beliebig | Beliebig | Beliebig |

Die Erdung kann mit einem beliebigen Ground Pin am Raspberry Pi verbunden werden.  
Die Buttons sind für den Fall da, dass OpenHab nicht erreichbar ist. Mit ihnen können alle Rollläden unabhängig von OpenHab geöffnet und geschlossen werden.

2. Licht verbinden

|   | Licht 1 |
|---|---|
| An/Aus | GPIO19 |
| Erdung | Beliebig |

## Neuen Raspi aufsetzen
1. Repository clonen
2. Systemd service erstellen
3. GPIO Pins verbinden (siehe Quickstart)
4. Sicherstellen, dass IP-Adressen stimmen
5. SmartHome genießen
 
 
## openhab
openhab muss mit einem MQTT Broker eingerichtet werden, welcher auf der gleichen IP wie openhab läuft. 
[openhab](https://www.openhab.org/)
[MQTT auf openhab](https://www.youtube.com/watch?v=RWpH9KjFYxw)

Dann können Things hinzugefügt werden, die auf einer MQTT Topic publishen oder subscriben.

## Scripts
### MQTT client script
Das MQTT client script kann in der branch MQTT gefunden werden. Es ist das Gegenstück zu OpenHab und soll dessen Kommandos ausführen.

### Manual Control
Dieses script funktioniert unabhängig von OpenHab und fährt mithilfe von Buttons alle Rollläden hoch oder runter.


## Geplante Features
- Logisch sicherstellen, dass Rollladen nicht gleichzeitig hoch und runter Kommando bekommen kann.
- Licht auch unabhängig von OpenHab steuern können (extra Button?)
- ISO image von Raspbian mit SMOOL erstellen
- Config Dateien erstellen, zur einfachen Personalizierung
