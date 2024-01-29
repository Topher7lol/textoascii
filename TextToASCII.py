import pyfiglet

def text_to_ascii_art(input_text):
    ascii_art = pyfiglet.figlet_format(input_text)
    return ascii_art

# What The Fuck Are You Converting It To
user_input = input("Enter Text To Convert To ASCII Art: ")

# Convert The Crap To ASCII
ascii_result = text_to_ascii_art(user_input)

# Print The ASCII
print(ascii_result)
# I Don't Mean To Offend Anyone With My Swears Boo Hoo