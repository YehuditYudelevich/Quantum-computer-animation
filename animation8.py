import pygame
import sys
import random

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 5)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# אתחול של pygame
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Cats")
start_x, start_y = 100, 100 
spacing = 270 

# הגדרת צבעים
colors = {
    'pink': (255, 192, 203),
    'mustard_yellow': (255, 219, 88),
    'olive_green': (128, 128, 0),
    'brown': (139, 69, 19),
    'purple': (128, 0, 128),
    'green': (0, 255, 0),  
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'orange': (255, 165, 0),
    'RED': (255, 0, 0),
    'GRAY': (169, 169, 169),
    'green_ligtht': (0, 100, 0) 
}

def draw_cat(color, eyes, tail, color_s, ears_c, smile, body_width, body_height, x, y):
    ear_width, ear_height = 40, 40
    ear_offset = 50 
    # ציור אוזניים החתול
    pygame.draw.polygon(screen, ears_c, [(x + 50, y + 20), (x + (body_width / 2) - ear_offset, y - ear_height), (x + 50 + ear_width, y + 20)]) 
    pygame.draw.polygon(screen, ears_c, [(x + body_width - 50 - ear_width, y + 20), (x + body_width - (body_width / 2) + ear_offset, y - ear_height), (x + body_width - 50, y + 20)])

    # ציור גוף החתול
    pygame.draw.ellipse(screen, color, (x, y, body_width, body_height))

    # ציור זנב החתול
    tail_start = (x + body_width, y + body_height / 2) 
    tail_end = (x + body_width + 50, y + body_height - 70)  
    pygame.draw.line(screen, tail, tail_start, tail_end, 8) 

    # ציור אף החתול
    pygame.draw.polygon(screen, colors['BLACK'], [(x + (body_width / 2) - 10, y + 60), (x + (body_width / 2) + 10, y + 60), (x + (body_width / 2), y + 70)]) 
    
    # ציור חיוך החתול
    if smile == "small":
        pygame.draw.arc(screen, color_s, (x + (body_width / 2) - 15, y + 70, 30, 20), 3.14, 0, 1)
    elif smile == "medium":
        pygame.draw.arc(screen, color_s, (x + (body_width / 2) - 15, y + 70, 30, 20), 3.14, 0, 3)
    elif smile == "big":
        pygame.draw.arc(screen, color_s, (x + (body_width / 2) - 15, y + 80, 30, 30), 3.14, 0, 6)
    
    # ציור עיני החתול
    pygame.draw.ellipse(screen, eyes, (x + (body_width / 2) - 40, y + 40, 30, 30))  
    pygame.draw.ellipse(screen, eyes, (x + (body_width / 2) + 10, y + 40, 30, 30))  

    # הוספת רגליים
    pygame.draw.rect(screen, color, (x + 50, y + body_height, 20, 40))
    pygame.draw.rect(screen, color, (x + body_width - 70, y + body_height, 20, 40))

    # הוספת שפם
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) - 40, y + 70), (x + (body_width / 2) - 60, y + 60), 2)
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) - 40, y + 75), (x + (body_width / 2) - 60, y + 75), 2)
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) - 40, y + 80), (x + (body_width / 2) - 60, y + 90), 2)
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) + 40, y + 70), (x + (body_width / 2) + 60, y + 60), 2)
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) + 40, y + 75), (x + (body_width / 2) + 60, y + 75), 2)
    pygame.draw.line(screen, colors['BLACK'], (x + (body_width / 2) + 40, y + 80), (x + (body_width / 2) + 60, y + 90), 2)

def cat_generate():
    colors_list = [colors['orange'], colors['brown'], colors['GRAY']]
    eyes_list = [colors['purple'], colors['BLACK'], colors['olive_green']]
    tail_list = [colors['GRAY'], colors['brown'], colors['BLACK']]
    smile_list = [colors['brown'], colors['pink'], colors['BLACK']]
    ears_list = [colors['orange'], colors['mustard_yellow'], colors['olive_green']]
    size_smile = ['small', 'big', 'medium']
    width_list = [200, 150, 170]
    height_list = [100, 150, 130]

    caty = []
    for j in range(3):
        body = random.choice(colors_list)
        eye = random.choice(eyes_list)
        tail = random.choice(tail_list)
        smile = random.choice(smile_list)
        ear = random.choice(ears_list)
        size_s = random.choice(size_smile)
        x = start_x + j * spacing
        cat = {'color': body, 'eyes': eye, 'tail': tail, 'color_s': smile, 'ears_c': ear, 'smile': size_s, 'width': width_list[j], 'height': height_list[j], 'x': x}
        caty.append(cat)
    return caty

def main():
    # צבע הרקע למסך
    colors['PALE_TURQUOISE'] = (224, 255, 255)
    screen.fill(colors['PALE_TURQUOISE'])
    start_position=colors['RED']

    pygame.draw.rect(screen, colors['BLACK'], (50, 30, 900, 300), 8)
    start_button = Button(50, 350, 400, 70, "Superposition", colors['BLACK'], start_position)
    end_button = Button(550, 350, 400, 70, "Measurement", colors['BLACK'], start_position)
    animation_running = False
    cats_after = [
        {'color': colors['orange'], 'eyes': colors['purple'], 'tail': colors['GRAY'], 'color_s': colors['brown'], 'ears_c': colors['orange'], 'smile': 'small', 'width': 200, 'height': 100, 'x': start_x},
        {'color': colors['brown'], 'eyes': colors['BLACK'], 'tail': colors['brown'], 'color_s': colors['pink'], 'ears_c': colors['mustard_yellow'], 'smile': 'medium', 'width': 150, 'height': 150, 'x': start_x + spacing},
        {'color': colors['GRAY'], 'eyes': colors['olive_green'], 'tail': colors['BLACK'], 'color_s': colors['BLACK'], 'ears_c': colors['olive_green'], 'smile': 'big', 'width': 170, 'height': 130, 'x': start_x + 2 * spacing}
    ]

    for i, cat in enumerate(cats_after):
        x = start_x + i * spacing
        draw_cat(cat['color'], cat['eyes'], cat['tail'], cat['color_s'], cat['ears_c'], cat['smile'], cat['width'], cat['height'], x, start_y)
    start_button.draw(screen)
    end_button.draw(screen)
    pygame.display.flip()

    # הגדרת השעון
    clock = pygame.time.Clock()
    regular_fps = 10  # קצב ריענון נמוך למצב הרגיל
    animation_fps = 20  # קצב ריענון גבוה בזמן האנימציה

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    animation_running = True
                    start_button = Button(50, 350, 400, 70, "Superposition", colors['BLACK'], colors['green'])
                    end_button = Button(550, 350, 400, 70, "Measurement", colors['BLACK'], colors['RED'])
                    font=pygame.font.Font(None,30)
                    text=font.render("this is",True,colors['BLACK'])
                    screen.blit(text,(50,450))
                    
                elif end_button.is_clicked(event.pos):
                    start_button = Button(50, 350, 400, 70, "Superposition", colors['BLACK'], colors['RED'])
                    end_button = Button(550, 350, 400, 70, "Measurement", colors['BLACK'], colors['green'])
                    cats_after = [
                        {'color': colors['orange'], 'eyes': colors['purple'], 'tail': colors['GRAY'], 'color_s': colors['brown'], 'ears_c': colors['orange'], 'smile': 'small', 'width': 200, 'height': 100, 'x': start_x},
                        {'color': colors['brown'], 'eyes': colors['BLACK'], 'tail': colors['brown'], 'color_s': colors['pink'], 'ears_c': colors['mustard_yellow'], 'smile': 'medium', 'width': 150, 'height': 150, 'x': start_x + spacing},
                        {'color': colors['GRAY'], 'eyes': colors['olive_green'], 'tail': colors['BLACK'], 'color_s': colors['BLACK'], 'ears_c': colors['olive_green'], 'smile': 'big', 'width': 170, 'height': 130, 'x': start_x + 2 * spacing}
                    ]
                    animation_running = False
        
        if animation_running:
            cats_after = cat_generate()
            # קצב ריענון מהיר בזמן האנימציה
            clock.tick(animation_fps)
        else:
            # קצב ריענון נמוך במצב הרגיל
            clock.tick(regular_fps)

        colors['LIGHT_COOL_APPLE_GREEN'] =  (230, 255, 230)
        screen.fill(colors['LIGHT_COOL_APPLE_GREEN'])






        pygame.draw.rect(screen, colors['BLACK'], (50, 30, 900, 300), 8)
        for cat in cats_after:
            draw_cat(cat['color'], cat['eyes'], cat['tail'], cat['color_s'], cat['ears_c'], cat['smile'], cat['width'], cat['height'], cat['x'], start_y)
        
        start_button.draw(screen)
        end_button.draw(screen)
        font=pygame.font.Font(None,30)
        text1=font.render("In superposition, a cat exists in all possible states at any given moment,",True,colors['BLACK'])
        screen.blit(text1,(50,600))
        text2=font.render("When we perform a measurement, the cat collapses into a single state.",True,colors['BLACK'])
        screen.blit(text2,(50,630))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

# קריאה לפונקציית main אם הקובץ רץ ישירות
if __name__ == "__main__":
    main()
