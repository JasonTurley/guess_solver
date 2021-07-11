"""
solver.py - An automated Guessing Game solver built with pwntools framework.
"""

from pwn import *

# Pretty colors
class colors:
	RED     = "\033[31m"
	BLUE    = "\033[34m"
	YELLOW  = "\033[93m"
	END 	= "\033[0m"


# Values used to calculate guess
low = 1
high = 1000

# Only show errors
context.log_level = "error"

# Let's us interact with the guessing game script
io = process("./guessing_game.py")

# Read the first line of text, which is the intro
print(io.readline().decode().strip())

while True:
	# Read the guess prompt
	io.readuntil("Enter your guess: ")

	# Binary search style method to generate the next guess
	mid = int((high + low) / 2)
	print(colors.BLUE + "solver: " + colors.END, end="")
	print(f"Attempting guess {mid}")

	# Send guess
	io.sendline(str(mid))

	# Read response (Too Low, Too High, or Correct)
	resp = io.readline()

	# Convert to string and strip off the newline
	resp = resp.decode().strip()

	# Update our next guess
	if resp == "Too Low":
		low = mid + 1
		print(colors.RED + resp + colors.END)

	elif resp == "Too High":
		high = mid - 1
		print(colors.RED + resp + colors.END)

	else:
		# Print the correct number
		print(colors.BLUE + "solver: " + colors.END, end="")
		print(colors.YELLOW + f"The correct number is {mid}" + colors.END)

		# Read the win messages and exit
		print(io.readuntil("tries.").decode().strip())

		break
