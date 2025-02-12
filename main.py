import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

FPS = 60
radius = 24
space = 20
A = 65

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_path = pygame.font.match_font("jokerman")
font = pygame.font.Font(font_path, 45)
WORD = pygame.font.Font(font_path, 40)
TITLE = pygame.font.Font(font_path, 70)
BUTTON = pygame.font.Font(font_path, 30)
WARNING = pygame.font.Font(font_path, 25)
ROLE = pygame.font.Font(font_path, 35)

images = []
for i in range(7):
    image = pygame.image.load(f"man{i + 1}.png")
    images.append(image)


def init_game():
    global hangman, guessed, input_mode, word, hint, input_text, error_message, letters
    letters = []
    x_start = round((WIDTH - (radius * 2 + space) * 13) / 2)
    y_start = 540

    for i in range(26):
        x = x_start + space * 2 + ((radius * 2 + space) * (i % 13))
        y = y_start + ((i // 13) * (space + radius * 2))
        letters.append([x, y, chr(A + i), True])

    hangman = 0
    guessed = []
    input_mode = 'word'
    word = ''
    hint = ''
    input_text = ''
    error_message = ''


def draw_buttons():
    proceed_button = BUTTON.render("Proceed", 1, BLACK)
    edit_button = BUTTON.render("Edit", 1, BLACK)
    proceed_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
    edit_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 160, 200, 50)
    pygame.draw.rect(win, (200, 200, 200), proceed_rect)
    pygame.draw.rect(win, (200, 200, 200), edit_rect)
    win.blit(proceed_button, (proceed_rect.x + 10, proceed_rect.y + 10))
    win.blit(edit_button, (edit_rect.x + 10, edit_rect.y + 10))
    return proceed_rect, edit_rect


def draw():
    win.fill(WHITE)

    title = TITLE.render("HANGMAN", 1, BLACK)
    win.blit(title, (WIDTH / 2 - title.get_width() / 2, 10))

    if input_mode in ['word', 'hint', 'verify']:
        role_text = ROLE.render("HOST", 1, (0, 100, 0))
    else:
        role_text = ROLE.render("PLAYER", 1, (0, 0, 139))
    win.blit(role_text, (WIDTH / 2 - role_text.get_width() / 2, 120))

    if input_mode == 'word':
        display_text = input_text.upper()
        input_label1 = WORD.render("Enter the word to guess:", 1, BLACK)
        win.blit(input_label1, (WIDTH / 2 - input_label1.get_width() / 2, HEIGHT / 2 - 60))
        input_label2 = WORD.render(display_text, 1, BLACK)
        win.blit(input_label2, (WIDTH / 2 - input_label2.get_width() / 2, HEIGHT / 2 - 10))
        warning = WARNING.render("(Should have 1-10 characters)", 1, (255, 0, 0))
        win.blit(warning, (WIDTH / 2 - warning.get_width() / 2, HEIGHT / 2 + 50))
        proceed_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
        pygame.draw.rect(win, (200, 200, 200), proceed_rect)
        proceed_text = BUTTON.render("Proceed", 1, BLACK)
        win.blit(proceed_text, (proceed_rect.x + 10, proceed_rect.y + 10))
        pygame.display.update()
        return proceed_rect, None

    elif input_mode == 'hint':
        display_text = input_text.upper()
        input_label1 = WORD.render("Enter the hint:", 1, BLACK)
        win.blit(input_label1, (WIDTH / 2 - input_label1.get_width() / 2, HEIGHT / 2 - 60))
        input_label2 = WORD.render(display_text, 1, BLACK)
        win.blit(input_label2, (WIDTH / 2 - input_label2.get_width() / 2, HEIGHT / 2 - 10))
        warning = WARNING.render("(Should have 1-40 characters)", 1, (255, 0, 0))
        win.blit(warning, (WIDTH / 2 - warning.get_width() / 2, HEIGHT / 2 + 50))
        proceed_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
        pygame.draw.rect(win, (200, 200, 200), proceed_rect)
        proceed_text = BUTTON.render("Proceed", 1, BLACK)
        win.blit(proceed_text, (proceed_rect.x + 10, proceed_rect.y + 10))
        pygame.display.update()
        return proceed_rect, None

    elif input_mode == 'verify':
        word_label = WORD.render("Word: " + word.upper(), 1, BLACK)
        hint_label = WORD.render("Hint: " + hint.upper(), 1, BLACK)
        win.blit(word_label, (WIDTH / 2 - word_label.get_width() / 2, HEIGHT / 2 - word_label.get_height()))
        win.blit(hint_label, (WIDTH / 2 - hint_label.get_width() / 2, HEIGHT / 2))
        proceed_rect, edit_rect = draw_buttons()
        pygame.display.update()
        return proceed_rect, edit_rect

    else:
        hint_label = WORD.render("Hint:", 1, BLACK)
        win.blit(hint_label, (WIDTH / 2 - hint_label.get_width() / 2, 170))
        hint_text = WORD.render(hint.upper(), 1, BLACK)
        win.blit(hint_text, (WIDTH / 2 - hint_text.get_width() / 2, 230))
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        display_word = " ".join([letter if letter in guessed else "_" for letter in word])
        text = WORD.render(display_word, 1, BLACK)
        centered_x = 490 - (text.get_width() // 2)
        win.blit(text, (centered_x, 280))

        for letter in letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(win, BLACK, (x, y), radius, 4)
                text = font.render(ltr, 1, BLACK)
                win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        win.blit(images[hangman], (50, 50))

    error_text = WORD.render(error_message, 1, (255, 0, 0))
    win.blit(error_text, (WIDTH / 2 - error_text.get_width() / 2, HEIGHT / 2 + 80))

    pygame.display.update()
    return None, None


init_game()
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    proceed_rect, edit_rect = draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if input_mode in ['word', 'hint']:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key != pygame.K_RETURN:
                    input_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if input_mode == 'word' and proceed_rect and proceed_rect.collidepoint(mouse_pos):
                if 0 < len(input_text) <= 10:
                    word = input_text.upper()
                    input_text = ''
                    input_mode = 'hint'
                    error_message = ''
                else:
                    error_message = 'Word must be 1-10 letters long.'

            elif input_mode == 'hint' and proceed_rect and proceed_rect.collidepoint(mouse_pos):
                if 0 < len(input_text) <= 40:
                    hint = input_text.upper()
                    input_text = ''
                    input_mode = 'verify'
                    error_message = ''
                else:
                    error_message = 'Hint must be 1-40 characters long.'

            elif input_mode == 'verify':
                if proceed_rect and proceed_rect.collidepoint(mouse_pos):
                    input_mode = 'game'
                elif edit_rect and edit_rect.collidepoint(mouse_pos):
                    input_mode = 'word'
                    input_text = ''
                    error_message = ''

            elif input_mode == 'game':
                mouse_x, mouse_y = mouse_pos
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dist = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if dist <= radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman += 1

    if input_mode == 'game':
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            win.fill(BLACK)
            text = WORD.render("PLAYER WON!", 1, (129, 255, 0))
            win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)
            init_game()

        if hangman == 6:
            win.fill(BLACK)
            text = WORD.render("HOST WON!", 1, (255, 0, 5))
            answer = WORD.render("THE ANSWER WAS: " + word, 1, (129, 255, 0))
            win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            win.blit(answer, (WIDTH / 2 - answer.get_width() / 2, HEIGHT / 2 + text.get_height()))
            pygame.display.update()
            pygame.time.delay(5000)
            init_game()

pygame.quit()