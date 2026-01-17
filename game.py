class agent:
    def __init__(self,name,age):
        print('Welcome to the Game!')
        self.name=name
        self.age=age
        self.health=100
        self.alive=True
    def cur_helath(self):
        print('current health of',self.name,'is',self.health)
    def punched(self):
        self.health-=10
    def shooted(self):
        self.health-=50
    def info(self):  
        if self.health<=0:
            self.alive=False
        print('Name:',self.name)
        print('Age:',self.age)
        print('Health:',self.health) 
        print('Alive:',self.alive) 
        if(self.health>=1000):
            print("This person become Boss \n congrats!")
p1=agent('Nikhil',19)  
p1.health=2000
p1.punched()
p1.punched()
p1.shooted()
p1.shooted()
p1.info()  
print('-'*50)    
p2=agent('Harsh',20)  
p2.punched()
p2.shooted()
p2.info()  
class boss(agent):                         #inheritance
    def blow_fire(self):
        print("Blow Fire!") 
print('-'*50)        
#creating object of the boss class
bs=boss('keshav',25)
bs.info()
bs.blow_fire()