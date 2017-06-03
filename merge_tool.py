def merge_the_tools(string1, k):
    # your code goes here
    word_list=list(string1)
    temp_list=[]
    for i in range(len(word_list),0,k):
        temp_list.append(word_list[i:i+k])

    print(temp_list)




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)