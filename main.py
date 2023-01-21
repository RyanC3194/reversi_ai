from env import Reversi

if __name__ == '__main__':
    r = Reversi(8)
    r.rendor()
    r.step((3,5))
    r.rendor()
    r.step((4,5))
    r.rendor()
