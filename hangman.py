import random
import hangman_art
import hangman_word

print(hangman_art.logo)
# list of word

chosen_word = random.choice(hangman_word.word_list)     #randomly choose a word from list
print(chosen_word)
lives = 6

display = []
for i in range(len(chosen_word)):
    display += "_"


end_of_letter=False
while not end_of_letter:
    guess = input('Guess a Letter: ').lower()

    if guess in display:
       print(f"you have already guessed {guess}")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
           display[i]=chosen_word[i]

    if guess not in chosen_word:
       
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          end_of_letter = True
          print("you loose!")
          print("word is: {}".format(chosen_word))
      print(hangman_art.stages[lives])

    print(''.join(display))
 
    if "_" not in display:
       end_of_letter=True
       print("You win!")
    