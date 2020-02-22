# SMOOL
SMart rOs schoOL

Generic control system with GUI for different smart home features like controlling light and shutter


Current state tutorial:

LEDs repräsentieren Rollladen hoch oder runter

Bis jetzt sind 2 Rollläden benutzbar:
  - LED auf GPIO Pin 14+15 für hoch/runter von Rollladen 1
  - LED auf GPIO Pin 16+17 für hoch/runter von Rollladen 2

Systemd Service manual_control.service ist durchgehend am laufen (startet und restartet automatisch)
Das heißt:

  Durchgehender Button Control mit Buttons verbunden mit GPIO Pins 9-12.
  - Button 9+10 für hoch/runter von Rollladen 1
  - Button 11+12 für hoch/runter von Rollladen 2
  Jeder klick sendet 5 Sekunden lang Signal an entsprechende LED (also an Pin OUT).
  Keine Kontrolle ob Rollladen auf oder zu ist.
 
 
ROS Nodes:

  Zwei ROS Nodes sind bis jetzt vorhanden:
  - shutter_control.py
    Besteht aus GUI zum kontrollieren aller Rollläden. Sollte auf Haupt-Kontroll-PC laufen.
    Um alle Rollläden eines Gebäudes/Etage/Raum zu steuern "99" in entsprechendes Feld eintragen.
    
  - shutter_slave.py
    Hört bis jetzt nur Signal von shutter_control.py zu und führt Befehl aus. 
    Mit Überprüfung ob Rollladen schon oben/unten ist.
    Jeder Befehl gibt (wie vorher) 5 Sekunden lang Strom auf entsprechenden PIN
    
    
QUICKSTART ROS

  Um alle ROS Nodes (control und slave) zu starten folgenden Befehl in Konsole eingeben:
  $ roslaunch shutter shutter.launch
  
  Um nur Control ROS Node zu starten:
   $ roslaunch shutter shutter_control.launch
    
