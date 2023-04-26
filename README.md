# TextGenerator
Program that "predicts" which word will be next in a sentence based on statistics. A file loaded to the program should contain a huge amount of words to create a Markov chain.  

For purposes of this program, a default file is in the Github repo already. The file is called "corpus" and it contains full script from Game Of Thrones (Over 300000 words).

My program takes that file filled with words and creates bigrams from those words. It then randomly chooses a word from this file as a start of the sentence. This word must be capitalized and not contain any sentence-ending punctuations. After that, the program finds which word has the highest chance of following the starting word based on the given file. 

I.e. word 'Jon' was followed by word 'Snow' the most in the file, so it has the highest chance of being the next word in the sentence if 'Jon' is the starting word.

The program continues this algorithm for a minimum of 5 tokens, then after 5 words have been generated, if a word contains any sentence-ending punctuation, this sentence is declared as finished. 

10 pseudo-sentences are created this way.
