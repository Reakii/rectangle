import rectangle

# Initialize Pygame and screen dimensions
rectangle.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = rectangle.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rectangle.display.set_caption('Adding image and background image')

# Load and scale images directly
background_image = rectangle.transform.scale(
    rectangle.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = rectangle.transform.scale(
    rectangle.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2 - 30))

# Initialize font, render text, and set text position
text = rectangle.font.Font(None, 36).render('Hello World ', True,
                                         rectangle.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


def game_loop():
  clock = rectangle.time.Clock()
  running = True
  while running:
    for event in rectangle.event.get():
      if event.type == rectangle.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)
    display_surface.blit(text, text_rect)

    rectangle.display.flip()
    clock.tick(30)

  rectangle.quit()


if __name__ == '__main__':
  game_loop()
