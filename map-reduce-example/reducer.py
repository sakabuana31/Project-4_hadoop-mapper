import sys

# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    #output : Brazil

    #split input strings to 2 vars by tab
    word, count = line.split('\t', 1)
    #word : Brazil
    #count : 1

    #convert to interger for summary step
    try:
        count = int(count)
        #count = 1 as interger
    except ValueError:
        continue

    #checking antara current word dan word selanjutnya
    if current_word == word:
        #Brazil == Brazil
        current_count += count
        #current count = i + n
    else:
        #step ini tidak akan berjalan ketika current word dan word selanjutnya tidak sama / none
        #current_word = None
        if current_word:
            print('%s\t%s' % (current_word, current_count))
            #brazil = 3

            current_count = count
            #current word = 1
            current_word = word
            #current word = Indonesia
        else:
            current_count = count
            current_word = word

if current_word == word:
    print('%s\t%s' % (current_word, current_count))
