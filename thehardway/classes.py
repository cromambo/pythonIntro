class Song():
  def __init__(self, lyrics):
    self.lyrics = lyrics
  def sing(self):
    for line in self.lyrics:
      print (line)
      
def main():
  happybirthday = Song("Happy birthday to you.")
  happybirthday.sing()

if __name__ == '__main__':
  main()  