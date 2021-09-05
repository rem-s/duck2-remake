import RPi.GPIO as GPIO
import time
class TB6612(object):
  # 0b<IN1><IN2><PWM><STBY>
  CCW = 0b0111
  CW = 0b1011
  BREAK = 0b1111
  STOP = 0b0011
  STBY = 0b0000

  N_STBY = 0
  N_PWM  = 1
  N_IN2  = 2
  N_IN1  = 3

  def __init__(self, gpio_mode=GPIO.BOARD, ain1=24, ain2=22, pwma=32, bin1=38, bin2=40, pwmb=33, stby=26):
    self.AIN1 = ain1
    self.AIN2 = ain2
    self.PWMA = pwma
    self.BIN1 = bin1
    self.BIN2 = bin2
    self.PWMB = pwmb
    self.STBY = stby

    GPIO.setmode(gpio_mode)
    GPIO.setup(self.AIN1, GPIO.OUT)
    GPIO.setup(self.AIN2, GPIO.OUT)
    GPIO.setup(self.PWMA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self.BIN1, GPIO.OUT)
    GPIO.setup(self.BIN2, GPIO.OUT)
    GPIO.setup(self.PWMB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self.STBY, GPIO.OUT, initial=GPIO.LOW)

    self.pa = GPIO.PWM(self.PWMA, 50)
    self.pb = GPIO.PWM(self.PWMB, 50) 

  def __del__(self):
    self.set_mode_a(TB6612.STBY, 0)
    self.set_mode_b(TB6612.STBY, 0)
    time.sleep(1)

    self.pa.stop()
    self.pb.stop()
    GPIO.cleanup()

  def set_mode_a(self, mode, pwm_value=0):
    GPIO.output(self.AIN1, self._mode_bits(mode, TB6612.N_IN1))
    GPIO.output(self.AIN2, self._mode_bits(mode, TB6612.N_IN2))
    if self._mode_bits(mode, TB6612.N_PWM) == GPIO.HIGH:
      self.pa.start(pwm_value)
    else:
      self.pa.stop()
    GPIO.output(self.STBY, self._mode_bits(mode, TB6612.N_STBY))

  def set_mode_b(self, mode, pwm_value=0):
    GPIO.output(self.BIN1, self._mode_bits(mode, TB6612.N_IN1))
    GPIO.output(self.BIN2, self._mode_bits(mode, TB6612.N_IN2))
    if self._mode_bits(mode, TB6612.N_PWM) == GPIO.HIGH:
      self.pb.start(pwm_value)
    else:
      self.pb.stop()
    GPIO.output(self.STBY, self._mode_bits(mode, TB6612.N_STBY))

  def _mode_bits(self, mode, n):
    if mode & (1 << n):
      return GPIO.HIGH
    else:
      return GPIO.LOW
