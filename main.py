import random

# 1. Read movies
with open("movie.txt", "r") as f:
    movies = [line.strip() for line in f]

# 2. Take first movie
for movie in movies:
    movie = movie.upper()   # uppercase easy comparison mate
        
print("Movie selected (hidden)!")

# 3. Create hidden pattern with some random characters
hidden = []
for ch in movie:
    if ch == " ":   # space hoy to space j raakhvi
        hidden.append(" ")
    else:
        # 40% letter reveal
        if random.random() < 0.4:
            hidden.append(ch)
        else:
            hidden.append("_")

print("Guess this movie by enter letters:")
print(" ".join(hidden))

# 4. User guessing loop
while "_" in hidden:
    guess = input("Enter a letter: ").upper()

    if guess in movie:
        for i in range(len(movie)):
            if movie[i] == guess:
                hidden[i] = guess
        print("Good! ", " ".join(hidden))
    else:
        print("Wrong guess! Try again.")

print("Congratulations! You guessed:", movie)

print("Thank you for playing!")