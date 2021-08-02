import nltk
import re
import string 

def preprocess(data): 
    """
    Split data into sentences as input for sentenpiece
    :param data: textfile
    """
    # replace \n with space
    data = data.replace('\n', ' ')
    
    # convert to lowercase and remove numbers, punctuations
    data = data.lower()
    data = re.sub(r'\d+', '', data)
    
    # replace unwanted spaces with 1 space
    data = re.sub(' +', ' ', data)
    
    tokenizer = nltk.tokenize.RegexpTokenizer(r'[^.?!]+')
    return list(map(str.strip, tokenizer.tokenize(data)))
    
def split_data(data, rate):
    """
    Split data into train set and test set
    :param data: input arry
    :param rate: ratio of test set
    """
    idx = int(len(data)*(1-rate))
    return data[:idx], data[idx:]

def write(filename, filedata):
    """
    Write text into file
    :param filename: name of the file
    :param filedata: array of senteces
    """
    with open(filename + ".txt", "w") as file:
        for line in filedata:
            file.write("".join(line) + "\n") 