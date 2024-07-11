import pygame
import sys
import io
from button import Button
import pygame_gui
import threading
from pymongo import MongoClient
from flask import Flask, Response, render_template_string

# Initialize Pygame
pygame.init()

# MongoDB setup
client = MongoClient('mongodb+srv://shayshmaiser:PmRtpwEnX6CldTMb@players.tplziu7.mongodb.net/')
db = client["bikorotDB"]
collection = db["Users"]

# Pygame setup
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("flask_app/assets/Background.png")
pianop = pygame.image.load("flask_app/assets/GAME.png")

Ap = pygame.image.load("flask_app/assets/A.png")
Bp = pygame.image.load("flask_app/assets/B.png")
Cp = pygame.image.load("flask_app/assets/C.png")
Dp = pygame.image.load("flask_app/assets/D.png")
Ep = pygame.image.load("flask_app/assets/E.png")
Fp = pygame.image.load("flask_app/assets/F.png")
Gp = pygame.image.load("flask_app/assets/G.png")
Amajorp = pygame.image.load("flask_app/assets/AMAJOR.png")
Cmajorp = pygame.image.load("flask_app/assets/CMAJOR.png")
Dmajorp = pygame.image.load("flask_app/assets/DMAJOR.png")
Fmajorp = pygame.image.load("flask_app/assets/FMAJOR.png")
Gmajorp = pygame.image.load("flask_app/assets/GMAJOR.png")

awav = pygame.mixer.Sound("flask_app/assets/a.wav")
swav = pygame.mixer.Sound("flask_app/assets/s.wav")
dwav = pygame.mixer.Sound("flask_app/assets/d.wav")
fwav = pygame.mixer.Sound("flask_app/assets/f.wav")
gwav = pygame.mixer.Sound("flask_app/assets/g.wav")
hwav = pygame.mixer.Sound("flask_app/assets/h.wav")
jwav = pygame.mixer.Sound("flask_app/assets/j.wav")
wwav = pygame.mixer.Sound("flask_app/assets/w.wav")
ewav = pygame.mixer.Sound("flask_app/assets/e.wav")
twav = pygame.mixer.Sound("flask_app/assets/t.wav")
ywav = pygame.mixer.Sound("flask_app/assets/y.wav")
uwav = pygame.mixer.Sound("flask_app/assets/u.wav")

manager = pygame_gui.UIManager((1280, 720))
clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("flask_app/assets/font.ttf", size)

def capture_screen():  # New function to capture the Pygame display
    screen = pygame.display.get_surface()
    pygame.image.save(screen, "flask_app/static/screen.png")

def register():
    global manager
    manager = pygame_gui.UIManager((1280, 720))
    username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 200), (600, 100)), manager=manager, object_id='#username_entry')
    password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 400), (600, 100)), manager=manager, object_id='#password_entry')
    username = ""
    password = ""
    username_filled = False
    password_filled = False
    show_login_button = False

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("ENTER USERNAME", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT2 = get_font(45).render("ENTER PASSWORD", True, "White")
        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(640, 360))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)
        PLAY_TEXT3 = get_font(45).render("REGISTER", True, "White")
        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        REGISTER_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        REGISTER_BACK.changeColor(PLAY_MOUSE_POS)
        REGISTER_BACK.update(SCREEN)
        
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REGISTER_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == '#username_entry':
                    username = event.text
                    username_filled = True
                elif event.ui_object_id == '#password_entry':
                    password = event.text
                    password_filled = True

            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(SCREEN)
        
        if username and password:
            post_createuser = {"username": username, "password": password}
            collection.insert_one(post_createuser)  
            username_input.set_text("")
            password_input.set_text("")
            username = ""
            password = ""
            username_filled = False
            password_filled = False
            show_login_button = True
        if show_login_button:
            REGISTER_LOGIN = Button(image=None, pos=(640, 560), 
                                    text_input="LOGIN", font=get_font(75), base_color="White", hovering_color="Green")

            REGISTER_LOGIN.changeColor(PLAY_MOUSE_POS)
            REGISTER_LOGIN.update(SCREEN)
            UI_REFRESH_RATE = clock.tick(60) / 1000  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if REGISTER_LOGIN.checkForInput(PLAY_MOUSE_POS):
                        login()  
        pygame.display.update() 

def login():
    global manager
    manager = pygame_gui.UIManager((1280, 720))
    username_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 200), (600, 100)), manager=manager, object_id='#username_entry1')
    password_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 400), (600, 100)), manager=manager, object_id='#password_entry1')
    username = ""
    password = ""
    username_filled1 = False
    password_filled1 = False
    show_continue = False
    show_failed = False
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("ENTER USERNAME", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_TEXT2 = get_font(45).render("ENTER PASSWORD", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 360))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        PLAY_TEXT3 = get_font(45).render("LOGIN", True, "Black")
        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(1040, 660), 
                            text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_DELETE = Button(image=None, pos=(340, 660), 
                            text_input="DELETE USER", font=get_font(50), base_color="Black", hovering_color="Green")

        OPTIONS_DELETE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_DELETE.update(SCREEN)

        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_DELETE.checkForInput(OPTIONS_MOUSE_POS):
                    deleteuser()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == '#username_entry1':
                    username = event.text
                    username_filled1 = True
                elif event.ui_object_id == '#password_entry1':
                    password = event.text
                    password_filled1 = True
        
            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(SCREEN)       
        
        if username and password:
            post_login = {"username": username, "password": password}
            input_login = collection.find_one(post_login)
            username_input1.set_text("")
            password_input1.set_text("")
            username = ""
            password = ""

            if input_login:
                show_continue = True
                show_failed = False
            else:
                show_failed = True
                show_continue = False

        if show_continue:
            LOGIN_CONTINUE = Button(image=None, pos=(640, 560), 
                                    text_input="CONTINUE", font=get_font(75), base_color="Black", hovering_color="Green")
            LOGIN_CONTINUE.changeColor(OPTIONS_MOUSE_POS)
            LOGIN_CONTINUE.update(SCREEN)
            UI_REFRESH_RATE = clock.tick(60) / 1000  
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LOGIN_CONTINUE.checkForInput(OPTIONS_MOUSE_POS):
                        game()
        if show_failed: 
            LOGIN_FAILED = get_font(45).render("LOGIN FAILED", True, "Black")
            LOGIN_FAILED_RECT = LOGIN_FAILED.get_rect(center=(640, 560))
            SCREEN.blit(LOGIN_FAILED, LOGIN_FAILED_RECT)
  
        pygame.display.update()

def deleteuser():
    global manager
    manager = pygame_gui.UIManager((1280, 720))
    username_input2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 200), (600, 100)), manager=manager, object_id='#username_entry2')
    password_input2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 400), (600, 100)), manager=manager, object_id='#password_entry2')
    username = ""
    password = ""
    username_filled2 = False
    password_filled2 = False
    show_continue = False
    show_failed = False
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("ENTER USERNAME", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_TEXT2 = get_font(45).render("ENTER PASSWORD", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 360))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        PLAY_TEXT3 = get_font(45).render("DELETE USER", True, "Black")
        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == '#username_entry2':
                    username = event.text
                    username_filled2 = True
                elif event.ui_object_id == '#password_entry2':
                    password = event.text
                    password_filled2 = True
        
            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(SCREEN)       
        
        if username and password:
            post_login = {"username": username, "password": password}
            verify = collection.find_one(post_login)

            if verify:
                show_continue = True
                show_failed = False
            else:
                show_failed = True
                show_continue = False

        if show_continue:
            input_login = collection.delete_one(post_login)
            username_input2.set_text("")
            password_input2.set_text("")
            username = ""
            password = ""
            DELETED_SUCCESS = get_font(45).render("DELETED SUCCESSFULLY", True, "Black")
            DELETED_SUCCESS_RECT = DELETED_SUCCESS.get_rect(center=(640, 560))
            SCREEN.blit(DELETED_SUCCESS, DELETED_SUCCESS_RECT)
            
        if show_failed: 
            LOGIN_FAILED = get_font(45).render("DELETE FAILED", True, "Black")
            LOGIN_FAILED_RECT = LOGIN_FAILED.get_rect(center=(640, 560))
            SCREEN.blit(LOGIN_FAILED, LOGIN_FAILED_RECT)
  
        pygame.display.update()

def changePassword():
    global manager
    manager = pygame_gui.UIManager((1280, 720))
    username_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 100), (600, 100)), manager=manager, object_id='#username_entry1')
    password_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 300), (600, 100)), manager=manager, object_id='#password_entry1')
    new_password_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((340, 500), (600, 100)), manager=manager, object_id='#new_password_entry1')
    username = ""
    password = ""
    new_password = ""
    username_filled1 = False
    password_filled1 = False
    new_password_filled1 = False
    show_continue = False
    show_failed = False

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("ENTER USERNAME", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_TEXT2 = get_font(45).render("ENTER PASSWORD", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        OPTIONS_TEXT3 = get_font(45).render("ENTER NEW PASSWORD", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(640, 460))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(150, 660), 
                            text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == '#username_entry1':
                    username = event.text
                    username_filled1 = True
                elif event.ui_object_id == '#password_entry1':
                    password = event.text
                    password_filled1 = True
                elif event.ui_object_id == '#new_password_entry1':
                    new_password = event.text
                    new_password_filled1 = True
        
            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(SCREEN)       
        
        if username and password and new_password:
            post_login = {"username": username, "password": password}
            input_login = collection.find_one(post_login)
            username_input1.set_text("")
            password_input1.set_text("")
            new_password_input1.set_text("")
            username = ""
            password = ""

            if input_login:
                show_continue = True
                show_failed = False
            else:
                show_failed = True
                show_continue = False
        
        if show_continue:
            collection.update_one(post_login, {"$set": {"password": new_password}})
            username_input1.set_text("")
            password_input1.set_text("")
            new_password_input1.set_text("")
            username = ""
            password = ""
            new_password = ""
            DELETED_SUCCESS = get_font(40).render("PASSWORD CHANGED", True, "#008000")
            DELETED_SUCCESS_RECT = DELETED_SUCCESS.get_rect(center=(640, 660))
            SCREEN.blit(DELETED_SUCCESS, DELETED_SUCCESS_RECT)
        if show_failed: 
            LOGIN_FAILED = get_font(45).render("USER NOT FOUND", True, "#ff0000")
            LOGIN_FAILED_RECT = LOGIN_FAILED.get_rect(center=(640, 660))
            SCREEN.blit(LOGIN_FAILED, LOGIN_FAILED_RECT)

        pygame.display.update()

def Apiano(x, y):
    SCREEN.blit(Ap, (x, y))

def Bpiano(x, y):
    SCREEN.blit(Bp, (x, y))

def Cpiano(x, y):
    SCREEN.blit(Cp, (x, y))

def Dpiano(x, y):
    SCREEN.blit(Dp, (x, y))

def Epiano(x, y):
    SCREEN.blit(Ep, (x, y))

def Fpiano(x, y):
    SCREEN.blit(Fp, (x, y))

def Gpiano(x, y):
    SCREEN.blit(Gp, (x, y))

def Amajorpiano(x, y):
    SCREEN.blit(Amajorp, (x, y))

def Cmajorpiano(x, y):
    SCREEN.blit(Cmajorp, (x, y))

def Dmajorpiano(x, y):
    SCREEN.blit(Dmajorp, (x, y))

def Fmajorpiano(x, y):
    SCREEN.blit(Fmajorp, (x, y))

def Gmajorpiano(x, y):
    SCREEN.blit(Gmajorp, (x, y))

def game():
    A_pos_x = 2000
    A_pos_y = 2000
    B_pos_x = 2000
    B_pos_y = 2000
    C_pos_x = 2000
    C_pos_y = 2000
    D_pos_x = 2000
    D_pos_y = 2000
    E_pos_x = 2000
    E_pos_y = 2000
    F_pos_x = 2000
    F_pos_y = 2000
    G_pos_x = 2000
    G_pos_y = 2000
    Amajor_pos_x = 2000
    Amajor_pos_y = 2000
    Cmajor_pos_x = 2000
    Cmajor_pos_y = 2000
    Dmajor_pos_x = 2000
    Dmajor_pos_y = 2000
    Fmajor_pos_x = 2000
    Fmajor_pos_y = 2000
    Gmajor_pos_x = 2000
    Gmajor_pos_y = 2000

    run = True
    while run:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            SCREEN.blit(pianop, (0, 0))
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    C_pos_x = 0
                    C_pos_y = 0
                    awav.play()
                if event.key == pygame.K_s:
                    D_pos_x = 0
                    D_pos_y = 0
                    swav.play()
                if event.key == pygame.K_d:
                    E_pos_x = 0
                    E_pos_y = 0
                    dwav.play()
                if event.key == pygame.K_f:
                    F_pos_x = 0
                    F_pos_y = 0
                    fwav.play()
                if event.key == pygame.K_g:
                    G_pos_x = 0
                    G_pos_y = 0
                    gwav.play()
                if event.key == pygame.K_h:
                    A_pos_x = 0
                    A_pos_y = 0
                    hwav.play()
                if event.key == pygame.K_j:
                    B_pos_x = 0
                    B_pos_y = 0
                    jwav.play()
                if event.key == pygame.K_w:
                    Cmajor_pos_x = 0
                    Cmajor_pos_y = 0
                    wwav.play()
                if event.key == pygame.K_e:
                    Dmajor_pos_x = 0
                    Dmajor_pos_y = 0
                    ewav.play()
                if event.key == pygame.K_t:
                    Fmajor_pos_x = 0
                    Fmajor_pos_y = 0
                    twav.play()
                if event.key == pygame.K_y:
                    Gmajor_pos_x = 0
                    Gmajor_pos_y = 0
                    ywav.play()
                if event.key == pygame.K_u:
                    Amajor_pos_x = 0
                    Amajor_pos_y = 0
                    uwav.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    C_pos_x = 2000
                    C_pos_y = 2000
                if event.key == pygame.K_s:
                    D_pos_x = 2000
                    D_pos_y = 2000
                if event.key == pygame.K_d:
                    E_pos_x = 2000
                    E_pos_y = 2000
                if event.key == pygame.K_f:
                    F_pos_x = 2000
                    F_pos_y = 2000
                if event.key == pygame.K_g:
                    G_pos_x = 2000
                    G_pos_y = 2000
                if event.key == pygame.K_h:
                    A_pos_x = 2000
                    A_pos_y = 2000
                if event.key == pygame.K_j:
                    B_pos_x = 2000
                    B_pos_y = 2000
                if event.key == pygame.K_w:
                    Cmajor_pos_x = 2000
                    Cmajor_pos_y = 2000
                if event.key == pygame.K_e:
                    Dmajor_pos_x = 2000
                    Dmajor_pos_y = 2000
                if event.key == pygame.K_t:
                    Fmajor_pos_x = 2000
                    Fmajor_pos_y = 2000
                if event.key == pygame.K_y:
                    Gmajor_pos_x = 2000
                    Gmajor_pos_y = 2000
                if event.key == pygame.K_u:
                    Amajor_pos_x = 2000
                    Amajor_pos_y = 2000
        Apiano(A_pos_x, A_pos_y)
        Bpiano(B_pos_x, B_pos_y)
        Cpiano(C_pos_x, C_pos_y)
        Dpiano(D_pos_x, D_pos_y)
        Epiano(E_pos_x, E_pos_y)
        Fpiano(F_pos_x, F_pos_y)
        Gpiano(G_pos_x, G_pos_y)
        Amajorpiano(Amajor_pos_x, Amajor_pos_y)
        Cmajorpiano(Cmajor_pos_x, Cmajor_pos_y)
        Dmajorpiano(Dmajor_pos_x, Dmajor_pos_y)
        Fmajorpiano(Fmajor_pos_x, Fmajor_pos_y)
        Gmajorpiano(Gmajor_pos_x, Gmajor_pos_y)         
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        REGISTER_BUTTON = Button(image=pygame.image.load("flask_app/assets/Options Rect.png"), pos=(640, 250), 
                            text_input="REGISTER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("flask_app/assets/Play Rect.png"), pos=(640, 400), 
                            text_input="LOGIN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("flask_app/assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="CHANGE PASSWORD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [REGISTER_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REGISTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    register()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    login()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    changePassword()

        pygame.display.update()

# Flask setup
def run_game():
    while True:  # Changed from the existing game loop to this
        main_menu()  # Call your main menu or game function here
        capture_screen()  # Capture the screen after each frame update
        pygame.display.update()
        clock.tick(30)  # Capture the screen at 30 FPS

if __name__ == "__main__":
    run_game() 