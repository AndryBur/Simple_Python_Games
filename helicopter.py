from utils import randcell

class Helicopter:
    def __init__(self, w, h):
       rc=randcell(w ,h)
       rx, ry=rc[0], rc[1]
       self.h=h
       self.w=w
       self.x=rx
       self.y=ry
       self.tank_max=1
       self.tank=0
       self.score=0
       self.lives=20
        

    def move(self, dx, dy):
        nx, ny=dx+self.x, dy+self.y
        if nx>=0 and ny>=0 and nx<self.h and ny<self.w:
            self.x, self.y=nx, ny
       
    def print_menu(self):
        print("🧺 ", self.tank, "/", self.tank_max, sep="", end=" | ")
        print("🏆 ", self.score, sep="", end=" | ")
        print("💛 ", self.lives, sep="")

    def data_export(self):
        return {"score":self.score, "lives":self.lives, "x":self.x, "y":self.y, "tank":self.tank, "tank_max":self.tank_max}
    
    def import_data(self, data):
        self.x=data["x"] or 0
        self.y=data["y"] or 0
        self.tank=data["tank"] or 0
        self.tank_max=data["tank_max"] or 1
        self.score=data["score"] or 0
        self.lives=data["lives"] or 20
        