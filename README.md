move the `.service` file to `/lib/systemd/system/`

```
sudo systemctl daemon-reload
sudo systemctl enable <.service file name>
sudo restart
```

update `/lib/systemd/system/pigpiod.service` to match the one in this repo

start pigpiod
```
sudo pigpiod
sudo pigs pud 4 u
```

