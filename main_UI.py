import pygame
import sys
from time import sleep

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('N-Queens Visualization')


WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
FONT = pygame.font.Font(None, 32)

def get_input():
    input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    start_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 60, WIDTH // 2, 50)  
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    button_color = pygame.Color('lightsalmon')  
    color = color_inactive
    active = False
    text = ''
    start_game = False  

    while not start_game:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                if start_button.collidepoint(event.pos):
                   
                    if text.isdigit():
                        start_game = True  
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        txt_surface = FONT.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

     
        start_txt_surface = FONT.render('Start', True, WHITE)
        pygame.draw.rect(screen, button_color, start_button)
        screen.blit(start_txt_surface, (start_button.x + 20, start_button.y + 10))

        pygame.display.flip()

    return int(text) if text.isdigit() else 5  

def main(queen_img):
    global N, BLOCK_SIZE 
    N = get_input() 
    speed = 0.1
    BLOCK_SIZE = WIDTH // N

    def draw_board(n):
        for i in range(n):
            for j in range(n):
                rect = pygame.Rect(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, WHITE if (i + j) % 2 == 0 else BLACK, rect)

    def draw_queens(board, queen_img):
        queen_img = pygame.transform.scale(queen_img, (BLOCK_SIZE, BLOCK_SIZE))  
        for col, row in enumerate(board):
            if row != -1:
                queen_rect = queen_img.get_rect()
                queen_rect.topleft = (col * BLOCK_SIZE, row * BLOCK_SIZE)
                screen.blit(queen_img, queen_rect)
    def is_valid(board, row, col):
        for i in range(col):
            if board[i] == row or abs(board[i] - row) == abs(i - col):
                return False
        return True

    def solve_n_queens():
        board = [-1] * N
        if not solve_n_queens_util(board, 0):
            print("Solution does not exist")
            return []
        return board

    def solve_n_queens_util(board, col):
            if col >= N:
                return True

            for i in range(N):
                if is_valid(board, i, col):
                    board[col] = i
                    draw_board(N)
                    draw_queens(board, queen_img)  
                    pygame.display.flip()
                    # sleep(speed)  # Delay to visualize the placement

                    if solve_n_queens_util(board, col + 1):
                        return True

                    board[col] = -1  # Backtrack
                    draw_board(N)
                    draw_queens(board, queen_img) 
                    pygame.display.flip()
                    # sleep(speed)  # Delay to visualize the backtracking

            return False






    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_board(N)
        solution = solve_n_queens()
        draw_queens(solution, queen_img)  
        pygame.display.flip()
        sleep(2) 
      
        filename = f"   {N}X{N}_final_solution.png"  
        pygame.image.save(screen, filename.strip()) 

        running = False 

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    queen_img = pygame.image.load("queen_img.png")  
    main(queen_img)
