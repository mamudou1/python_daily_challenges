a="this is it"
print(a.upper())
# a.lowe() for lowe case
#a.strip() to remove white space
# a.replace("t","m") 
#slit()


#concatenation
b="it is all well "
print()
c=a+" "+b
print(c)

# format
height=str(23)
wrd="his height is" +" "+ height
wr="we mean this one {}"
print(wrd)
#using  formate
print(wr.format(height))
#more on format
x=23
y=34
z=34
xx="this {} is a {} by {}"
print(xx.format(x,y,z))

#escape characters

txt="we shall see said \"maka\" and so"
print(txt)