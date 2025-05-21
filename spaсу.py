import pygame
import random
import sqlite3

pygame.init()

# Окно
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Цвета и шрифт
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 36)

# Загрузка изображений
player_img = pygame.image.load("images.png")
player_img = pygame.transform.scale(player_img, (60, 60))

enemy_img = pygame.image.load("spaceship_red.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

# Игрок
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 60))
player_speed = 5

# Пули и враги
bullets = []
bullet_speed = 7
enemies = []

# Игровые переменные
score = 0
level = 1
enemy_speed = 2
game_state = "menu"
paused = False
username = ""
input_active = False
show_scores = True

# БД
conn = sqlite3.connect('game_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, score INTEGER)''')
conn.commit()

clock = pygame.time.Clock()


def draw_text(text, x, y, color=WHITE, center=False):
    render = font.render(text, True, color)
    rect = render.get_rect(topleft=(x, y))
    if center:
        rect = render.get_rect(center=(x, y))
    screen.blit(render, rect)


def save_score(username, score):
    cursor.execute('INSERT INTO users (username, score) VALUES (?, ?)', (username, score))
    conn.commit()


def get_top_scores(limit=5):
    cursor.execute('SELECT username, score FROM users ORDER BY score DESC LIMIT ?', (limit,))
    return cursor.fetchall()


def restart_game():
    global bullets, enemies, score, level, player_rect, show_scores
    bullets = []
    enemies = []
    score = 0
    level = 1
    player_rect.centerx = WIDTH // 2
    show_scores = True


def spawn_enemy():
    x = random.randint(0, WIDTH - 50)
    enemy = enemy_img.get_rect(topleft=(x, -50))
    enemies.append(enemy)


def move_enemies():
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)


def handle_collisions():
    global score, game_state, show_scores
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    for enemy in enemies:
        if enemy.colliderect(player_rect):
            save_score(username if username else "Player", score)
            game_state = "game_over"
            show_scores = True


def draw_input_box():
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 150, 150, 300, 40), 2)
    text_surface = font.render(username, True, WHITE)
    screen.blit(text_surface, (WIDTH // 2 - 140, 155))


def main():
    global score, level, enemy_speed, game_state, paused, username, input_active, show_scores

    running = True

    while running:
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()

        if game_state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if WIDTH // 2 - 100 < mx < WIDTH // 2 + 100 and 300 < my < 350:
                        if username.strip() != "":
                            game_state = "difficulty"
                    elif WIDTH // 2 - 100 < mx < WIDTH // 2 + 100 and 370 < my < 420:
                        running = False
                    elif WIDTH // 2 - 150 < mx < WIDTH // 2 + 150 and 150 < my < 190:
                        input_active = True
                    else:
                        input_active = False
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif len(username) < 15 and event.unicode.isprintable():
                        username += event.unicode

            draw_text("SPACE SHOOTER", WIDTH // 2, 50, center=True)
            draw_text("Enter your name:", WIDTH // 2, 120, center=True)
            draw_input_box()
            pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, 300, 200, 50))
            pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, 370, 200, 50))
            draw_text("Start Game", WIDTH // 2, 315, center=True)
            draw_text("Exit", WIDTH // 2, 385, center=True)

        elif game_state == "difficulty":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if WIDTH // 2 - 100 < mx < WIDTH // 2 + 100:
                        if 250 < my < 300:
                            enemy_speed = 1.5
                            restart_game()
                            game_state = "playing"
                        elif 320 < my < 370:
                            enemy_speed = 2.5
                            restart_game()
                            game_state = "playing"
                        elif 390 < my < 440:
                            enemy_speed = 3.5
                            restart_game()
                            game_state = "playing"

            draw_text("Choose Difficulty", WIDTH // 2, 180, center=True)
            pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, 250, 200, 50))
            pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, 320, 200, 50))
            pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, 390, 200, 50))
            draw_text("Easy", WIDTH // 2, 265, center=True)
            draw_text("Medium", WIDTH // 2, 335, center=True)
            draw_text("Hard", WIDTH // 2, 405, center=True)

        elif game_state == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10)
                        bullets.append(bullet)
                    elif event.key == pygame.K_p:
                        game_state = "paused"

            if keys[pygame.K_LEFT] and player_rect.left > 0:
                player_rect.x -= player_speed
            if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
                player_rect.x += player_speed

            for bullet in bullets[:]:
                bullet.y -= bullet_speed
                if bullet.bottom < 0:
                    bullets.remove(bullet)

            if random.random() < 0.02 * level:
                spawn_enemy()
            move_enemies()
            handle_collisions()

            screen.blit(player_img, player_rect)
            for bullet in bullets:
                pygame.draw.rect(screen, WHITE, bullet)
            for enemy in enemies:
                screen.blit(enemy_img, enemy)

            draw_text(f"Score: {score}", 10, 10)
            draw_text(f"Level: {level}", WIDTH - 150, 10)

        elif game_state == "paused":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    game_state = "playing"
            draw_text("PAUSED - Press C to Continue", WIDTH // 2, HEIGHT // 2, center=True)

        elif game_state == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_state = "menu"
                    elif event.key == pygame.K_ESCAPE:
                        running = False

            screen.fill(BLACK)
            draw_text("Game Over", WIDTH // 2, 100, center=True)
            draw_text(f"Your Score: {score}", WIDTH // 2, 150, center=True)

            if show_scores:
                top_scores = get_top_scores()
                show_scores = False

            draw_text("Top Scores:", WIDTH // 2, 220, center=True)
            for i, (user, s) in enumerate(top_scores):
                draw_text(f"{i + 1}. {user} - {s}", WIDTH // 2, 250 + i * 30, center=True)

            draw_text("Press R to Restart or ESC to Quit", WIDTH // 2, HEIGHT - 40, center=True)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    conn.close()


if __name__ == "__main__":
    main()
