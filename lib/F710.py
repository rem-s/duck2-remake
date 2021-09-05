import pygame
import os

class F710(object):
  DEVICE_NAME = "Logitech Gamepad F710"

  AXIS = 0
  BUTTON = 1
  HAT = 2

  # BUTTON_NAME = (Assigned Event, Assigned Number)
  
  LEFT_STICK_X = (AXIS, 0)
  LEFT_STICK_Y = (AXIS, 1)
  RIGHT_STICK_X = (AXIS, 3)
  RIGHT_STICK_Y = (AXIS, 4)
  LEFT_TRIGGER = (AXIS, 2)
  RIGHT_TRIGGER = (AXIS, 5)

  A_BUTTON = (BUTTON, 0)
  B_BUTTON = (BUTTON, 1)
  X_BUTTON = (BUTTON, 2)
  Y_BUTTON = (BUTTON, 3)
  LEFT_BUMPER = (BUTTON, 4)
  RIGHT_BUMPER = (BUTTON, 5)
  BACK_BUTTON = (BUTTON, 6)
  START_BUTTON = (BUTTON, 7)
  LEFT_STICK_IN = (BUTTON, 8)
  RIGHT_STICK_IN = (BUTTON, 9)
  GUIDE_BUTTON = (BUTTON, 10)

  HAT_SWITCHES = (HAT, -1)

  def __init__(self, auto_detect=True, device_num=0):
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.joystick.init()

    if auto_detect == True:
      self.device = None
      for i in range(0, pygame.joystick.get_count()):
        if pygame.joystick.Joystick(i).get_name() == F710.DEVICE_NAME:
          self.device = pygame.joystick.Joystick(i)
      if not self.device:
        print("Not found %s" % F710.DEVICE_NAME)
        exit(0)
    else:
      self.device = pygame.joystick.Joystick(device_num)

    print("Gamepad F710 has initialized. Please use X-Box mode on the gamepad.")
    self.device.init()

  def __del__(self):
    pygame.joystick.quit()

  def get_status(self, button):
    event, num = button
    if event == AXIS:
      return self.device.get_axis(num)
    elif event == BUTTON:
      return self.device.get_button(num)
    elif event == HAT:
      return self.device.get_hat(num)

