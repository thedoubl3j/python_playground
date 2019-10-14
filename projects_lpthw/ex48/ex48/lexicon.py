# using a dict for the lexicon, easiest way. 

lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    3: 'number',
    91234: 'number'
    }

 
# function that is going to scan the lexicon
def scan(sentence):

    words = sentence.split()
    # this is the tuple that the test wants. function will drop the lexicon key: values into it. 
    result = []
    
    for word in words:
        check_string = convert_numbers(word) # we need this to convert (if it can) a string to integer with conver_numbers() function
                                             
        
        if word in lexicon: 
            
            check_number = convert_numbers(word) 
            # we need this one for examples like assert_equal(lexicon.scan("1234"), [('number', 1234)])
            #if there is an integer in the tuple ,instead of a string like most of them in the exercise(a little 'trap' by Zed)
            #in the convert_numbers() funtion if the string cant be return as int it will be return as string again so no worries.
            pair = (lexicon[word], check_number) #pairs the two final words in a tuple ...
            result.append(pair) #...so that it can return the tuple in a list.
				
        
        elif type(check_string) == type(1): #we check if the type of the variable check_string is int ,and if it is then we proceede.
            
            number = convert_numbers(word)
            if number:
                
                pair = ('number' , number) #pretty much the same as above only here we put the string 'number' directly in the tuple
                result.append(pair)
        else:
          #this is the tricky part(not hard tho) this final if-statement looks if a word is missing from our dict
          #and if it is missing it counts as error
            error_word = word
            pair = ('error', error_word)
            result.append(pair)
                
    return result

# Simple converter found in the book. This looks at our string and tries to see if it can be an int, if not, it goes on as a string.    
def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return s
        