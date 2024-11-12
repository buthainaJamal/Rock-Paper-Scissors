import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)

choices = ["rock", "paper", "scissors"]

button_width, button_height = 150, 50
rock_button = pygame.Rect(50, 300, button_width, button_height)
paper_button = pygame.Rect(225, 300, button_width, button_height)
scissors_button = pygame.Rect(400, 300, button_width, button_height)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def game_loop():
    running = True
    player_choice = None
    computer_choice = None
    result_text = ""

    while running:
        screen.fill(WHITE)

        pygame.draw.rect(screen, GREEN, rock_button)
        pygame.draw.rect(screen, GREEN, paper_button)
        pygame.draw.rect(screen, GREEN, scissors_button)

        rock_text = font.render("Rock", True, BLACK)
        paper_text = font.render("Paper", True, BLACK)
        scissors_text = font.render("Scissors", True, BLACK)
        screen.blit(rock_text, (rock_button.x + 30, rock_button.y + 10))
        screen.blit(paper_text, (paper_button.x + 30, paper_button.y + 10))
        screen.blit(scissors_text, (scissors_button.x + 30, scissors_button.y + 10))

        if player_choice:
            player_label = font.render(f"Player: {player_choice.capitalize()}", True, BLACK)
            screen.blit(player_label, (50, 50))

        if computer_choice:
            computer_label = font.render(f"Computer: {computer_choice.capitalize()}", True, BLACK)
            screen.blit(computer_label, (400, 50))

        result_surface = font.render(result_text, True, RED if "win" in result_text else BLACK)
        screen.blit(result_surface, (SCREEN_WIDTH // 2 - result_surface.get_width() // 2, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rock_button.collidepoint(event.pos):
                    player_choice = "rock"
                elif paper_button.collidepoint(event.pos):
                    player_choice = "paper"
                elif scissors_button.collidepoint(event.pos):
                    player_choice = "scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    result_text = determine_winner(player_choice, computer_choice)

        pygame.display.flip()

game_loop()