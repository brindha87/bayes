# ------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#
from __future__ import division

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]

def NextWordProbability(sampletext, word):
    all_words = sampletext.split(" ")
    w_dictionary = {}
    for i in range(len(all_words)):
        if all_words[i] == word:
            if all_words[i+1] not in w_dictionary.keys():
                w_dictionary[all_words[i+1]] = 0
            w_dictionary[all_words[i+1]] += 1
            i+=1

    return w_dictionary

def LaterWords(sample, word, distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    w1_dict = {}
    w1_dict = NextWordProbability(sample, word)
    p1_dict = {}
    word1_total = sum(w1_dict.values())
    for i in w1_dict:
        p1_dict[i] = w1_dict[i]/word1_total

    w2 = {}
    p2 = {}
    p2_dict = {}
    for k1, v1 in p1_dict.items():
        w2 = NextWordProbability(sample, k1)
        w2_total = sum(w2.values())
        for i in w2:
            p2[i] = w2[i]/w2_total
        for k2, v2 in p2.items():
            p = v1*v2
            if k2 not in p2_dict.keys():
                p2_dict[k2] = p
            else:
                p2_dict[k2] += p


    #finding the word2 which has max probability
    max_prob = 0
    probable_word2 = ""
    for k,v in p2_dict.items():
        if v > max_prob:
            max_prob = v
            probable_word2 = k

    return probable_word2



    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.


print "Word 2 is :"
print LaterWords(sample_memo, "ahead", 2)