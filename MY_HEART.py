import math
import random
import sys
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart & Particles Effect")

BG_COLOR = (10, 10, 20)
FONT_COLOR = (255, 180, 200)

glow_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
text_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(BG_COLOR)


class Particle:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.delay = random.randint(0, 50)
    self.alpha = 0
    self.flicker = random.random() * 10
    self.size_mult = random.uniform(1.0, 2.0)
    self.color = FONT_COLOR
    self.font = pygame.font.SysFont("Arial", 24)
    self.word = "love"


def draw_glow_text(surface_glow, surface_text, font, word, color, x, y, alpha, size_mult):
   text_surface = font.render(word, True, color)
   text_surface.set_alpha(alpha)
   text_rect = text_surface.get_rect(center=(x, y))
   surface_text.blit(text_surface, text_rect)



particles = []
num_particles = 45

for i in range(num_particles):
  t = (i / num_particles) * 2 * math.pi

  x_offset = 16 * (math.sin(t) ** 3) * 14
  y_offset = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3*t) - math.cos(4*t)) * 14

  heart_x = int(WIDTH // 2 + x_offset)
  heart_y = int(HEIGHT // 2 - y_offset)

  particles.append(Particle(heart_x, heart_y))

frame = 0
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False

  screen.blit(background, (0, 0))
  glow_layer.fill((0, 0, 0, 0))
  text_layer.fill((0, 0, 0, 0))

  frame += 1

  for p in particles:
    if frame > p.delay and p.alpha < 255:
      p.alpha = min(255, p.alpha + 14 + random.randint(0, 4))
    if p.alpha >= 255:
      flick = 0.75 + 0.25 * math.sin(frame * 0.04 + p.flicker)
    else:
      flick = 1.0
    alpha = int(p.alpha * flick)
    if alpha <= 0:
      continue
    draw_glow_text(glow_layer, text_layer, p.font, p.word, p.color, p.x, p.y, alpha, p.size_mult)

  screen.blit(glow_layer, (0, 0))
  screen.blit(text_layer, (0, 0))

  pygame.display.flip()
  pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()