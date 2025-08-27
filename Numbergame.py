import pygame
import random
import re

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" Number Crunch")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 200, 0)
BLUE = (30, 144, 255)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 215, 0)

# Function to generate a math puzzle
def generate_puzzle():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    display_op = '×' if operator == '*' else operator
    puzzle_text = f"What is {num1} {display_op} {num2}?"
    return puzzle_text, answer

# Function to draw gradient background
def draw_gradient(surface, top_color, bottom_color):
    for y in range(screen_height):
        color_ratio = y / screen_height
        r = top_color[0] * (1 - color_ratio) + bottom_color[0] * color_ratio
        g = top_color[1] * (1 - color_ratio) + bottom_color[1] * color_ratio
        b = top_color[2] * (1 - color_ratio) + bottom_color[2] * color_ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, y), (screen_width, y))

# Main game loop
def main():
    clock = pygame.time.Clock()
    puzzle_text, correct_answer = generate_puzzle()
    user_answer = ""
    feedback = ""
    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if re.match("^-?[0-9]+$", user_answer):
                        typed_number = int(user_answer)
                        if typed_number == correct_answer:
                            feedback = "✅ Correct!"
                            score += 1
                            puzzle_text, correct_answer = generate_puzzle()
                            user_answer = ""
                        else:
                            feedback = "❌ Incorrect! Try again."
                            user_answer = ""
                    else:
                        feedback = "⚠️ Invalid input."
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode

        # Draw gradient background
        draw_gradient(screen, LIGHT_BLUE, BLUE)

        # Fonts
        title_font = pygame.font.Font(None, 64)
        puzzle_font = pygame.font.Font(None, 48)
        input_font = pygame.font.Font(None, 40)
        feedback_font = pygame.font.Font(None, 36)

        # Title
        title_surface = title_font.render("🎮 Number Crunch 🎮", True, YELLOW)
        title_rect = title_surface.get_rect(center=(screen_width // 2, 60))
        screen.blit(title_surface, title_rect)

        # Puzzle box
        pygame.draw.rect(screen, WHITE, (150, 180, 500, 80), border_radius=15)
        puzzle_surface = puzzle_font.render(puzzle_text, True, BLACK)
        puzzle_rect = puzzle_surface.get_rect(center=(screen_width // 2, 220))
        screen.blit(puzzle_surface, puzzle_rect)

        # Input box
        pygame.draw.rect(screen, WHITE, (250, 300, 300, 60), border_radius=10)
        user_input_surface = input_font.render(user_answer, True, BLACK)
        user_input_rect = user_input_surface.get_rect(center=(screen_width // 2, 330))
        screen.blit(user_input_surface, user_input_rect)

        # Feedback
        color = GREEN if "Correct" in feedback else RED
        feedback_surface = feedback_font.render(feedback, True, color)
        feedback_rect = feedback_surface.get_rect(center=(screen_width // 2, 420))
        screen.blit(feedback_surface, feedback_rect)

        # Score
        score_surface = feedback_font.render(f"Score: {score}", True, YELLOW)
        score_rect = score_surface.get_rect(center=(screen_width // 2, 500))
        screen.blit(score_surface, score_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()