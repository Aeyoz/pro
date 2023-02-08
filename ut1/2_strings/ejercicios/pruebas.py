# Metodo 1

song = '''You look so beautiful in this light
# Your silhouette over me
# The way it brings out the blue in your eyes
# Is the Tenerife sea
# And all of the voices surrounding us here
# They just fade out when you take a breath
# Just say the word and I will disappear
# Into the wilderness'''
# 
# new_song = ""
# 
# for i in song.split():
#     if i != "voices":
#         new_song += i + " "
#     elif i == "voices":
#         new_song += "sounds "
# 
# print(new_song)

## Calculo de la longitud de una cadena de texto

# Metodo 2

# song2 = song.split("voices")
# new_song = song2[0] + "sounds" + song2[1]
#
# print("\n" + new_song.strip() + "\n")

# Metodo 3

keyword = "voices"
replace_word = "sounds"

word_index = song.find(keyword)
keyword_legth = len(keyword)
word_end_index = word_index + keyword_legth

song_part1 = song[:word_index]
song_part2 = song[word_end_index:]
new_song = song_part1 + replace_word + song_part2

print(new_song)