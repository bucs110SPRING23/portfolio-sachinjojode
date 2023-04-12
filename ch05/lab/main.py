import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit + 1):
        count = threenp1(i)
        objs_in_sequence[i] = count
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict, window):
    coordinates = list(threenplus1_iters_dict.items())
    print(coordinates)
    max_count = max(coordinates, key=lambda x: x[1])
    pygame.draw.lines(window, "blue", False, coordinates)
    width, height = window.get_size()
    new_display = pygame.transform.scale(window, (width * 5, height * 5))
    window.blit(new_display, (0,0))
    new_display = pygame.transform.flip(window, False, True)
    window.blit(new_display, (0,0))
    font = pygame.font.Font(None, 42)
    msg = font.render("Max Count: " + str(max_count[0]), False, "white", "black")
    window.blit(msg, (10, 10))
    pygame.display.flip()

def main():
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    pygame.display.flip()
    graph_coordinates(threenp1range(20), window)
    pygame.time.wait(10000)

main()
