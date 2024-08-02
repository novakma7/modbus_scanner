from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import logging

# Enable logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Configure the client
client = ModbusClient(method='rtu', port='COM6', baudrate=9600, timeout=1, parity='N', stopbits=1, bytesize=8)

# Connect to the client
connection = client.connect()
if not connection:
    print("Failed to connect to the Modbus device")
else:
    # Function to read a single input register
    def read_single_input_register(client, unit_id, address):
        try:
            result = client.read_input_registers(address=address, count=1, unit=unit_id)
            if result.isError():
                print(f"Error reading register {address}: {result}")
            else:
                return result.registers[0]
        except Exception as e:
            print(f"Exception reading register {address}: {str(e)}")

    # Function to scan registers within a range
    def scan_registers(client, unit_id, start_address, end_address):
        for address in range(start_address, end_address + 1):
            register_value = read_single_input_register(client, unit_id, address)
            if register_value is not None:
                print(f"Register {address}: {register_value}")

    # Specify the Modbus address of the device and the range to scan
    unit_id = 1  # Modbus address of the device
    start_address = 0  # Start address of the scan
    end_address = 9  # End address of the scan

    # Scan the registers
    scan_registers(client, unit_id, start_address, end_address)

    # Close the client connection
    client.close()
