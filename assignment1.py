




#a list that contains months
month_year=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
# variable to control my loop
x=True
while x is True:
    
    #getting input from the user
    #since the user can mispell or input a wrong name for a month, I added try and except to prevent that my program break
    # I converted my user input into a way that will make easier to write conditional statement
    b=True
    while b==True:
        try:
                print('enter the month name')
                user_month_input=input('>>>')
                print('enter the number of the days of the month')
                user_day_input= int(input('>>>'))
                
                user_month_input=user_month_input.upper()
        
           
                if month_year.index(user_month_input)>=0:
                    if user_day_input<=31 and user_day_input>0:
                       break
    
        except:
                    print('you mispelt the month name or the number of days exceeds 31')
    
     #the loop for is going to help me to iterate through the list of months I created.

    for i in month_year:
             
          if i==user_month_input:
                
                        
                if (month_year.index(i)==2 and user_day_input>=20) or month_year.index(i)==3 or  month_year.index(i)==4 or (month_year.index(i)== 5 and user_day_input < 21):
                    print(f' the season in {i.lower()} is Spring')
                elif (month_year.index(i)==5 and user_day_input>=20) or month_year.index(i)==6 or  month_year.index(i)==7 or (month_year.index(i)== 5 and user_day_input < 22):
                    print(f' the season in {i.lower()} is Summer')
                elif (month_year.index(i)==11 and user_day_input>=21) or  month_year.index(i)==0 or month_year.index(i)== 1 or (month_year.index(i)== 2 and user_day_input < 20):
                    print(f' the season in {i.lower()} is Winter')
                elif (month_year.index(i)==8 and user_day_input>=22) or month_year.index(i)==9 or  month_year.index(i)>=10 :
                    print(f' the season in {i.lower()} is Fall')
          
    #since there is a loop, I added an option that would help a user to quit the program
        
    print()    
    print('Do you want to stop the program, if Yes, press Y if not, press any key')
    user_option=input('>>>')
    if user_option.upper()=='Y':
       x=False
    else:
       continue
    
    
    
                

        



