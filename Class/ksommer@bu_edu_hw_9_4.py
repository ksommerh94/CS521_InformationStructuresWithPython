'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 4 pages 564-566

'''
# There are many websites where you could listen to music , for example, rhapsody.com .
# A music album ontains many sountracks and each sountrack has a name , time duration,  name of artist, year and other data.
# Design classes fot sountrack and album
class Soundtrack:
    def __init__(self,name,time_duration,artist,year,other_data):
        self.name=name
        self.time_duration=time_duration
        self.artist=artist
        self.year =year
        self.other_data =other_data

    def play(self):
        pass
    def stop(self):
        pass
    def pause(self):
        pass
    def __str__(self):
        return "Song is:"+self.name+" by "+self.artist

class Album:
    def __init__(self,l_soundtracks,name):
        self.l_soundtracks=l_soundtracks
        self.name=name

    def __str__(self):
        return "Album is "+str(self.name)

l_st=[]
st=Soundtrack('Rojo','3:04','Jbalvin',2020,'First single')
l_st.append(st)
st=Soundtrack('Negro','3:20','Jbalvin',2020,'Eng: Black')
l_st.append(st)
st=Soundtrack('Azul','2:48','Jbalvin',2020,'Eng: Blue')
l_st.append(st)

album=Album(l_st,'colores')
print(album)
print(album.l_soundtracks[0])
print(album.l_soundtracks[1])
print(album.l_soundtracks[2])
