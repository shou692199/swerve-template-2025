from commands2 import Command
from subsystems import Climber

class ClimbCage(Command):
  def __init__(self, climber: Climber):
    self.climber = climber

    self.addRequirements(self.climber)
    
  def initialize(self):
    self.climber.setSpeed(0.2)

  def end(self, interrupted):
    if interrupted:
      self.climber.stop()

  def isFinished(self):
    return False#self.climber.atGoalAngle()
