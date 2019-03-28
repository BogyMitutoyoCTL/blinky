Wir erstellen eine *Systemd Service Datei*:

```console
pi@raspberrypi:~/blinky $ chmod +x blink.py
pi@raspberrypi:~ $ sudo vi /lib/systemd/system/bogy.service
```

Der Inhalt sollte dann folgender sein:

```bash
[Unit]
Description=bogy
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecStart=/home/pi/blinky/blink.py
WorkingDirectory=/home/pi/blinky/
StandardOutput=null
StandardError=null
Restart=always
RestartSec=15
User=root
Group=root

[Install]
WantedBy=multi-user.target
Alias=bogy.service
```

Mit 

```console
pi@raspberrypi:~ $ sudo systemctl daemon-reload 
pi@raspberrypi:~ $ sudo systemctl enable bogy.service
```
*enablen* wir den Service...

Danach starten wir den Service mit

```console
pi@raspberrypi:~ $ sudo systemctl start bogy.service 
```

Und mit 

```console
pi@raspberrypi:~ $ sudo systemctl status bogy.service 
```
sollten wir eine ähnlich Ausgabe erhalten wie hier:

```console
● pressure_and_temp.service - PressureAndTempSensor
   Loaded: loaded (/lib/systemd/system/bogy.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2018-09-01 13:22:00 UTC; 16s ago
 Main PID: 1810 (blah)
   CGroup: /system.slice/pressure_and_temp.service
           └─1810 /usr/bin/python3 /home/pi/blinky/blink.py

```

