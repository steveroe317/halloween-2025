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

pir = digitalio.DigitalInOut(board.D26)
pir.direction = digitalio.Direction.INPUT

start_ms = time_ms()
duration_ms = 0.0
while True:
    now_ms = time_ms()
    duration_ms = now_ms - start_ms
    if pir.value and led.duty_cycle == 0:
        print("motion detected")
        led.duty_cycle = 32000.0
    else:
        led.duty_cycle = 0
    time.sleep(0.01)

led_oe_n.value = True
led.duty_cycle = 0
