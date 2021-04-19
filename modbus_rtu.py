# import fcntl
import struct
from serial import Serial, PARITY_EVEN
from umodbus.client.serial import rtu


class modbus_rtu():
    def __init__(self):
        print("modbus RTU protocol")

    def get_serial_port(self, port):
        self.device_port = port
        """ Return serial.Serial instance, ready to use for RS485."""
        self.port = Serial(port=self.device_port, baudrate=19200, parity=PARITY_EVEN, stopbits=1, bytesize=8,
                           timeout=1000)
        return self.port

    def write_coil_register(self, slave_id, address, port, value):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1
        message = rtu.write_single_coil(slave_id=int(slave_id), address=add, value=int(value))
        response = rtu.send_message(message, self.serial_port)
        print(response)
        self.serial_port.close()

    def read_coil_registers(self, slave_id, address, quantity, port):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1
        message = rtu.read_coils(slave_id=int(slave_id), starting_address=add, quantity=int(quantity))
        hexadecimal_string = message.hex()
        print(hexadecimal_string)
        response = rtu.send_message(message, self.serial_port)
        print("response", response)
        result = []
        # return response
        count = 0
        for offset in range(int(address), int(address) + int(quantity)):
            print("offset", offset)
            # for i in response:
            if offset == 100:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 101:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 102:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 103:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 10:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 124:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 131:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 183:
                res = response[count] / 10
                print("Factory value", res)
            else:
                res = response[count]
                print(res)
            count = count + 1
            result.append(res)

        return result, hexadecimal_string
        self.serial_port.close()

    def write_holding_register(self, slave_id, address, port, value):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1

        if int(value) < 0:
            value1 = int(value) + 2 ** 16
        else:
            value1 = int(value)
        print(value1)
        message = rtu.write_single_register(slave_id=int(slave_id), address=add, value=int(value1))
        print(message)
        hexadecimal_string = message.hex()
        print(hexadecimal_string)
        response = rtu.send_message(message, self.serial_port)
        print(response)
        print(type(response))
        self.serial_port.close()

    def read_holding_registers(self, slave_id, address, quantity, port):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1
        message = rtu.read_holding_registers(slave_id=int(slave_id), starting_address=add, quantity=int(quantity))
        print(message)
        hexadecimal_string = message.hex()
        print(hexadecimal_string)
        response = rtu.send_message(message, self.serial_port)
        print("response", response)
        index = 0
        for i in response:

            if (i & 0x8000):
                s16 = -(((~i) & 0xFFFF) + 1)
            else:
                s16 = i
            response[index] = s16
            index = index + 1
        result = []
        # return response
        count = 0
        for offset in range(int(address), int(address) + int(quantity)):
            print("offset", offset)
            # for i in response:
            if offset == 100:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 101:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 102:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 103:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 10:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 124:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 131:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 183:
                res = response[count] / 10
                print("Factory value", res)
            else:
                res = response[count]
                print(res)
            count = count + 1
            result.append(res)
            self.serial_port.close()
        return result
        # return res

    def read_discrete_inputs(self, slave_id, address, quantity, port):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1
        message = rtu.read_discrete_inputs(slave_id=int(slave_id), starting_address=add, quantity=int(quantity))
        hexadecimal_string = message.hex()
        print(hexadecimal_string)
        response = rtu.send_message(message, self.serial_port)
        print("response", response)

        result = []
        # return response
        count = 0
        for offset in range(int(address), int(address) + int(quantity)):
            print("offset", offset)
            # for i in response:
            if offset == 100:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 101:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 102:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 103:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 10:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 124:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 131:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 183:
                res = response[count] / 10
                print("Factory value", res)
            else:
                res = response[count]
                print(res)
            count = count + 1
            result.append(res)

        return result, hexadecimal_string
        self.serial_port.close()

    def read_input_registers(self, slave_id, address, quantity, port):
        self.serial_port = self.get_serial_port(port)
        add = int(address) - 1
        message = rtu.read_input_registers(slave_id=int(slave_id), starting_address=add, quantity=int(quantity))
        hexadecimal_string = message.hex()
        print(hexadecimal_string)
        response = rtu.send_message(message, self.serial_port)

        print("response", response)

        result = []
        # return response
        count = 0
        for offset in range(int(address), int(address) + int(quantity)):
            print("offset", offset)
            # for i in response:
            if offset == 100:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 101:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 102:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 103:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 10:
                res = response[count] / 10
                print("Factory value", res)
            # print("count",count)
            elif offset == 124:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 131:
                res = response[count] / 10
                print("Factory value", res)

            elif offset == 183:
                res = response[count] / 10
                print("Factory value", res)
            else:
                res = response[count]
                print(res)
            count = count + 1
            result.append(res)

        return result, hexadecimal_string
        self.serial_port.close()

    def modbus_disconnect(self):
        self.serial_port.close()

# a=modbus_rtu()
# a.write_coil_register(5,101,"COM2",1)
# a.read_coil_registers(5,100,6,"COM2")
# a.write_holding_register(5,216,"COM2",-500)
# a.read_holding_registers(5,100,6,"COM2")
# a.read_discrete_inputs(5,100,6,"COM2")
# a.read_input_registers(5,100,6,"COM2")
