def timeconversion(s):
    a=s.split(":")
    if  a[2][-2:] == "PM":
        a[0]=str(int(a[0])+12)

    a[2]=a[2][0:2]
    z=":".join(a)
    print(z)

if __name__ == '__main__':


    s = input()

    result = timeconversion(s)