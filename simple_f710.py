from lib.F710 import F710
import time

def main():
  f710 = F710()
  val = 1
  incr = 1
  m = 1
  print("F710 Capture running. Press CTRL+C to exit.")

  try:
    while True:
      time.sleep(0.5)
      print("left trigger", f710.get_status(F710.LEFT_TRIGGER), "right trigger", f710.get_status(F710.RIGHT_TRIGGER))
  finally:
    pass # cleanup process

if __name__ == '__main__':
  main()

