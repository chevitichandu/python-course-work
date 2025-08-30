class Details:
    def __init__(self,name,mail,pwd):
        self.name=name
        self._mail=mail
        self.__pwd=pwd

    def getpassword(self):
         return self.__pwd
    def setpassword(self,new_password):
         self.__pwd=new_password


sumanth=Details("Sumanth","sumanth@gmail","Sumanth@123")

print(sumanth.name)
sumanth.name="Sanjay"
print(sumanth.name)


print(sumanth._mail)
sumanth._mail="sanjay@gmail"
print(sumanth._mail)


print(sumanth.getpassword())
sumanth.setpassword("Sanjay@123")
print(sumanth.getpassword())





class Bank:
    def __init__(self):
        self.name="xyz"
        self._balance=0
    @property
    def noresbalance(self):
        return self._balance
    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount


b=Bank()

print(b.noresbalance)
b.noresbalance=3000
print(b.noresbalance)




class Instagram:
    def __init__(self,username,bio,account_status=False):
        self.username+username
        self._bio=bio
        self._bio



        

class Status:
    def __init__(self,caption,image,video=None):
        self.caption=caption
        self.image=image
        self.video=video
        self.videolength=30
        
    def see_status(self):
        if self.video:
            print(f"---{self.video}---\n'{self.caption}'")
        else:
            print(f"---{self.image}---\n'{self.caption}'")

            
class Statusv1(Status):
    def likes(self):
        print("Like")
    def addmusic(self,music):
        print("Music Added")
        
gopal=Status("Hey i'm using whatsapp","goodmrng.png")

gopal.see_status()

gopi=Statusv1("Good Evening","coffee.png")

gopi.see_status()
gopi.likes()
gopi.addmusic("softcore")





class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")

class Statusv1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

class Statusv2(Status):
    def like(self):
        print(f'You can like status')

class Statusv3(Statusv1,Statusv2):
    def addMusic(self,music):
        self.music=music
        print(f'{self.music}...is added to your status')

class Statusv4(Statusv3):
    def videolength(self,video):
        self.video=video
        print(f'{self.video} is uploaded to  your status')
        
sravani=Status()
sravani.uploadImage('selfie.png')

hema=Statusv1()
hema.uploadImage('GoodMrng.png')
hema.addCaption("Morning Friends!!!!")

vaishnavi=Statusv2()
vaishnavi.uploadImage("Coffee.png")
vaishnavi.like()


deepika=Statusv3()
deepika.uploadImage("Mountains_and_Trees.png")
deepika.addCaption("no wifi")
deepika.like()
deepika.addMusic("MAture.mp3")

nikitha=Statusv4()
nikitha.uploadImage("Sunrise.png")
nikitha.addCaption("Nothing")
nikitha.like()
nikitha.addMusic("Music")
nikitha.videolength("Somevideo.mp4")
