# gEther on RaspberryPi

## config.txt
lastline -> `dtoverlay=dwc2`

## cmdline.txt
after rootwait -> `modules-load=dwc2,g_ether`

## /etc/network/interfaces
```
allow-hotplug usb0
iface usb0 inet static
        address 192.168.2.2
        netmask 255.255.255.0
        network 192.168.2.0
        broadcast 192.168.7.255
        gateway 192.168.2.1
```
