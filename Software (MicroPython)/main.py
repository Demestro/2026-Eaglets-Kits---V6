strip = Neopixel(2, 0, 16, "GRB")
red = (255, 0, 0)
blue = (0, 0, 255)
strip.brightness(100)
strip.set_pixel(0, red)
strip.set_pixel(1, blue)
strip.show()

from machine import Pin, I2C
import time

# Initialize I2C (pins may vary depending on your board)
i2c = I2C(1, scl=Pin(19), sda=Pin(18))  # adjust pins for your MCU

# Initialize sensor
tof = VL53L4CD(i2c)

# Start ranging (continuous mode)
tof.start_ranging()

try:
    while True:
        if tof.data_ready:
            dist = tof.distance   # distance in cm
            print("Distance:", dist, "cm")
            tof.clear_interrupt()
        time.sleep(0.05)

except KeyboardInterrupt:
    tof.stop_ranging()
    print("Stopped")
    
