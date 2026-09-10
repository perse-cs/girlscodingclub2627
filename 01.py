import random
import pygame


WIDTH = 760
HEIGHT = 520
HUD_HEIGHT = 64

BACKGROUND = (15, 23, 42)
PLAY_AREA = (30, 41, 59)
WHITE = (241, 245, 249)
GREY = (148, 163, 184)
BLUE = (59, 130, 246)
BLUE_LIGHT = (147, 197, 253)
YELLOW = (250, 204, 21)
GREEN = (34, 197, 94)
BOX_FILL = (51, 65, 85)

PLAYER_SIZE = 30
PLAYER_SPEED = 260
BOX_WIDTH = 96
BOX_HEIGHT = 70


class Player(pygame.sprite.Sprite):
    """A small player sprite that can move around the play area."""

    def __init__(self, centre):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            BLUE_LIGHT,
            (PLAYER_SIZE // 2, PLAYER_SIZE // 2),
            PLAYER_SIZE // 2,
        )
        pygame.draw.circle(
            self.image,
            BLUE,
            (PLAYER_SIZE // 2, PLAYER_SIZE // 2),
            PLAYER_SIZE // 2,
            4,
        )
        self.rect = self.image.get_rect(center=centre)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def move(self, keys, seconds, boundary):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1

        # Diagonal movement should not be faster than horizontal movement.
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707

        self.x += dx * PLAYER_SPEED * seconds
        self.y += dy * PLAYER_SPEED * seconds
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        self.rect.clamp_ip(boundary)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


def random_boxes(play_boundary):
    """Make five separated target boxes at random positions."""
    boxes = []

    while len(boxes) < 5:
        left = random.randint(play_boundary.left, play_boundary.right - BOX_WIDTH)
        top = random.randint(play_boundary.top, play_boundary.bottom - BOX_HEIGHT)
        candidate = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)

        # The inflated rectangles leave a small travelling gap between boxes.
        if not any(candidate.inflate(18, 18).colliderect(box) for box in boxes):
            boxes.append(candidate)

    return boxes


def random_player_centre(play_boundary, boxes):
    """Choose a starting place that is not already inside a target."""
    while True:
        centre = (
            random.randint(
                play_boundary.left + PLAYER_SIZE // 2,
                play_boundary.right - PLAYER_SIZE // 2,
            ),
            random.randint(
                play_boundary.top + PLAYER_SIZE // 2,
                play_boundary.bottom - PLAYER_SIZE // 2,
            ),
        )
        player_rect = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
        player_rect.center = centre
        if not any(player_rect.colliderect(box) for box in boxes):
            return centre


def draw_centred_text(screen, text, font, colour, centre):
    picture = font.render(text, True, colour)
    screen.blit(picture, picture.get_rect(center=centre))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Run: 1 to 5")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 25)
large_font = pygame.font.Font(None, 62)

play_boundary = pygame.Rect(0, HUD_HEIGHT, WIDTH, HEIGHT - HUD_HEIGHT)
start_button = pygame.Rect(265, 265, 230, 68)

game_state = "waiting"
boxes = []
player = None
next_box = 0
start_ticks = 0
final_time = 0.0

running = True
while running:
    seconds = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        elif (
            game_state == "waiting"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and start_button.collidepoint(event.pos)
        ):
            boxes = random_boxes(play_boundary)
            player = Player(random_player_centre(play_boundary, boxes))
            next_box = 0
            start_ticks = pygame.time.get_ticks()
            game_state = "playing"

    if game_state == "playing":
        player.move(pygame.key.get_pressed(), seconds, play_boundary)
        elapsed = (pygame.time.get_ticks() - start_ticks) / 1000

        # contains(), unlike colliderect(), requires the WHOLE player to fit.
        if boxes[next_box].contains(player.rect):
            next_box += 1
            if next_box == len(boxes):
                final_time = elapsed
                game_state = "finished"
    elif game_state == "finished":
        elapsed = final_time
    else:
        elapsed = 0.0

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, PLAY_AREA, play_boundary)

    timer_text = font.render(f"Time: {elapsed:.2f} s", True, WHITE)
    screen.blit(timer_text, (18, 18))

    if game_state == "waiting":
        draw_centred_text(
            screen,
            "BOX RUN",
            large_font,
            WHITE,
            (WIDTH // 2, 175),
        )
        pygame.draw.rect(screen, BLUE, start_button, border_radius=12)
        pygame.draw.rect(screen, BLUE_LIGHT, start_button, 3, border_radius=12)
        draw_centred_text(
            screen,
            "Start game",
            font,
            WHITE,
            start_button.center,
        )
        draw_centred_text(
            screen,
            "Move fully inside boxes 1, 2, 3, 4 and 5",
            small_font,
            GREY,
            (WIDTH // 2, 375),
        )
    else:
        if game_state == "finished":
            progress_message = "All boxes complete!"
        else:
            progress_message = f"Next box: {next_box + 1}"
        progress_text = font.render(progress_message, True, WHITE)
        screen.blit(progress_text, (WIDTH - 175, 18))

        for index, box in enumerate(boxes):
            if index < next_box:
                border_colour = GREEN
                fill_colour = (20, 83, 45)
            elif index == next_box and game_state == "playing":
                border_colour = YELLOW
                fill_colour = BOX_FILL
            else:
                border_colour = GREY
                fill_colour = BOX_FILL

            pygame.draw.rect(screen, fill_colour, box, border_radius=8)
            pygame.draw.rect(screen, border_colour, box, 4, border_radius=8)
            draw_centred_text(
                screen,
                str(index + 1),
                font,
                border_colour,
                box.center,
            )

        screen.blit(player.image, player.rect)

        if game_state == "finished":
            result_panel = pygame.Rect(155, 187, 450, 145)
            pygame.draw.rect(screen, BACKGROUND, result_panel, border_radius=16)
            pygame.draw.rect(screen, GREEN, result_panel, 4, border_radius=16)
            draw_centred_text(
                screen,
                "Finished!",
                large_font,
                WHITE,
                (WIDTH // 2, 230),
            )
            draw_centred_text(
                screen,
                f"Final time: {final_time:.2f} seconds",
                font,
                GREEN,
                (WIDTH // 2, 294),
            )

    pygame.display.flip()

pygame.quit()
