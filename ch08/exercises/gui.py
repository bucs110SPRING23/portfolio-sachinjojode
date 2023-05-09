class Move:
    def __init__(self, pnum=1):
        self.player_num = pnum
        self.speed = 1
        self.jump_height = 1
        self.jump_distance = 1
        
class Collide:
    def __init__(self, pnum=1):
        self.player_num = pnum
        self.collide = False
        self.collide_type = None
        self.collide_direction = None
        self.collide_object = None
        
class Player:
    def __init__(self, pnum=1):
        self.player_num = pnum
        self.score = 0
        self.lives = 3
        self.coins = 0
        
class Goomba:
    def __init__(self):
        self.g_height = 1
        self.g_speed = 1
        self.g_damage = True
        
class Text:
    def __init__(self):
        self.text = None
        self.text_size = 1
        self.text_color = "white"
        self.text_font = 20
        self.text_pos = None
        
        
