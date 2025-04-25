from listener import PLCListener

instance = PLCListener("192.168.1.253", 8500)

instance.write("DM36535", 16706)