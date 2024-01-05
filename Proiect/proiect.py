import pygame
import random

class ZonaZaruri:
    def __init__(self,screen):
        self.screen=screen
        self.height_zona_zaruri=200
        self.zar1=None
        self.zar2=None
        self.button_press=False


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

        poz_triunghiuri=[(self.dim_margini+self.poz_right_tabla+i*self.dim_piesa, self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-1) for i in range(13,-1,-1)]
        for i in range(14):
            poz_triunghiuri.append((self.dim_margini+self.poz_right_tabla+i*self.dim_piesa,(self.height_screen-self.height_tabla)//2+self.dim_margini))

        self.puncte_triunghiuri=[]
        height1=self.height_screen//2-self.dim_piesa//2
        height2=self.height_screen//2+self.dim_piesa//2
        for i in range(len(poz_triunghiuri)-1):
            if i != 6 and i!=20 and i!=13:
                if i<13:
                    self.puncte_triunghiuri.append([poz_triunghiuri[i],poz_triunghiuri[i+1],((poz_triunghiuri[i][0]+poz_triunghiuri[i+1][0])//2,height2)])
                else:
                    self.puncte_triunghiuri.append([poz_triunghiuri[i],poz_triunghiuri[i+1],((poz_triunghiuri[i][0]+poz_triunghiuri[i+1][0])//2,height1)])  

        self.poz_piese=[6,6,6,6,6,8,8,8,13,13,13,13,13,24,24,1,1,12,12,12,12,12,17,17,17,19,19,19,19,19]#primele 15- player1/ urm 15- player2, pozitiile o sa fie de la 1 la 24 reprezentand triungiul respectiv, 0 daca e afara si va urma sa il punem pe tabla, -1 daca am ajuns la final pentu piesa noastra
        self.UpdatePozPieseXY()

        self.piesa_aleasa=None
        self.pozitii_ultimele_piese=[]

    def UpdatePozPieseXY(self):
        self.poz_piese_xy=[]
        for i in range(len(self.poz_piese)):
            calc=self.poz_piese[:i].count(self.poz_piese[i])
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

            if self.poz_piese[i]<13:
                self.poz_piese_xy.append((self.puncte_triunghiuri[self.poz_piese[i]-1][2][0],self.height_tabla+(self.height_screen-self.height_tabla)//2-self.dim_margini-self.dim_piesa//2-self.dim_piesa*(calc-scad)-(ori)*(self.dim_piesa//2)))
            else:
                self.poz_piese_xy.append((self.puncte_triunghiuri[self.poz_piese[i]-1][2][0],(self.height_screen-self.height_tabla)//2+self.dim_margini+self.dim_piesa//2+self.dim_piesa*(calc-scad)+(ori)*(self.dim_piesa//2)))
    
    def PiesaCuMutariDisponibile(self,rand,oponent,buton_zar_apasat,piesa,zar1,zar2):
        if buton_zar_apasat:
            mutarePosibila=[]
            if rand==0:
                if zar1!=None and self.poz_piese[piesa]-zar1>0 and self.poz_piese[15:].count(self.poz_piese[piesa]-zar1)<=1:
                    mutarePosibila.append(self.poz_piese[piesa]-zar1)
                if zar2!=None and zar1!=zar2 and self.poz_piese[piesa]-zar2>0 and self.poz_piese[15:].count(self.poz_piese[piesa]-zar2)<=1:
                    mutarePosibila.append(self.poz_piese[piesa]-zar2)
            elif rand==1 and oponent==0:
                if zar1!=None and self.poz_piese[piesa]+zar1<=24 and self.poz_piese[:15].count(self.poz_piese[piesa]+zar1)<=1:
                    mutarePosibila.append(self.poz_piese[piesa]+zar1)
                if zar2!=None and zar1!=zar2 and self.poz_piese[piesa]+zar2<=24 and self.poz_piese[:15].count(self.poz_piese[piesa]+zar2)<=1:
                    mutarePosibila.append(self.poz_piese[piesa]+zar2)
        
        return mutarePosibila


    def PozUltimelePieseCuMutariDisponibile(self,rand,oponent,buton_zar_apasat,zar1,zar2):
        self.pozitii_ultimele_piese=[]
        if buton_zar_apasat and self.piesa_aleasa==None:
            triunghi_ultimele_piese=[]
            if rand==0:
                for i in range(14,-1,-1):
                    if self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                        triunghi_ultimele_piese.append(self.poz_piese[i])
                        self.pozitii_ultimele_piese.append(i)
            elif rand==1 and oponent==0:
                for i in range(len(self.poz_piese)-1,14,-1):
                    if self.poz_piese[i] not in triunghi_ultimele_piese and self.PiesaCuMutariDisponibile(rand,oponent,buton_zar_apasat,i,zar1,zar2)!=[]:
                        triunghi_ultimele_piese.append(self.poz_piese[i])
                        self.pozitii_ultimele_piese.append(i)
            



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
        pygame.draw.rect(self.screen,(210, 180, 140),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),border_radius=5)

        for i in range(len(self.table.puncte_triunghiuri)):
            if i%2==0:
                pygame.draw.polygon(self.table.screen,(255,255,255),self.table.puncte_triunghiuri[i])
            else:
                pygame.draw.polygon(self.screen,(255,0,0),self.table.puncte_triunghiuri[i])
        
        for i in range(len(self.table.poz_piese_xy)):
            if i<15:
                pygame.draw.circle(self.screen,(238,232,170),self.table.poz_piese_xy[i],self.table.dim_piesa//2)    
            else:
                pygame.draw.circle(self.screen,(255,99,71),self.table.poz_piese_xy[i],self.table.dim_piesa//2)

            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//2,2)
            pygame.draw.circle(self.screen,(0,0,0),self.table.poz_piese_xy[i],self.table.dim_piesa//4,2)

        pygame.draw.rect(self.screen,(152, 133, 88),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),self.table.dim_margini,5)
        pygame.draw.rect(self.screen,(0, 0, 0),(self.table.poz_right_tabla,(self.height-self.table.height_tabla)//2,self.table.width_tabla,self.table.height_tabla),1,5)
        pygame.draw.line(self.screen,(152, 133, 88),(self.table.poz_right_tabla+self.table.width_tabla//2,(self.height-self.table.height_tabla)//2+1),(self.table.poz_right_tabla+self.table.width_tabla//2,self.height-(self.height-self.table.height_tabla)//2-2),self.table.dim_piesa)
        pygame.draw.line(self.screen,(189,183,107),(self.table.poz_right_tabla+self.table.width_tabla//2,(self.height-self.table.height_tabla)//2+1),(self.table.poz_right_tabla+self.table.width_tabla//2,self.height-(self.height-self.table.height_tabla)//2-2),5)
    

    def DrawZonaZaruri(self):
        pygame.draw.rect(self.screen,(160,82,45),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2,self.width-(self.table.poz_right_tabla+self.table.width_tabla),self.zonaZaruri.height_zona_zaruri),border_radius=5)
        pygame.draw.rect(self.screen,(128,0,0),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2-self.zonaZaruri.height_zona_zaruri//2,self.width-(self.table.poz_right_tabla+self.table.width_tabla),self.zonaZaruri.height_zona_zaruri),5,5)
        if self.zonaZaruri.button_press:
            zar1f=pygame.font.Font(None,20)
            zar1_s=zar1f.render(str(self.zonaZaruri.zar1),False,(0,255,0))
            zar2f=pygame.font.Font(None,20)
            zar2_s=zar2f.render(str(self.zonaZaruri.zar2),False,(0,255,0))
            self.screen.blit(zar1_s,(self.table.poz_right_tabla+self.table.width_tabla+10,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10))
            self.screen.blit(zar2_s,(self.table.poz_right_tabla+self.table.width_tabla+10,self.height//2-self.zonaZaruri.height_zona_zaruri//2+10+10+1))

        #button
        pygame.draw.rect(self.screen,(0,0,255),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2+self.zonaZaruri.height_zona_zaruri//2+2,100,30),border_radius=5)
        pygame.draw.rect(self.screen,(0,255,255),(self.table.poz_right_tabla+self.table.width_tabla,self.height//2+self.zonaZaruri.height_zona_zaruri//2+2,100,30),5,5)

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
                pygame.draw.circle(self.screen,(0,255,0),self.table.puncte_triunghiuri[i-1][2],self.table.dim_piesa//2)
                pygame.draw.circle(self.screen,(0,0,0),self.table.puncte_triunghiuri[i-1][2],self.table.dim_piesa//2,2)
                pygame.draw.circle(self.screen,(0,0,0),self.table.puncte_triunghiuri[i-1][2],self.table.dim_piesa//4,2)



    def Draw(self,rand,oponent):
        self.screen.blit(self.background_s,(0,0))
        self.DrawTable()
        self.DrawZonaZaruri()
        self.DrawPieseDisponibile()
        self.DrawPozitiiDisponibilePiesaAleasa(rand,oponent)

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

        self.rand=0 #0-player1 1-player2
        self.oponent=0 #0-uman 1-bot
    
    def VerificaButonApasat(self,event):
        if not self.zonaZaruri.button_press:
            rect1=pygame.Rect(self.table.poz_right_tabla+self.table.width_tabla,self.height//2+self.zonaZaruri.height_zona_zaruri//2+2,100,30)
            if rect1.collidepoint(event.pos):
                self.zonaZaruri.zar1=random.randint(1,6)
                self.zonaZaruri.zar2=random.randint(1,6)
                self.zonaZaruri.button_press=True

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
                cerc=pygame.Rect(self.table.puncte_triunghiuri[i-1][2][0]-self.table.dim_piesa//2,self.table.puncte_triunghiuri[i-1][2][1]-self.table.dim_piesa//2,self.table.dim_piesa,self.table.dim_piesa)
                if cerc.collidepoint(event.pos):
                    if self.zonaZaruri.zar1!=None and (self.table.poz_piese[self.table.piesa_aleasa]-i==self.zonaZaruri.zar1 or self.table.poz_piese[self.table.piesa_aleasa]-i==0-self.zonaZaruri.zar1):
                        self.zonaZaruri.zar1=None
                    elif self.zonaZaruri.zar2!=None and (self.table.poz_piese[self.table.piesa_aleasa]-i==self.zonaZaruri.zar2 or self.table.poz_piese[self.table.piesa_aleasa]-i==0-self.zonaZaruri.zar2):
                        self.zonaZaruri.zar2=None
                    if self.zonaZaruri.zar1==None and self.zonaZaruri.zar2==None:
                        self.zonaZaruri.button_press=False
                        self.rand=(self.rand+1)%2
                    self.table.poz_piese[self.table.piesa_aleasa]=i
                    self.table.UpdatePozPieseXY()
                    self.table.piesa_aleasa=None
                    self.table.PozUltimelePieseCuMutariDisponibile(self.rand,self.oponent,self.zonaZaruri.button_press,self.zonaZaruri.zar1,self.zonaZaruri.zar2)

                    
    def Events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                self.close_display=True
                return True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.VerificaButonApasat(event)
                self.VerificarePiesaApasata(event)
                self.VerificareApasarePozitiiDisponibilePiesaApasata(event)

        return False
    def DrawGame(self):
        self.gameGui.Draw(self.rand,self.oponent)

    def Run(self):
        while not self.close_display:
            if self.Events():
                return
            self.DrawGame()
            pygame.display.update()
            self.clock.tick(60)

game=Game()
game.Run()