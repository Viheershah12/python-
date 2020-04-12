

  
# long_word = "juxtaposition"
# first = long_word.index("t")
# last = long_word.rfind("t")
# print(long_word[first:last+1])

quote = "they who stumble run fast"
start = 0
end = 25
space_index = quote.find(" ")
while space_index != -1:
    quote = "they who stumble run fast"
    print(quote[start:space_index])
    start += space_index
    print(start)
    #space_index = quote.find(" ",start,end)
    #print(quote[4:8])
    # print(space_index)


input()


