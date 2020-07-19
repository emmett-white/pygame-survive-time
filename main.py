# SA-MP Survive Time Application


# Import
import pygame
import pyautogui as pygui
import subprocess
import os


pygame.init()


# Global variables
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 350
DISPLAY_CAPTION = 'SA-MP: Survive Time'

stIcon = pygame.image.load('./images/st-icon.png')

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_icon(stIcon)
pygame.display.set_caption((DISPLAY_CAPTION))

pygame.display.flip()

# Colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
ORANGE_CORAL = [255, 127, 80]
DARK_GREEN = [21, 176, 16]

# Background color
screen.fill(WHITE)


app_logo = pygame.image.load('./images/st-logo.png')
app_logo = pygame.transform.scale(app_logo, (300, 200))
app_logo.convert()

app_logo_rect = app_logo.get_rect()
app_logo_rect.center = ((DISPLAY_WIDTH // 2), (DISPLAY_HEIGHT - 190))


# Labels
titleFont = pygame.font.SysFont('Calibri', 28, True, True)
titleFont.set_underline(1)

title = titleFont.render('San Andreas Multiplayer', True, (BLACK))

# Play - Exit Labels
font_btn = pygame.font.SysFont('Calibri', 22, True, False)

playFont = font_btn.render('PLAY', True, (BLACK))
exitFont = font_btn.render('EXIT', True, (WHITE))


# Functions
def find_files(filename, search_path):
	result = []

	for root, dir, files in os.walk(search_path):
		if filename in files:
			result.append(os.path.join(root, filename))


	return result


# Enter samp.exe location
location = pygui.prompt(text = 'In which partition is your samp.exe located? (e.g C:/ or D:/)', title = 'samp.exe location' , default = '')


# Run game
runningGame = True

while runningGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runningGame = False


		# Click on image
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos

			if play_btn.collidepoint(x, y):
				subprocess.Popen(find_files('samp.exe', (location)))

				# Show message box with server ip and port
				pygui.alert('CLICK ON \"Servers\" > \"Add server\" and enter ip: \"localhost:7777\".', 'Survive Time - IP Address')


			elif exit_btn.collidepoint(x, y):
				runningGame = False


	screen.blit(app_logo, app_logo_rect)
	screen.blit(title,
		((200 - title.get_width() // 2), (title.get_height() // 2)))


	# Buttons
	play_btn = pygame.draw.rect(screen, ORANGE_CORAL, (90, 280, 100, 50))
	exit_btn = pygame.draw.rect(screen, DARK_GREEN, (215, 280, 100, 50))


	# Play button coordinates
	screen.blit(playFont,
		((140 - playFont.get_width() // 2), (305 - playFont.get_height() // 2)))


	# Exit button coordinates
	screen.blit(exitFont,
		((265 - exitFont.get_width() // 2), (305 - exitFont.get_height() // 2)))


	pygame.display.update()


pygame.quit()
quit()
