from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import logging

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)  

# Configure the client
client = ModbusClient(method='rtu', port='COM6', baudrate=4800, timeout=1, parity='N', stopbits=1, bytesize=8)

# Connect to the client
connection = client.connect()
if not connection:
    print("Failed to connect to the Modbus device")
else:
    # Function to write a single register
    def write_single_register(client, unit_id, address, value):
        try:
            result = client.write_register(address=address, value=value, unit=unit_id)
            if result.isError():
                print(f"Error writing to register {address}: {result}")
            else:
                print(f"Successfully wrote value {value} to register {address}")
        except Exception as e:
            print(f"Exception writing to register {address}: {str(e)}")

    # Specify the Modbus address of the device and the register to write
    unit_id = 1  # Modbus address of the device
    address = 2000  # Register address to write
    value = 3  # Value to write

    # Write the value to the register
    write_single_register(client, unit_id, address, value)

    # Close the client connection
    client.close()
