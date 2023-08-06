import pygame.time
import Main_menu_screen as Ms
import Background as Bg
import resultscreen as res
status = 1
status, exitb, e2 = Ms.main_menu(status)
print(status)
while status:
    size, screen,boo, R, BA= Bg.background(exitb)
    print("Now Showing REsults")
    status = res.disp_result(screen, size, back=BA, pad=R ,button_sprite=e2, theend=boo)

print("USER EXITED!!")
exit(0)
