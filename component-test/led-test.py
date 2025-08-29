#! /usr/bin/env python

import board
import digitalio
import math
import pwmio
import time


MILLISECONDS_PER_NANOSECOND = 1000000


def time_ms():
    return time.time_ns() / MILLISECONDS_PER_NANOSECOND

led_oe_n = digitalio.DigitalInOut(board.D4)
led_oe_n.direction = digitalio.Direction.OUTPUT
led_oe_n.value = False

led = pwmio.PWMOut(board.D12)

start_ms = time_ms()
duration_ms = 0.0
while duration_ms < 100000:
    now_ms = time_ms()
    duration_ms = now_ms - start_ms
    phase = - math.pi / 2.0 + (2 * math.pi * duration_ms) / 4000.0
    led_intensity = (math.sin(phase) + 1) * 64000.0 / 2.0 + 400
    print(duration_ms, led_intensity)
    led.duty_cycle = int(led_intensity)
    time.sleep(0.01)

led_oe_n.value = True
led.duty_cycle = 0
