 1# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
 2# SPDX-License-Identifier: MIT
 3
 4import time
 5import board
 6import adafruit_bno055
 7
 8
 9i2c = board.I2C()
10sensor = adafruit_bno055.BNO055_I2C(i2c)
11
12# If you are going to use UART uncomment these lines
13# uart = board.UART()
14# sensor = adafruit_bno055.BNO055_UART(uart)
15
16last_val = 0xFFFF
17
18
19def temperature():
20    global last_val  # pylint: disable=global-statement
21    result = sensor.temperature
22    if abs(result - last_val) == 128:
23        result = sensor.temperature
24        if abs(result - last_val) == 128:
25            return 0b00111111 & result
26    last_val = result
27    return result
28
29
30while True:
31    print("Temperature: {} degrees C".format(sensor.temperature))
      #Measures the temperature of the chip in degrees Celsius.
32    """
33    print(
34        "Temperature: {} degrees C".format(temperature())
35    )  # Uncomment if using a Raspberry Pi
36    """
37    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
      #Gives the raw accelerometer readings, in m/s. Returns an empty tuple of length 3 when this property has been disabled by the current mode.
38    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
      #Gives the raw magnetometer readings in microteslas. Returns an empty tuple of length 3 when this property has been disabled by the current mode.
39    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
40    print("Euler angle: {}".format(sensor.euler))
41    print("Quaternion: {}".format(sensor.quaternion))
42    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
43    print("Gravity (m/s^2): {}".format(sensor.gravity))
      #Returns the gravity vector, without acceleration in m/s. Returns an empty tuple of length 3 when this property has been disabled by the current mode.
44    print()
45
46    time.sleep(1)
