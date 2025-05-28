#!/usr/bin/env python

import bluerobotics_navigator as navigator
import time
import math


def color_from_sine(percentage):
    pi = math.pi
    red = (math.sin(percentage * 2.0 * pi) * 0.5) + 0.5
    green = (math.sin((percentage + 0.33) * 2.0 * pi) * 0.5) + 0.5
    blue = (math.sin((percentage + 0.67) * 2.0 * pi) * 0.5) + 0.5
    return [
        int(red * 255),
        int(green * 255),
        int(blue * 255),
    ]


def main():
    if platform.machine() == "aarch64":
        # It's possible to set the configuration before initializing the navigator, check this example
        from bluerobotics_navigator import NavigatorVersion, Raspberry
        print("Setting up for Navigator V2 on Raspberry Pi 5")
        navigator.set_rgb_led_strip_size(1)
        navigator.set_navigator_version(NavigatorVersion.Version2)
        navigator.set_raspberry_pi_version(Raspberry.Pi5)

    navigator.init()

    print("Creating rainbow effect!")
    while True:
        steps = 1000
        for i in range(steps):
            ratio = i / steps
            navigator.set_neopixel([color_from_sine(ratio)])
            time.sleep(0.01)


if __name__ == "__main__":
    main()
