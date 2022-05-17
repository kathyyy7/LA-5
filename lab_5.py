
"""""
The program is trying to translate a sentence captured as user input.
We first need to read in the text file textese.txt
Then from the text file, we first create a dictionary from the text file.
Then, we create a dictionary the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which evolves splitting the user input (sentence)
into an array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight]

Once we have the array of strings representing the user's input sentence, we loop through
each words, find the key matching the word and returns back the value tied to the word
in our dictionary.

After each word is translated, we then
Print out the translated sentence to the user.

"""""

"""""

Main():
  set dictionary = translate()
  translate(sentence, dictionary)


translate(sentence, dictionary):
   word = for each of the word in the sentence
   for each words, translate the word
   print translated sentence to user

create_dictionary():
   read in textese.txt
   create list = each line from file
   close the file
   create a dict off of the list
   return the dict
   
main()

"""""

def main():
    sentence = "enjoy the excellent band tonight"
    dictionary = create_dictionary("Textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

    # #print("words", words)
    # translation = {}
    # dict([word,split(",")for word in words]):
    #     [k,v] = word.split(",")
    #     translation[k] = v
    # #print(translation)
    # return translation

    # return {
    #     "tonight":"2nite",
    #     "late":"18"
    # }

    def translate(sentence, dictionary):
        #print("From translate", sentence)
        words = sentence.split()
        for word in words:
            print(dictionary.get(word, word), " ", end="")

main()

