import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = screen.get_window_size()

hitbox_width = width / 2 #half the screen
hitbox_height = height / 2 #half the screen
#2 halves make quarter

hitboxes = {
    "red": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "purple": pygame.Rect(0, 0, hitbox_width, hitbox_height),    
}

#rectangles do not track visuals

hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].topright
hitboxes["purple"].topleft = hitboxes["red"].topright

font = pygame.font.Font(None, 24)

#state
done = False
result = []
turns = 0


keys = hitboxes.keys()
order = list(keys)

#Mainloop
## each time through the while is one frame
while not done:
    #respond to events
    for event in pygame.event.get(): #gets all events since the last call
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order)
                turns = len(order)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns -= 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):
                result.append("purple")
        
    if turns == 0:
        if result == order:
            font.render("You win!", True, "white")
        else:
            font.render("You win!", True, "white")