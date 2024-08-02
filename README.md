# modbus_scanner

Those scripts can scan the RS485 bus on selected COM port. They return the content of the found register. If the register does not exists, they report "register address does not exist". The scan range can be set.

Script:
scan_modbus_RTU.py     includes all pymodbus debug output
scan_modbus_RTU_2.py   only reports the registers
