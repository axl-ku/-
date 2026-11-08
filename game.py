import pygame
import sys
from classes import Gamer, Prp, Vrag, Supervrag, Boss, Portal, Money, Ass, Kotya
import cpp_one
pygame.font.init()
pygame.init()
pygame.mixer.init()
def ud_fon(surface):
    surface = surface.convert_alpha()
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            r, g, b, a = surface.get_at((x, y))
            if (r > 225 and g > 225 and b > 225) or (190 < r < 210 and 190 < g < 210 and 190 < b < 210):
                surface.set_at((x, y), (0, 0, 0, 0))
    return surface
h = pygame.mixer.Sound("first_steps.mp3")
h.set_volume(0.5)
# "." - пустота, "P"-препятствие, "V"-обычный враг, "S"-супер-враг, "B"-босс, "O"-портал
plann = [[".....P..P....P.........P..O....P...V.........S.........V...P......B", "..............MMMMMMMMMMMMMMOMMM"], ["P.....P......P..S.......P.........V.............O.....V...P....V.P......B", "..............MMMMMMMMMMMMMMOMMM"]]
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = win.get_rect()
center_x = screen_rect.centerx
center_y = screen_rect.centery
total, totalvr, total_flagvr, fd, ffd, uroven = 0, 0, 1, 0, 0, 0
clock = pygame.time.Clock()
fl_pause, fl_p, fl_proig, flag, flagvr, flag2, fl_bon, fl_pho, fl_IKEA, fl_music, fl_svob, fl_menu, fl_shag, fl_lob_1 = False, False, False, False, False, False, False, False, False, False, False, False, False, False
pygame.mixer.music.load("first_steps.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
tot_IKEA = 0
fram = 90
inpt = ""
gamer = Gamer( "gaamer.png", 0, 463)
kotya = Kotya("kot.png")
pl = pygame.transform.scale(pygame.image.load("fon_les.png").convert_alpha(), (10800, 216))
ag = pygame.transform.scale(pygame.image.load("againn.png").convert_alpha(), (50, 50))
pl2 = pygame.Rect(1636, 648, 1800, 216)
fon = pygame.transform.scale(pygame.image.load("less.png"), (1536, 864))
prp = Prp((100, 216), 1000)
fon_city = pygame.transform.scale(pygame.image.load("fon_cityy.png"), (1536, 864))
fon_for_pho = pygame.transform.scale(pygame.image.load("fon_for_pho.jpg"), (1536, 864))
IKEA = pygame.transform.scale(pygame.image.load("IKEA.jpg"), (1536, 864))
lob_1 = pygame.transform.scale(pygame.image.load("lobanov_1.jpg"), (100, 80))
ass = pygame.transform.scale(pygame.image.load("ch_kv.jpg").convert(), (10800, 216))
ass.set_colorkey((255, 255, 255))
as2 = pygame.Rect(0, 648, 10800, 216)
me = pygame.transform.scale(pygame.image.load("mee.jpg").convert_alpha(), (250, 150))
tr = pygame.transform.scale(pygame.image.load("tr.jpg").convert_alpha(), (1536, 864))
tr.set_colorkey((0, 0, 0))
shr = pygame.font.SysFont('Arial', 48)
t = [{"r": prp.p2, "sx": prp.px, "stat": True, "zhiv": True}, {"r": pl2, "sx": 1636, "stat": False, "zhiv": True}]
t2 = [{"r": as2, "sx": 0, "stat": True}]
p = []
p2 = []
totalprp, total_money = 0, 0
zhzn = pygame.image.load("....jpg").convert_alpha()
ram2 = pygame.transform.scale(zhzn,((gamer.health / 27000) * 50, 20))
ram2.set_colorkey(ram2.get_at((0, 0)))
kv = pygame.transform.scale(pygame.image.load("ch_kv.jpg").convert_alpha(), (1000, 500))
kv.set_colorkey((255, 255, 255))
sl_ur = pygame.transform.scale(pygame.image.load("kn_vp.png").convert_alpha(), (75, 75))
pr_ur = pygame.transform.scale(pygame.image.load("kn_vll.png").convert_alpha(), (75, 75))
fon_city = pygame.transform.scale(pygame.image.load("fon_cityy.png"), (1536, 864))
fon_for_menu = pygame.transform.scale(pygame.image.load("fon_for_menu.png"), (1536, 864))
monney = pygame.transform.scale(pygame.image.load("many.png").convert_alpha(), (50, 50))
mon = pygame.transform.scale(pygame.image.load("монеткии.png").convert_alpha(), (1536, 864))
fd2, fdd2 = 0, 0
mf = pygame.font.SysFont('Arial', 48)
mf2 = pygame.font.SysFont('Arial', 20)
h = pygame.mixer.Sound("zhopa.ogg")
def level(plan2):
    plan = plan2[0]
    global p, p2, t, totalprp, port, port2
    for w in range(len(plan)):
        if plan[w] == "P":
            totalprp += 1
            if totalprp == 1:
                p.append(Prp((150, 416), w * 120))
            elif totalprp == 2:
                p.append(Prp((250, 416), w * 120))
            elif totalprp == 3:
                p.append(Prp((750,416), w * 120))
            elif totalprp == 4:
                p.append(Prp((200, 416), w * 120))
            elif totalprp == 5:
                p.append(Prp((700, 416), w * 120))
            elif totalprp == 6:
                p.append(Prp((700, 416), w * 120))
            t.append({"r": p[-1].p2, "sx": p[-1].px, "stat": True, "zhiv": True})
        elif plan[w] == "V":
            v = Vrag(w * 125)
            p.append(v)
            t.append({"r": v.p2, "sx": v.px, "stat": True, "t": "vr", "zhiv": True})
        elif plan[w] == "S":
            s = Supervrag(w * 120)
            p.append(s)
            t.append({"r": s.p2, "sx": s.px, "stat": True, "t": "vr", "zhiv": True})
        elif plan[w] == "B":
            b = Boss(w * 130)
            p.append(b)
            t.append({"r": b.p2, "sx": b.px, "stat": True, "t": "vr", "zhiv": True})
        elif plan[w] == "O":
            port = Portal(w * 120, "zv_pr.wav")
            p.append(port)
            t.append({"r": port.p2, "sx": port.px, "stat": True, "zhiv": True})
    plan = plan2[1]
    for w in range(len(plan)):
        if plan[w] == "P":
            p2.append(Ass((450, 416), w * 120))
            t2.append({"r": p2[-1].p2, "sx": p2[-1].px, "stat": False})
        elif plan[w] == "O":
            port2 = Portal(w * 120, "zv_pr.wav")
            p2.append(port2)
            t2.append({"r": port2.p2, "sx": port2.px, "stat": True})
        elif plan[w] == "M":
            m = Money(w * 120)
            p2.append(m)
            t2.append({"r": m.p2, "sx": m.px, "stat": True})
        elif plan[w] == "S":
            s = Supervrag(w * 120)
            p2.append(s)
            t2.append({"r": s.p2, "sx": s.px, "stat": True, "t": "vr"})
level(plann[uroven])

while True:
    if fl_menu:
        if not fl_pho or fl_pho == "tf":
            gamer.g2 = pygame.Rect(gamer.x, gamer.y, 100, 200)
            if not fl_pause:
                pygame.mixer.music.unpause()
                if not fl_bon:
                    cpp_one.cpp(t, fd)
                    keys = pygame.key.get_pressed()
                    if flag == True:
                        gamer.y -= 25
                        total += 1
                        if total == 15:
                            flag = "tf"
                    elif flag == "tf":
                        gamer.y += 25
                        total -= 1
                        if total == 0:
                            flag = False
                    if gamer.x < 930:
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            gamer.x -= 5
                        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                           gamer.x += 5
                    else:
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:                            ffd += 5
                            fd += 5
                        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            fd -= 5
                            ffd -= 5
                    if ffd < -1536:
                        ffd = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_m:
                                fl_menu = False
                                break
                            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                                flag = True
                            if event.key == pygame.K_RETURN:
                                for pp in p:
                                    if isinstance(pp, Portal) and pp.p2.colliderect(gamer.g2):
                                        fl_bon = True
                                        break
                            if event.key == pygame.K_s:
                                for pp in p:
                                    if not isinstance(pp, Prp):
                                        if gamer.g2.colliderect(pp.p2):
                                            pp.health -= gamer.uron
                                        if pp.health <= 0:
                                            if isinstance(pp, Boss):
                                                fl_pause, fl_p = True, True
                                            p.remove(pp)
                                            cpp_one.cpp_2(t, pp)
                            if event.key == pygame.K_p:
                                fl_pause = True
                                fl_pho = "tf"
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    gamer.g2.y = gamer.y
                    for pp in p:
                        if isinstance(pp, Prp):
                            if gamer.g2.colliderect(pp.p2) and flag != True:
                                gamer.y = 270
                                flag2 = True
                                break
                            if flag2 and not gamer.g2.colliderect(pp.p2):
                                flag2 = False
                                if not flag:
                                    gamer.y = 468
                        if isinstance(pp, Vrag):
                            dist = abs(pp.p2.x - gamer.x)
                            if 200 <= dist <= pp.radar:
                                if gamer.x > pp.p2.x:
                                    cpp_one.cpp_3(t, pp, '+')
                                if pp.p2.x > gamer.x:
                                    cpp_one.cpp_3(t, pp, '-')
                            elif dist <= 5:
                                cpp_one.cpp_4(t, pp)
                            if pp.p2.colliderect(gamer.g2):
                                gamer.health -= pp.uron
                                if gamer.health <= 0:
                                    fl_pause, fl_proig = True, True
                                cpp_one.cpp(t, fd)
                    win.fill((0, 0, 0))
                    win.blit(fon, (ffd - 1536, 0))
                    win.blit(fon, (ffd, 0))
                    win.blit(fon, ((ffd + 1536, 0)))
                    for pp in p:
                        if pp.zhiv:
                            win.blit(pp.p, pp.p2)
                    win.blit(pl, (fd, 648))
                    win.blit(monney, (0, 0))
                    win.blit(shr.render(str(total_money), True, (255, 255, 255)), (60, 0))
                    win.blit(gamer.g, (gamer.x, gamer.y))
                    win.blit(pygame.transform.scale(ram2, ((gamer.health / 27000) * 50, 20)), (gamer.x + 55, gamer.y + 5))
                    pygame.display.update()
                    clock.tick(fram)
                elif fl_bon:
                    cpp_one.cpp(t2, fd2)
                    keys = pygame.key.get_pressed()
                    if flag == True:
                        gamer.y -= 25
                        total += 1
                        if total == 15:
                            flag = "tf"
                    elif flag == "tf":
                        gamer.y += 25
                        total -= 1
                        if total == 0:
                            flag = False
                    if gamer.x < 930:
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            gamer.x -= 5
                        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            gamer.x += 5
                    else:
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            fdd2 += 5
                            fd2 += 5
                        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            fd2 -= 5
                            fdd2 -= 5
                    if fdd2 < -1536:
                        fdd2 = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                                flag = True
                            if event.key == pygame.K_RETURN:
                                for pp in p2:
                                    if isinstance(pp, Portal) and pp.p2.colliderect(gamer.g2):
                                        fl_bon = False
                                        break
                            if kotya.p2.colliderect(gamer.g2) and event.key == pygame.K_RETURN:
                                kotya.obsh = True
                            if event.key == pygame.K_p:
                                fl_pause = True
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    for pp in p2:
                        if isinstance(pp, Prp):
                            if gamer.g2.colliderect(pp.p2):
                                gamer.y = 270
                                flag2 = True
                                break
                            if flag2 and not gamer.g2.colliderect(pp.p2):
                                flag2 = False
                                gamer.y = 468
                        if isinstance(pp, Vrag):
                            dist = abs(pp.p2.x - gamer.x)
                            if 200 <= dist <= pp.radar:
                                if gamer.x > pp.p2.x:
                                    cpp_one.cpp(t2, pp, '+')
                                if pp.p2.x > gamer.x:
                                    cpp_one.cpp(t2, pp, '-')
                            elif dist <= 5:
                                cpp_one.cpp(t2, pp)
                            if pp.p2.colliderect(gamer.g2):
                                gamer.health -= pp.uron
                                for it in t2:
                                    if it["stat"]:
                                        it["r"].x = it["sx"] + fd2
                        if isinstance(pp, Money):
                            if pp.p2.colliderect(gamer.g2):
                                total_money += 1
                                for it in t2:
                                    if it["r"] == pp.p2:
                                        t2.remove(it)
                                p2.remove(pp)
                    win.fill((0, 0, 0))
                    win.blit(fon_city, (fdd2 - 1536, 0))
                    win.blit(fon_city, (fdd2, 0))
                    win.blit(fon_city, ((fdd2 + 1536, 0)))
                    win.blit(port2.p, (port2.p2.x, port2.p2.y + 90))
                    win.blit(kotya.k, (port2.p2.x - 240, port2.p2.y + 280))
                    win.blit(gamer.g, (gamer.x, gamer.y + 90))
                    win.blit(monney, (0, 0))
                    for pp in p2:
                        if not isinstance(pp, Portal):
                            if isinstance(pp, Money):
                               win.blit(pp.p, (pp.p2.x, pp.p2.y + 200))
                            else:
                                win.blit(pp.p, (pp.p2.x, pp.p2.y + 90))
                    win.blit(kotya.k, kotya.p2)
                    win.blit(mf.render(str(total_money), True, (255, 255, 255)), (60, 0))
                    pygame.display.update()
                    clock.tick(fram)
            else:
                if fl_p:
                    win.blit(kv, (center_x - 500, center_y - 300))
                    win.blit(pygame.font.SysFont('Arial', 56).render("Congratulations!".upper(), True, (255, 255, 255)),(center_x - 250, center_y - 150))
                    win.blit(pygame.font.SysFont("Arial", 36).render("you have won", True, (255, 255, 255)), (center_x - 120, center_y - 10))
                    win.blit(sl_ur, (center_x - 25, center_y + 50))
                    win.blit(pygame.font.SysFont('Arial', 48).render("L".upper(), True, (255, 255, 255)),(center_x - 130, center_y + 55))
                    win.blit(pr_ur, (center_x - 100, center_y + 50))
                    win.blit(pygame.font.SysFont('Arial', 52).render("R".upper(), True, (255, 255, 255)),(center_x + 50, center_y + 55))
                elif fl_proig:
                    pygame.mixer.music.pause()
                    h.play()
                    pygame.mixer.music.unpause()
                    win.blit(kv, (center_x - 500, center_y - 300))
                    win.blit(pygame.font.SysFont('Arial', 56).render("GAME OVER. YOU LOSE", True, (255, 255, 255)), (center_x - 250, center_y - 150))
                    win.blit(pygame.font.SysFont('Arial', 34).render("(tap a)", True, (255, 255, 255)),(center_x - 15, center_y))
                    win.blit(ag, (center_x, center_y - 50))
                else:
                    win.blit(kv, (center_x - 500, center_y - 300))
                    win.blit(pygame.font.SysFont('Arial', 48).render("The game is suspended".upper(), True, (255, 255, 255)), (center_x - 250, center_y - 150))
                    win.blit(pygame.font.SysFont('Arial', 32).render('press "P" to continue', True, (255, 255, 255)),(center_x - 140, center_y - 10))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            uroven -= 1
                            gamer.g2.x, fd, ffd, gamer.health, total_money = 0, 0, 0, 27000, 0
                            level(plann[uroven])
                            fl_pause, fl_p, fl_proig = False, False, False
                        if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                            flag = True
                        if event.key == pygame.K_p:
                            fl_pause = False
                        if event.key == pygame.K_l:
                            uroven += 1
                            gamer.g2.x, fd, ffd, gamer.health = 0, 0, 0, 27000
                            level(plann[uroven])
                            fl_pause, fl_p, fl_proig = False, False, False
                        if event.key == pygame.K_a:
                            gamer.g2.x, fd, ffd, gamer.health = 0, 0, 0, 27000
                            level(plann[uroven])
                            fl_pause, fl_p, fl_proig = False, False, False
                        if event.key == pygame.K_m and fl_pho == "tf":
                            fl_pho = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
                clock.tick(fram)
        else:
            win.fill((0, 0, 0))
            win.blit(fon_for_pho, (0, 0))
            win.blit(mf.render('Phoenix state activated. 06 of July 2026. \n one year ago I have died but now I am really alive', True, (217, 22, 22)), (10, 750))
            win.blit(mf2.render("чтобы вернуться в игру введи первое правило места куда попал(зна-\nками препинания, ё и заглавными пренебрегаем(Вольвач, сориииии))", True, (217, 22, 22)), (1000, 0))
            win.blit(me, (1336, 714))
            win.blit(mf2.render(inpt, True, (217, 22, 22)), (center_x - (len(inpt) * 7), center_y))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        inpt = inpt[:-1]
                    elif event.key != pygame.K_RETURN:
                        inpt += event.unicode
                    elif event.key == pygame.K_RETURN:
                        if "первое правило моей головы никто не должен знать о моей голове" == inpt:
                            fl_pho, fl_pause = False, False
                        elif "т" == inpt or "лишь утратив все до конца мы обретаем свободу" == inpt:
                            total_money = 0

                            #Свобода и Перерождение: Игра стирает ВСЕ показатели прогресса на этом уровне. Игрок буквально «утратил всё до конца». Но в этот момент девочка взлетает на крыльях ангела прямо сквозь разрушенный интерфейс, и игра переносит её на секретную локацию, которую нельзя открыть никак иначе. Ты забрала у игрока цифровой мусор (монеты), но дала ему истинную свободу.
                            fl_svob = True
                        elif "мы покупаем вещи которые нам не нужны на деньги которых у нас нет чтобы впечатлить людей которых мы не любим" == inpt:
                            fl_IKEA = True
                        elif "когда у тебя бессонница все вокруг кажется ненастоящим" == inpt:
                            fl_music = True
                        elif "если можно проснуться в другом месте если можно проснуться в другое время почему бы не проснуться другим человеком" == inpt:
                            #после ввода игрок переносится на секретный уровень с неоновыми островами. Героиня меняет свой облик на Макс Мейфилд или ангела-феникса, получая уникальные способности для прохождения бонусной локации. В финале персонаж возвращается, а новый скин сохраняется для всей игры На этом неоновом уровне музыка играет не фоном. По всей локации вместо монеток висят летающие пиксельные кассеты или значки треков.Когда героиня подбирает такой значок, трек Глеба или Кристи прямо на ходу меняется на другой (например, жесткий рок сменяется на лиричную «Аутоагрессию» или «3 минуты»), а вместе с музыкой меняется и цвет всего неонового уровня (был синий — стал ядовито-розовый или огненно-красный). Игрок сам миксует настроение уровня, пока бежит по нему.
                            fl_new = True
                        inpt = ""
            if fl_IKEA:
                win.fill((0, 0, 0)), win.blit(IKEA, (0, 0))
                win.blit(gamer.g, (1000, 650))
                win.blit(mon, (0, 864 - (tot_IKEA * 10)))
                if 864 - (tot_IKEA * 10) > 0:
                    tot_IKEA += 1
                else:
                    win.blit(mf.render('если ты не знаешь чего хочешь ты умрешь в куче того что тебе не нужно', True, (217, 22, 22)), (10, 450))
            elif fl_music:
                pass
            elif fl_svob:
                win.blit(tr, (0, 0))
                #трещены появлются на экране потом все глючит между глюками видны фотки(отрывки воспоминаний)
            pygame.display.update()
            clock.tick(fram)

    else:
        win.fill((0, 0, 0))
        win.blit(fon_for_menu, (0, 0))
        win.blit(kv, (center_x - 500, center_y - 300))
        win.blit(mf.render("MENU",True, (255, 255, 255)), (center_x - 80, center_y - 200))
        win.blit(mf.render('press "s" to start', True, (255, 255, 255)), (center_x - 150, center_y - 50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    fl_menu = True
                    pygame.event.clear()
                if event.key == pygame.K_p:
                    fl_menu, fl_pho = True, True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(fram)