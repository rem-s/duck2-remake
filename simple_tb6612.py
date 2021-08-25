from lib.TB6612 import TB6612
import time

def main():
  tb6612 = TB6612()
  val = 1
  incr = 1
  m = 1
  print("TB6612 PWM running. Press CTRL+C to exit.")

  try:
    while True:
      time.sleep(0.5)
      if val >= 30:
        incr = -incr
      if val <= 0:
        incr = -incr
        tb6612.set_mode_a(TB6612.STOP)
        tb6612.set_mode_b(TB6612.STOP)
        m = -m
      val += incr
      if m == 1:
        print("A", val)
        tb6612.set_mode_a(TB6612.CW, pwm_value=val)
      else:
        print("B", val)
        tb6612.set_mode_b(TB6612.CW, pwm_value=val)
  finally:
    pass # cleanup process

if __name__ == '__main__':
  main()

