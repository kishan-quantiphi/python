def lsort(words, order): 
    Order_index = {order[i]: i for i in range(len(order))} 
    for i in range(len(words) - 1): 
        word1 = words[i] 
        word2 = words[i + 1] 
        for k in range(min(len(word1), len(word2))): 
            if word1[k] != word2[k]: 
                if Order_index[word1[k]] > Order_index[word2[k]]:
                    words[i],words[i+1]=words[i+1],words[i]
                break
            else: 
                if len(word1) > len(word2): 
                    words[i],words[i+1]=words[i+1],words[i]
                break
                
                    
  
    return words


order = ['r','c','t','a']
inp = ['car','rat','cat']
print(lsort(inp,order))