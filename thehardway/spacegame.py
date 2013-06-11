import sys

class Scene(object):
  def enter(self):
    print ('This is a generic scene. Subclass and implement me!')
    

class Death(Scene):
  def enter(self):
    print ('You died in a funny way. Haha. My game is simple and unforgiving.')
    sys.exit(1)
    
class CentralCorridor(Scene):
  def enter(self):
    print ('You see a gothon standing there.')
    print ('What do you do?', end=' ')
    corridorChoice = input()
    if 'joke' in corridorChoice:
      print ('You tell a joke and the Gothon\'s head explodes. You pass by into the Laser Weapon Armory')
      return 'Laser Weapon Armory'
    else:
      print ('It\'s not super effective')
      return 'Central Corridor'
      
class LaserWeaponArmory(Scene):
  def enter(self):
    print ('There\'s a keypad, guess the combination: ', end = '')
    keypadGuess = input()
    if '69' in keypadGuess:
      print ('You get the bomb and run out of the room to the bridge')
      return 'The Bridge'
    else:
      print ('That\'s not the combination. It explodes.')
      return 'Death'
      
class TheBridge(Scene):
  def enter(self):
    print ('You place the bomb on the bridge and leave for the escape pod bay')
    return 'Escape Pod'
    
class EscapePod(Scene):
  def enter(self):
    print ('You jump in the escape pod and get the girl. (...what girl?). Grats!')
    sys.exit(0)
    
class Engine(object):
  def __init__(self, sceneMap):
    print ('Engine Init')
    self.sceneMap = sceneMap

  def play(self):
    print ('Engine playing')
    currentScene = self.sceneMap.openingScene()
    while True:
      nextSceneName = currentScene.enter(currentScene)
      print ('--------You are at: %s ----------------' % nextSceneName)
      currentScene = self.sceneMap.lookupScene(nextSceneName)
    
  sceneMap = 0
     
class Map(object):
  def __init__(self, startScene):
    if startScene in self.sceneLookupTable:
      self.startScene = startScene
   
  def lookupScene(self, sceneName):
    if sceneName in self.sceneLookupTable:
      return self.sceneLookupTable[sceneName]
    else:
      print ('Scene name %s not found' % sceneName)
      sys.exit(-1)
    
  def openingScene(self):
    return self.sceneLookupTable[self.startScene]
  
  startScene = ''
  sceneLookupTable = {
    'Central Corridor'    :CentralCorridor,
    'Escape Pod'          :EscapePod,
    'The Bridge'          :TheBridge,
    'Laser Weapon Armory' :LaserWeaponArmory,
    'Death'               :Death
    
  }
  
def main():
  sceneMap = Map('Central Corridor')
  gameEngine = Engine(sceneMap)
  gameEngine.play()
  
  sceneMap.openingScene()

if __name__ == '__main__':
  main()  