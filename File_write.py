def main():
    f=open("foo.txt", "w+")
    for i in range(10):
        f.write("this is line %d \n"%(i+1))
    f.close()
def main1():
    try:
        f=open("foo.txt", "r+")
        x=f.readlines()
    except IOError:
        print ("File not found")
    else:
        for line in x:
            print (line)
        f.close()
if __name__=='__main__':
    #main()
    main1()

