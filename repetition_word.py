# Ask user to enter a word, a separator and number of repetitions. Write a Python code displaying the word with repetition times and having each word separated with separator character. For example, if user entered word as Tina, separator as ! and repetitions as 3 expected output is "Tina!Tina!Tina" Be careful there is no separator character at the end.


word = input("Please enter your word ypu want to repeat : " )
separator = input("Please enter your separetor : ")
time = input("Please enter your repetition number : ")

def repeat(word, separator, time) :
    sentence = ""
    for i in range(int(time)) :
        if i == int(time) -1:
            sentence += word
        else :
            sentence += (word + separator)
    return sentence

repeat(word, separator, time)
