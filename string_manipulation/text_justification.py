# Python offers several functions that helps to align string. 
# It offers a way to add user specified padding instead of blank space.

# str.ljust(s, width[, fillchar])
# str.rjust(s, width[, fillchar])
# str.center(s, width[, fillchar])

# width : The width of string to expand it.
# Overall width characters string will be generated

print("==============================================")
# str = "I love python !!!"
# print("Original String",str,"\n")

#         # center( len, fillchr )
# print (str.center(40,"#"))      # 40 characters     (###########I love python !!!############)
# print (str.ljust(40,"#"))       # 40 characters     (I love python !!!#######################)
# print (str.rjust(40,"#"), "\n") # 40 characters     (#######################I love python !!!) 


# # Testing with lesser characters than string provided
# print (str.center(10,"#"))      # 18 characters     (I love python !!!)
# print (str.ljust(10,"#"))       # 18 characters     (I love python !!!)
# print (str.rjust(10,"#"))       # 18 characters     (I love python !!!)

# Printing the Hackerrank logo with ljust, rjust, center
#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 

thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    # Each time a new 'H' is added to str
    #       str.rjust(thickness-1) + 'H' + str.ljust(thickness-1)
    #               ______________    H   ______________
    #               _____________H    H   H_____________
    #               ____________HH    H   HH____________

    print((c*i).rjust(thickness-1) +  c  + (c*i).ljust(thickness-1))

# Top Pillar

# Demo
#   HHHHH   
# __HHHHH___-------------------------HHHHH
#   HHHHH   
# __HHHHH___-------------------------HHHHH
#   HHHHH   
# __HHHHH___-------------------------HHHHH
#   HHHHH   
# __HHHHH___-------------------------HHHHH
#   HHHHH   
# __HHHHH___-------------------------HHHHH
#   HHHHH   
# __HHHHH___-------------------------HHHHH

# for i in range(thickness+1):
    # 'HHHHH' center justified with thickness * 2   (5 * 2 = 10)
    # '  HHHHH   '
    # print((c*thickness).center(thickness*2))
    # print((c*thickness).center(thickness*2,"_")+(c*thickness).rjust(thickness*6,"-"))

# Actual Implementation as per HackerRank test case requirement
for i in range(thickness+1):
    # 'HHHHH' center justified with thickness * 2   (5 * 2 = 10)
    # '  HHHHH   '
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Pattern till now
#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH 

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))