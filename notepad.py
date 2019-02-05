import pygame
import time

# Get current milliseconds
def get_millis():
    return int(round(time.time() * 1000))

# Main program function
def main():
    pygame.init()

    # Pygame essential variables
    size = (500, 700)
    display = pygame.display.set_mode(size, pygame.RESIZABLE)
    clock = pygame.time.Clock()

    # Font related variables
    font_size = 18
    font = pygame.font.SysFont('Arial', font_size)
    bold = False

    # Variables to store and index the text
    lines = [""]
    line_index = 0

    # Cursor variables
    current_time = get_millis()
    show_cursor = True

    # Main program loop
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            # Quit Handling
            if event.type == pygame.QUIT:
                running = False
                break
            # Key input
            elif event.type == pygame.KEYDOWN:
                # Delete character
                if event.key == pygame.K_BACKSPACE:
                    if lines[line_index] == "" and line_index != 0:
                        del lines[line_index]
                        line_index -= 1
                    else:
                        lines[line_index] = lines[line_index][:-1]
                # Make new line
                elif event.key == pygame.K_RETURN:
                    line_index += 1
                    if line_index == len(lines):
                        lines.append("")
                elif event.key == pygame.K_UP:
                    if line_index > 0:
                        line_index -= 1
                elif event.key == pygame.K_DOWN:
                    if line_index < len(lines) - 1:
                        line_index += 1
                # Write text
                else:
                    lines[line_index] += event.unicode
                show_cursor = True
                current_time = get_millis()
            # Mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Change line index base on mouse position
                mouse_pos = pygame.mouse.get_pos()
                line_index = mouse_pos[1] // font_size
                if line_index >= len(lines):
                    line_index = len(lines) - 1
            # Update display when user resizes it
            elif event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        # Rendering
        display.fill((255, 255, 255))
        for i in range(len(lines)):
            text_render = font.render(lines[i], bold, (0,0,0))
            display.blit(text_render, (5, font_size * i))
            if show_cursor and line_index == i:
                cursor_rect = pygame.Rect(text_render.get_width() + 5, line_index * font_size, 1, font_size)
                pygame.draw.rect(display, (0,0,0), cursor_rect)
        if get_millis() - current_time >= 500:
            show_cursor = not show_cursor
            current_time = get_millis()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
main()
