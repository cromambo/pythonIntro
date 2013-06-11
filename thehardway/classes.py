class Scene(object):
  def enter(self):
    pass
    
class Engine(object):
  def __init__(self, sceneMap):
    pass
  def play(self):
    pass
    
class Death(Scene):
  def enter(self):
    pass
class CentralCorridor(Scene):
  def enter(self):
    pass
class LaserWeaponArmory(Scene):
  def enter(self):
    pass
class TheBridge(Scene):
  def enter(self):
    pass
class EscapePod(Scene):
  def enter(self):
    pass
   
class Map(object):
  def __init__(self, start_scene):
    pass
   
  def nextScene(self, sceneName):
    pass
  def openingScene(self):
    pass
      
def main():
  gameMap = Map('Central Corridor')
  gameEngine = Engine(gameMap)
  gameEngine.play()

if __name__ == '__main__':
  main()  