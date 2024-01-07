import pygame
import random

# clasa pentru zona zaruri
class ZonaZaruri:
    def __init__(self,screen):
        self.screen=screen
        self.height_zona_zaruri=200
        self.zar1=None
        self.zar2=None
        self.button_press=False
        self.dubla=False
        self.ramas=None

    # resetam setarile pentru zona zaruri
    def Restart(self):
        self.zar1=None
        self.zar2=None
        self.button_press=False
        self.dubla=False
        self.ramas=None

# clasa pentru tabla de joc
class Table:
    def __init__(self,screen,width_screen,height_screen):
        self.screen=screen
        self.width_screen=width_screen
        self.height_screen=height_screen
        self.poz_right_tabla=20
        self.dim_piesa=60
        self.dim_margini=20
        self.width_tabla=13*self.dim_piesa+2*self.dim_margini
        self.height_tabla=11*self.dim_piesa+2*self.dim_margini

        # pozitii prntru triungiuri tabla (doar capetele triunghiurilor, intr un vector)
        poz_triunghiuri=[(self.dim_margini+self.poz_right_tabla+i*self.dim_piesa, self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-1) for i in range(13,-1,-1)]
        for i in range(14):
            poz_triunghiuri.append((self.dim_margini+self.poz_right_tabla+i*self.dim_piesa,(self.height_screen-self.height_tabla)//2+self.dim_margini))

        # pozitii prntru triungiuri tabla (cele 3 varfuri intr-un tuplu)
        self.puncte_triunghiuri=[]
        height1=self.height_screen//2-self.dim_piesa//2
        height2=self.height_screen//2+self.dim_piesa//2
        for i in range(len(poz_triunghiuri)-1):
            if i != 6 and i!=20 and i!=13:
                if i<13:
                    self.puncte_triunghiuri.append([poz_triunghiuri[i],poz_triunghiuri[i+1],((poz_triunghiuri[i][0]+poz_triunghiuri[i+1][0])//2,height2)])
                else:
                    self.puncte_triunghiuri.append([poz_triunghiuri[i],poz_triunghiuri[i+1],((poz_triunghiuri[i][0]+poz_triunghiuri[i+1][0])//2,height1)])  
        
        self.puncte_triunghiuri_player1=[poz_triunghiuri[6],poz_triunghiuri[6+1],((poz_triunghiuri[6][0]+poz_triunghiuri[6+1][0])//2,height2)] #poz triungi pentru piesa mancata player1
        self.puncte_triunghiuri_player2=[poz_triunghiuri[20],poz_triunghiuri[20+1],((poz_triunghiuri[20][0]+poz_triunghiuri[20+1][0])//2,height1)] #poz triungi pentru piesa mancata player2
        
        # poz  pentru piesele ajunse la finalul jocului pt player1, respectiv player2
        self.puncte_sfarsit_player1=[(self.poz_right_tabla+self.width_tabla+1,self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-1),(self.poz_right_tabla+self.width_tabla+1+self.dim_piesa,self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-1),(self.poz_right_tabla+self.width_tabla+1+self.dim_piesa//2,poz_triunghiuri[0][1]-self.dim_piesa//2)]
        self.puncte_sfarsit_player2=[(self.poz_right_tabla+self.width_tabla+1,(self.height_screen-self.height_tabla)//2+self.dim_margini),(self.poz_right_tabla+self.width_tabla+1+self.dim_piesa,(self.height_screen-self.height_tabla)//2+self.dim_margini),(self.poz_right_tabla+self.width_tabla+1+self.dim_piesa//2,poz_triunghiuri[14][1]+self.dim_piesa//2)]

        self.poz_piese=[6,6,6,6,6,8,8,8,13,13,13,13,13,24,24,1,1,12,12,12,12,12,17,17,17,19,19,19,19,19]#primele 15- player1/ urm 15- player2, pozitiile o sa fie de la 1 la 24 reprezentand triungiul respectiv,
                                                                                                        #daca val este 25-reprezinta pozitia pentru o piesa a player1 afara din tabla, daca 26-la fel dar pentru player2
                                                                                                        #daca val este 27-reprezinra pozitia de final pentru o pisa a player1, daca val este 28-la fel pentru player2
        self.UpdatePozPieseXY()                                                                         #[6,6,6,6,6,8,8,8,13,13,13,13,13,24,24,1,1,12,12,12,12,12,17,17,17,19,19,19,19,19]#

        self.piesa_aleasa=None
        self.pozitii_ultimele_piese=[]

    # resetam setarile pentru zona tablei de joc
    def Restart(self):
        self.poz_piese=[6,6,6,6,6,8,8,8,13,13,13,13,13,24,24,1,1,12,12,12,12,12,17,17,17,19,19,19,19,19]#primele 15- player1/ urm 15- player2, pozitiile o sa fie de la 1 la 24 reprezentand triungiul respectiv,
                                                                                                        #daca val este 25-reprezinta pozitia pentru o piesa a player1 afara din tabla, daca 26-la fel dar pentru player2
                                                                                                        #daca val este 27-reprezinra pozitia de final pentru o pisa a player1, daca val este 28-la fel pentru player2
        self.UpdatePozPieseXY()                                                                         #[6,6,6,6,6,8,8,8,13,13,13,13,13,24,24,1,1,12,12,12,12,12,17,17,17,19,19,19,19,19]#

        self.piesa_aleasa=None
        self.pozitii_ultimele_piese=[]
    
    # in functie de vectorul poz_piese vom pozitiona aceste piese pe tabla (coord x,y) in vectorul poz_piese_xy
    def UpdatePozPieseXY(self):
        self.poz_piese_xy=[]
        for i in range(len(self.poz_piese)):
            calc=self.poz_piese[:i].count(self.poz_piese[i])

            # vom clacula pozitia pentru a sta o piesa una peste alta ok 
            if calc<5:
                ori=0
                scad=0
            elif calc<9:
                ori=1
                scad=5
                
            elif calc<12:
                ori=2
                scad=9
            
            elif calc<14:
                ori=3
                scad=12
                
            elif calc<15:
                ori=4
                scad=14

            #daca cumva piesa este e pozitia finala atunci ele vor fi puse un apeste alta ca un teanc(poz 27,28), in rest vor forma o piramida
            if self.poz_piese[i]==25:
                self.poz_piese_xy.append((self.puncte_triunghiuri_player1[2][0],self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-self.dim_piesa//2-self.dim_piesa*(calc-scad)-(ori)*(self.dim_piesa//2)))
            elif self.poz_piese[i]==26:
                self.poz_piese_xy.append((self.puncte_triunghiuri_player2[2][0],(self.height_screen-self.height_tabla)//2+self.dim_margini+self.dim_piesa//2+self.dim_piesa*(calc-scad)+(ori)*(self.dim_piesa//2)))
            elif self.poz_piese[i]==27:
                self.poz_piese_xy.append((self.puncte_sfarsit_player1[2]))
            elif self.poz_piese[i]==28:
                self.poz_piese_xy.append(self.puncte_sfarsit_player2[2])
            elif self.poz_piese[i]<13:
                self.poz_piese_xy.append((self.puncte_triunghiuri[self.poz_piese[i]-1][2][0],self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-self.dim_piesa//2-self.dim_piesa*(calc-scad)-(ori)*(self.dim_piesa//2)))
            else:
                self.poz_piese_xy.append((self.puncte_triunghiuri[self.poz_piese[i]-1][2][0],(self.height_screen-self.height_tabla)//2+self.dim_margini+self.dim_piesa//2+self.dim_piesa*(calc-scad)+(ori)*(self.dim_piesa//2)))
    
    # returnam mutarile disponibile ale piesei
    def PiesaCuMutariDisponibile(self,rand,oponent,buton_zar_apasat,piesa,zar1,zar2):
        if buton_zar_apasat:
            mutarePosibila=[]
            if rand==0:
                if self.poz_piese[piesa]==25:
                    poz1=25
                else:
                    poz1=self.poz_piese[piesa]
                if not self.AreToatePieseleLaFinal(rand,oponent): # prin final ne referim la zona din care vom scoate de pe tabla piese
                    if zar1!=None and poz1-zar1>0 and self.poz_piese[15:].count(poz1-zar1)<=1:
                        mutarePosibila.append(poz1-zar1)
                    if zar2!=None and zar1!=zar2 and poz1-zar2>0 and self.poz_piese[15:].count(poz1-zar2)<=1:
                        mutarePosibila.append(poz1-zar2)
                else:
                    if zar1!=None:
                        if self.poz_piese[piesa]-zar1<=0:
                            mutarePosibila.append(27)
                        elif zar1!=None and poz1-zar1>0 and self.poz_piese[15:].count(poz1-zar1)<=1:
                            mutarePosibila.append(self.poz_piese[piesa]-zar1)
                    if zar2!=None:
                        if self.poz_piese[piesa]-zar2<=0:
                            mutarePosibila.append(27)
                        elif zar2!=None and zar1!=zar2 and poz1-zar2>0 and self.poz_piese[15:].count(poz1-zar2)<=1:
                            mutarePosibila.append(self.poz_piese[piesa]-zar2)
            elif rand==1: 
                if self.poz_piese[piesa]==26:
                    poz1=0
                else:
                    poz1=self.poz_piese[piesa]
                if not self.AreToatePieseleLaFinal(rand,oponent):
                    if zar1!=None and poz1+zar1<=24 and self.poz_piese[:15].count(poz1+zar1)<=1:
                        mutarePosibila.append(poz1+zar1)
                    if zar2!=None and zar1!=zar2 and poz1+zar2<=24 and self.poz_piese[:15].count(poz1+zar2)<=1:
                        mutarePosibila.append(poz1+zar2)
                else:
                    if zar1!=None:
                        if poz1+zar1>24:
                            mutarePosibila.append(28)
                        elif zar1!=None and poz1+zar1<=24 and self.poz_piese[:15].count(poz1+zar1)<=1:
                            mutarePosibila.append(poz1+zar1)
                    if zar2!=None:
                        if poz1+zar2>24:
                            mutarePosibila.append(28)
                        elif zar2!=None and zar1!=zar2 and poz1+zar2<=24 and self.poz_piese[:15].count(poz1+zar2)<=1:
                            mutarePosibila.append(poz1+zar2)
        
        return mutarePosibila

    # verificam daca toate piesele unui jucator sunt scoase de pe tabla => a castigat acest jucator
    def AreToatePieseleIanafarTableiLaSfarsit(self,rand,oponent):
        if rand==0:
            for i in range(14,-1,-1):
                if self.poz_piese[i]!=27:
                    return False
        else:
            for i in range(len(self.poz_piese)-1,14,-1):
                if self.poz_piese[i]!=28:
                    return False
        return True

    # verificam daca toate piesele unui jucator sunt in chenarul de unde se pot scoate de pe tabla (daca sunt deja scoase nu le vom lua in calcul) => poate sa scoata piese
    def AreToatePieseleLaFinal(self,rand,oponent):
        if rand==0:
            for i in range(14,-1,-1):
                if self.poz_piese[i]!=27 and not( self.poz_piese[i]>0 and self.poz_piese[i]<=6):
                    return False
        else:
            for i in range(len(self.poz_piese)-1,14,-1):
                if self.poz_piese[i]!=28 and not( self.poz_piese[i]>=19 and self.poz_piese[i]<=24):
                    return False
        return True

    # setam pozitiile ultimelor piese dintr-un triungi unde se poate face o mutare
    def PozUltimelePieseCuMutariDisponibile(self,rand,oponent,buton_zar_apasat,zar1,zar2):
        self.pozitii_ultimele_piese=[]
        if buton_zar_apasat and self.piesa_aleasa==None:
            triunghi_ultimele_piese=[]
            if rand==0:
                # daca avem cel putin o piesa "mancata" de adversar, vom prioritiza acele piese pentru a fi mutate
                if 25 in self.poz_piese[:15]:
                   for i in range(14,-1,-1):
                        if 25==self.poz_piese[i] and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                            triunghi_ultimele_piese.append(self.poz_piese[i])
                            self.pozitii_ultimele_piese.append(i)
                            break
                else:
                    for i in range(14,-1,-1):
                        if self.poz_piese[i]!=27 and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                            triunghi_ultimele_piese.append(self.poz_piese[i])
                            self.pozitii_ultimele_piese.append(i)
            elif rand==1 and oponent==0:
                # daca avem cel putin o piesa "mancata" de adversar, vom prioritiza acele piese pentru a fi mutate
                if 26 in self.poz_piese[15:]:
                    for i in range(len(self.poz_piese)-1,14,-1):
                        if 26==self.poz_piese[i] and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                            triunghi_ultimele_piese.append(self.poz_piese[i])
                            self.pozitii_ultimele_piese.append(i)
                            break
                else:
                    for i in range(len(self.poz_piese)-1,14,-1):
                        if self.poz_piese[i]!=28 and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                            triunghi_ultimele_piese.append(self.poz_piese[i])
                            self.pozitii_ultimele_piese.append(i)

    # returnam pozitiile ultimelor piese dintr-un triungi unde se poate face o mutare   
    def PozUltimelePieseCuMutariDisponibileBot(self,zar1,zar2):
        poz3=[]
        triunghi_ultimele_piese=[]
        # daca avem cel putin o piesa "mancata" de adversar, vom prioritiza acele piese pentru a fi mutate
        if 26 in self.poz_piese[15:]:
            for i in range(len(self.poz_piese)-1,14,-1):
                if 26==self.poz_piese[i] and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(1,1,True,i,zar1,zar2)!=[]:
                    triunghi_ultimele_piese.append(self.poz_piese[i])
                    poz3.append(i)
                    break
        else:
            for i in range(len(self.poz_piese)-1,14,-1):
                if self.poz_piese[i]!=28 and self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(1,1,True,i,zar1,zar2)!=[]:
                    triunghi_ultimele_piese.append(self.poz_piese[i])
                    poz3.append(i)
        return poz3


# clasa pentru interfata grafica
class GameGUI:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Backgammon Game')
        self.background_s = pygame.image.load('imagini/background1.png').convert()

        self.table=Table(self.screen,self.width,self.height)
        self.zonaZaruri=ZonaZaruri(self.screen)
    
    def DrawTable(self):
        #desenam dreptungiul pentru tabla
        pygame.draw.rect(self.screen,(210, 180, 140),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),border_radius=5)
        pygame.draw.rect(self.screen,(152, 133, 88),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),self.table.dim_margini,5)
        pygame.draw.rect(self.screen,(0, 0, 0),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),1,5)
        pygame.draw.line(self.screen,(152, 133, 88),(self.table.poz_right_tabla+self.table.width_tabla//2,(self.height-self.table.height_tabla)//2+1),(self.table.poz_right_tabla+self.table.width_tabla//2,self.height-(self.height-self.table.height_tabla)//2-2),self.table.dim_piesa)
        pygame.draw.line(self.screen,(189,183,107),(self.table.poz_right_tabla+self.table.width_tabla//2,(self.height-self.table.height_tabla)//2+1),(self.table.poz_right_tabla+self.table.width_tabla//2,self.height-(self.height-self.table.height_tabla)//2-2),5)

        #desenam triunghiurile tablei
        for i in range(len(self.table.puncte_triunghiuri)):
            if i%2==0:
                pygame.draw.polygon(self.table.screen,(255,255,255),self.table.puncte_triunghiuri[i])
            else:
                pygame.draw.polygon(self.screen,(255,0,0),self.table.puncte_triunghiuri[i])
        
        #desenam piesele pe tabla
        for i in range(len(self.table.poz_piese_xy)):
            if i<15:
                pygame.draw.circle(self.screen,(238,232,170),self.table.poz_piese_xy[i],self.table.dim_piesa//2)    
            else:
                pygame.draw.circle(self.screen,(255,99,71),self.table.poz_piese_xy[i],self.table.dim_piesa//2)

            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//2,2)
            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//4,2)

    #desenam zarul
    def DrawZarFata(self,nr_zar,x,y):
        zar_latura=60
        rect1=pygame.Rect(x,y,zar_latura,zar_latura)
        pygame.draw.rect(self.screen,(255,255,224),rect1,border_radius=5)
        pygame.draw.rect(self.screen,(0,0,0),rect1,4,5)
        if nr_zar==1:
            pygame.draw.circle(self.screen,(0,0,0),rect1.center,5)
        elif nr_zar==2:
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx,rect1.centery+15),5)
        elif nr_zar==3:
            pygame.draw.circle(self.screen,(0,0,0),rect1.center,5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery+15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery-15),5)
        elif nr_zar==4:
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery+15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery+15),5)
        elif nr_zar==5:
            pygame.draw.circle(self.screen,(0,0,0),rect1.center,5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery+15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery+15),5)
        elif nr_zar==6:
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery-15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery+15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery+15),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx-15,rect1.centery),5)
            pygame.draw.circle(self.screen,(0,0,0),(rect1.centerx+15,rect1.centery),5)


    def DrawZonaZaruri(self,rand):
        #scris sus dreptunghi
        if rand!=None:
            rand_f=pygame.font.Font(None,25)
            rand_s=rand_f.render("Rand: Player1" if rand==0 else "Rand: Player2",False,(255,255,255))
            self.screen.blit(rand_s,(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2-20))
        else:
            rand_f=pygame.font.Font(None,25)
            rand_s=rand_f.render("Dati cu zarul:",False,(255,255,255))
            self.screen.blit(rand_s,(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2-20))
        
        #dreptungi zona zaruri
        pygame.draw.rect(self.screen,(160,82,45),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2,self.width-(self.table.poz_right_tabla+self.table.width_tabla),self.zonaZaruri.height_zona_zaruri),border_radius=5)
        pygame.draw.rect(self.screen,(128,0,0),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2,self.width-(self.table.poz_right_tabla+self.table.width_tabla),self.zonaZaruri.height_zona_zaruri),5,5)
        if self.zonaZaruri.button_press:
            if self.zonaZaruri.zar1!=None:
                self.DrawZarFata(self.zonaZaruri.zar1,self.table.poz_right_tabla+self.table.width_tabla+10,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10)
            if self.zonaZaruri.zar2!=None:
                self.DrawZarFata(self.zonaZaruri.zar2,self.table.poz_right_tabla+self.table.width_tabla+10+65,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10)

        #button
        rect1=pygame.Rect(self.table.poz_right_tabla+self.table.width_tabla,self.height//2+self.zonaZaruri.height_zona_zaruri//2+2,100,30)
        pygame.draw.rect(self.screen,(184,134,11),rect1,border_radius=5)
        pygame.draw.rect(self.screen,(218,165,32),rect1,2,5)

        scris_f=pygame.font.Font(None,20)
        scris_s=scris_f.render("Zaruri",False,(255,255,255))
        scris_rect=scris_s.get_rect(center=rect1.center)
        self.screen.blit(scris_s,scris_rect)


    def DrawPieseDisponibile(self):
        if self.table.piesa_aleasa==None:
            for i in self.table.pozitii_ultimele_piese:
                pygame.draw.circle(self.screen,(0,255,0),self.table.poz_piese_xy[i],self.table.dim_piesa//2)
                pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//2,2)
                pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//4,2)

    def DrawPozitiiDisponibilePiesaAleasa(self,rand,oponent):
        if self.table.piesa_aleasa!=None:
            pygame.draw.circle(self.screen,(0,255,255),self.table.poz_piese_xy[self.table.piesa_aleasa],self.table.dim_piesa//2)
            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[self.table.piesa_aleasa],self.table.dim_piesa//2,2)
            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[self.table.piesa_aleasa],self.table.dim_piesa//4,2)
            pozitii_disp=self.table.PiesaCuMutariDisponibile(rand,oponent,self.zonaZaruri.button_press,self.table.piesa_aleasa,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
            for i in pozitii_disp:
                if i==27:
                    var=self.table.puncte_sfarsit_player1
                elif i==28:
                    var=self.table.puncte_sfarsit_player2
                else:
                    var=self.table.puncte_triunghiuri[i-1]
                pygame.draw.circle(self.screen,(0,255,0),var[2],self.table.dim_piesa//2)
                pygame.draw.circle(self.screen,(0,0,0),var[2],self.table.dim_piesa//2,2)
                pygame.draw.circle(self.screen,(0,0,0),var[2],self.table.dim_piesa//4,2)

    def Draw(self,rand,oponent):
        self.screen.blit(self.background_s,(0,0))
        self.DrawTable()
        self.DrawZonaZaruri(rand)
        self.DrawPieseDisponibile()
        self.DrawPozitiiDisponibilePiesaAleasa(rand,oponent)


    def DrawZonaCastigator(self,castigator):
        self.screen.blit(self.background_s,(0,0))
        scris_f=pygame.font.Font(None,40)
        scris_s=scris_f.render("Castigator:",False,(255,255,255))
        scris_rect=scris_s.get_rect(center=(self.width//2,self.height//2-100))
        self.screen.blit(scris_s,scris_rect)


        castigator_f=pygame.font.Font(None,60)
        castigator_s=castigator_f.render("Player1" if castigator==0 else "Player2",False,(255,215,0))
        castigator_rect=castigator_s.get_rect(center=(self.width//2,self.height//2))
        self.screen.blit(castigator_s,castigator_rect)

        #button
        rect1=pygame.Rect(self.width//2-35,self.height//2+50,70,30)
        pygame.draw.rect(self.screen,(184,134,11),rect1,border_radius=5)
        pygame.draw.rect(self.screen,(218,165,32),rect1,2,5)
        scris_buton_f=pygame.font.Font(None,15)
        scris_buton_s=scris_buton_f.render("Joc Nou",False,(255,255,255))
        scris_buton_rect=scris_buton_s.get_rect(center=rect1.center)
        self.screen.blit(scris_buton_s,scris_buton_rect)



    def DrawZonaInceput(self):
        self.screen.blit(self.background_s,(0,0))
        #Backgammon
        scris_title_f=pygame.font.Font(None,80)
        scris_title_s=scris_title_f.render("Backgammon",False,(255,255,255))
        scris_title_rect=scris_title_s.get_rect(center=(self.width//2,self.height//2-200))
        self.screen.blit(scris_title_s,scris_title_rect)

        rect1=pygame.Rect(self.width//2-200,self.height//2-35-60,400,70)
        rect2=pygame.Rect(self.width//2-200,self.height//2-35+60,400,70)
        

        #button
        pygame.draw.rect(self.screen,(184,134,11),rect1,border_radius=5)
        pygame.draw.rect(self.screen,(218,165,32),rect1,5,5)

        #button
        pygame.draw.rect(self.screen,(184,134,11),rect2,border_radius=5)
        pygame.draw.rect(self.screen,(218,165,32),rect2,5,5)

        scris_buton1_f=pygame.font.Font(None,40)
        scris_buton1_s=scris_buton1_f.render("Player1 vs Player2",False,(255,255,255))
        scris_buton1_rect=scris_buton1_s.get_rect(center=(rect1.center))
        self.screen.blit(scris_buton1_s,scris_buton1_rect)

        scris_buton2_s=scris_buton1_f.render("Player vs bot",False,(255,255,255))
        scris_buton2_rect=scris_buton2_s.get_rect(center=(rect2.center))
        self.screen.blit(scris_buton2_s,scris_buton2_rect)

#clasa pentru joc
class Game:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 800
        self.gameGui=GameGUI(self.width,self.height)
        self.clock=pygame.time.Clock()
        self.table=self.gameGui.table
        self.zonaZaruri=self.gameGui.zonaZaruri
        self.close_display = False

        self.rand=None #0-player1 1-player2
        self.oponent=None #0-uman 1-bot
        self.castigator=None
        self.inceput=False
    
    def VerificaButonApasat(self,event):
        if not self.zonaZaruri.button_press:
            rect1=pygame.Rect(self.table.poz_right_tabla+self.table.width_tabla,self.height//2+self.zonaZaruri.height_zona_zaruri//2+2,100,30)
            if rect1.collidepoint(event.pos):
                self.zonaZaruri.zar1=random.randint(1,6)
                self.zonaZaruri.zar2=random.randint(1,6)
                if self.zonaZaruri.zar1==self.zonaZaruri.zar2:
                    self.zonaZaruri.dubla=True
                    self.zonaZaruri.ramas=4
                self.zonaZaruri.button_press=True
        #verificam daca va fii vreo mutare posibila
                if self.rand!=None:
                    self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
                    if self.table.pozitii_ultimele_piese==[]:
                        self.zonaZaruri.Restart()
                        self.rand=(self.rand+1)%2

                        self.table.UpdatePozPieseXY()
                        self.table.piesa_aleasa=None
                        self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
                else:
                    if self.zonaZaruri.zar1!=self.zonaZaruri.zar2:
                        self.rand=0 if self.zonaZaruri.zar1>self.zonaZaruri.zar2 else 1
                    self.gameGui.DrawZarFata(self.zonaZaruri.zar1,self.table.poz_right_tabla+self.table.width_tabla+10,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10)
                    self.gameGui.DrawZarFata(self.zonaZaruri.zar2,self.table.poz_right_tabla+self.table.width_tabla+10,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10+65)
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.zonaZaruri.Restart()
                    
                    
    def VerificarePiesaApasata(self,event):
        self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
        for i in self.table.pozitii_ultimele_piese:
                cerc=pygame.Rect(self.table.poz_piese_xy[i][0]-self.table.dim_piesa//2,self.table.poz_piese_xy[i][1]-self.table.dim_piesa//2,self.table.dim_piesa,self.table.dim_piesa)
                if cerc.collidepoint(event.pos):
                    self.table.piesa_aleasa=i
                    

    def VerificareApasarePozitiiDisponibilePiesaApasata(self,event):
        if self.table.piesa_aleasa!=None:
            pozitii_disp=self.table.PiesaCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.table.piesa_aleasa,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
            for i in pozitii_disp:
                if i==27:
                    cerc=pygame.Rect(self.table.puncte_sfarsit_player1[2][0]-self.table.dim_piesa//2,self.table.puncte_sfarsit_player1[2][1]-self.table.dim_piesa//2,self.table.dim_piesa,self.table.dim_piesa)
                elif i==28:
                    cerc=pygame.Rect(self.table.puncte_sfarsit_player2[2][0]-self.table.dim_piesa//2,self.table.puncte_sfarsit_player2[2][1]-self.table.dim_piesa//2,self.table.dim_piesa,self.table.dim_piesa)
                else:
                    cerc=pygame.Rect(self.table.puncte_triunghiuri[i-1][2][0]-self.table.dim_piesa//2,self.table.puncte_triunghiuri[i-1][2][1]-self.table.dim_piesa//2,self.table.dim_piesa,self.table.dim_piesa)
                if cerc.collidepoint(event.pos):
                    if self.table.poz_piese[self.table.piesa_aleasa]==25:
                        poz1=25
                    elif self.table.poz_piese[self.table.piesa_aleasa]==26:
                        poz1=0
                    else:
                        poz1=self.table.poz_piese[self.table.piesa_aleasa]
                    if i!=27 and i!=28:
                        if self.zonaZaruri.zar1!=None and (poz1-i==self.zonaZaruri.zar1 or poz1-i==0-self.zonaZaruri.zar1):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar1=None
                            
                        elif self.zonaZaruri.zar2!=None and (poz1-i==self.zonaZaruri.zar2 or poz1-i==0-self.zonaZaruri.zar2):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar2=None

                    elif i==27:
                        if self.zonaZaruri.zar1!=None and (poz1-self.zonaZaruri.zar1<=0):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar1=None
                        elif self.zonaZaruri.zar2!=None and (poz1-self.zonaZaruri.zar2<=0):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar2=None
                    elif i==28:
                        if self.zonaZaruri.zar1!=None and (poz1+self.zonaZaruri.zar1>24):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar1=None
                        elif self.zonaZaruri.zar2!=None and (poz1+self.zonaZaruri.zar2>24):
                            if self.zonaZaruri.dubla:
                                if self.zonaZaruri.ramas>1:
                                    self.zonaZaruri.ramas-=1
                                else:
                                    self.zonaZaruri.Restart()
                            else:
                                self.zonaZaruri.zar2=None

                    
                    self.table.poz_piese[self.table.piesa_aleasa]=i
                    if self.table.AreToatePieseleIanafarTableiLaSfarsit(self.rand,self.oponent):
                        self.castigator=self.rand
                    
                    #dupa ce am facut mutarea verificam daca cumva pe acelasi triunghi gasim o piesa a adversarului, si o vom "manaca"
                    if self.rand==0:
                        if i in self.table.poz_piese[15:]:
                            for j in range(15,len(self.table.poz_piese)):
                                if self.table.poz_piese[j]==i:
                                    self.table.poz_piese[j]=26
                                    break
                    else:
                        if i in self.table.poz_piese[:15]:
                            for j in range(15):
                                if self.table.poz_piese[j]==i:
                                    self.table.poz_piese[j]=25
                                    break

                    if self.zonaZaruri.zar1==None and self.zonaZaruri.zar2==None:
                        self.zonaZaruri.button_press=False
                        self.rand=(self.rand+1)%2

                    
                    self.table.UpdatePozPieseXY()
                    self.table.piesa_aleasa=None
                    self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
                    if self.zonaZaruri.button_press!=False and self.table.pozitii_ultimele_piese==[]:
                        self.zonaZaruri.zar1=None
                        self.zonaZaruri.zar2=None
                        self.zonaZaruri.button_press=False
                        self.rand=(self.rand+1)%2

                        self.table.UpdatePozPieseXY()
                        self.table.piesa_aleasa=None
                        self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
                    break


    def VerificareButonNouMeciApasat(self,event):
        rect1=pygame.Rect(self.width//2-35,self.height//2+50,70,30)
        if rect1.collidepoint(event.pos):
            self.rand=None #0-player1 1-player2
            self.oponent=None #0-uman 1-bot
            self.castigator=None
            self.inceput=False
            self.table.Restart()
            self.zonaZaruri.Restart()

    def VerificareButonJocCuPlayerSauBot(self,event):
        rect1=pygame.Rect(self.width//2-200,self.height//2-35-60,400,70)
        rect2=pygame.Rect(self.width//2-200,self.height//2-35+60,400,70)
        if rect1.collidepoint(event.pos):
            self.oponent=0
            self.inceput=True
        if rect2.collidepoint(event.pos):
            self.oponent=1
            self.inceput=True

                  
    def Events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                self.close_display=True
                return True
            if self.inceput==True:
                if self.castigator==None and event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.VerificaButonApasat(event)
                    self.VerificarePiesaApasata(event)
                    self.VerificareApasarePozitiiDisponibilePiesaApasata(event)
                if self.castigator!=None and event.type==pygame.MOUSEBUTTONDOWN:
                    self.VerificareButonNouMeciApasat(event)
            else:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.VerificareButonJocCuPlayerSauBot(event)
        return False
    
    def Bot(self):
        if self.rand==1 and self.oponent==1:
            if self.zonaZaruri.zar1==None and self.zonaZaruri.zar2==None:
                self.zonaZaruri.zar1=random.randint(1,6)
                self.zonaZaruri.zar2=random.randint(1,6)
                if self.zonaZaruri.zar1==self.zonaZaruri.zar2:
                    self.zonaZaruri.dubla=True
                    self.zonaZaruri.ramas=4
                self.zonaZaruri.button_press=True
                self.gameGui.DrawZonaZaruri(self.rand)
                pygame.display.update()
            
            pygame.time.delay(500)##############################################
            poz=self.table.PozUltimelePieseCuMutariDisponibileBot(self.zonaZaruri.zar1,self.zonaZaruri.zar2)

            if poz==[]:
                self.zonaZaruri.Restart()
                self.rand=(self.rand+1)%2

                self.table.UpdatePozPieseXY()
                self.table.piesa_aleasa=None
                self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
            else:
                #alegem o piesa pe care o va muta botul
                if len(poz)>1:
                    alegere=random.randint(0,len(poz)-1)
                else:
                    alegere=0
                
                
                poz_disp_alegere=self.table.PiesaCuMutariDisponibile(1,1,True,poz[alegere],self.zonaZaruri.zar1,self.zonaZaruri.zar2)
               
               #alegem o pozitie din cele disponibele ale piesei alese
                if len(poz_disp_alegere)>1:
                    alegere2=random.randint(0,len(poz_disp_alegere)-1)
                else:
                    alegere2=0
                
                if self.table.poz_piese[poz[alegere]]==26:
                    poz1=0
                else:
                    poz1=self.table.poz_piese[poz[alegere]]
                

                if self.zonaZaruri.zar1!=None and (( poz1-poz_disp_alegere[alegere2]==0-self.zonaZaruri.zar1) or (self.table.AreToatePieseleLaFinal(1,1) and poz1+self.zonaZaruri.zar1>24)):
                    if self.zonaZaruri.dubla:
                        if self.zonaZaruri.ramas>1:
                            self.zonaZaruri.ramas-=1
                        else:
                            self.zonaZaruri.Restart()
                    else:
                        self.zonaZaruri.zar1=None
                elif self.zonaZaruri.zar2!=None and (( poz1-poz_disp_alegere[alegere2]==0-self.zonaZaruri.zar2) or (self.table.AreToatePieseleLaFinal(1,1) and poz1+self.zonaZaruri.zar2>24) ):
                    if self.zonaZaruri.dubla:
                        if self.zonaZaruri.ramas>1:
                            self.zonaZaruri.ramas-=1
                        else:
                            self.zonaZaruri.Restart()
                    else:
                        self.zonaZaruri.zar2=None
                
                self.table.poz_piese[poz[alegere]]= poz_disp_alegere[alegere2]
                if self.table.AreToatePieseleIanafarTableiLaSfarsit(self.rand,self.oponent):
                    self.castigator=self.rand
               
                #dupa ce am facut mutarea verificam daca cumva pe acelasi triunghi gasim o piesa a adversarului, si o vom "manaca"
                if poz_disp_alegere[alegere2] in self.table.poz_piese[:15]:
                    for j in range(15):
                        if self.table.poz_piese[j]==poz_disp_alegere[alegere2]:
                            self.table.poz_piese[j]=25
                            break

                if self.zonaZaruri.zar1==None and self.zonaZaruri.zar2==None:
                    self.zonaZaruri.button_press=False
                    self.rand=(self.rand+1)%2
                
                
                self.table.UpdatePozPieseXY()
                self.table.piesa_aleasa=None
                self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)
            


    def DrawGame(self):
        self.gameGui.Draw(self.rand,self.oponent)

    def Run(self):
        while not self.close_display:
            if self.Events():
                return
            if self.inceput:
                if self.castigator==None:
                    self.DrawGame()
                    pygame.display.update()
                    if self.rand!=None:
                        self.Bot()
                        self.DrawGame()
                        pygame.display.update()
                    self.clock.tick(60)
                else:
                    self.gameGui.DrawZonaCastigator(self.castigator)
                    pygame.display.update()
            else:
                self.gameGui.DrawZonaInceput()
                pygame.display.update()

#cream un joc si il pornim                
game=Game()
game.Run()