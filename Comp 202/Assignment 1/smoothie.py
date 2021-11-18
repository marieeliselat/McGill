#Marie-Elise Latorre
#260981320
 
#global variables
 
#smoothie types
SMOOTHIE1_NAME = "Pineapple Banana"
SMOOTHIE2_NAME  = "Almond Basil"
SMOOTHIE3_NAME  = "Purple Surprise"
SMOOTHIE4_NAME = "Onion Toffee"
 
#smoothie cost
SMOOTHIE1_COST  = 4.99
SMOOTHIE2_COST = 6.49
SMOOTHIE3_COST  = 0.99
SMOOTHIE4_COST  = 9.99
 
#sizes name
SIZE1_NAME = "small"
SIZE2_NAME = "medium"
SIZE3_NAME = "large"
SIZE4_NAME = "galactic"
 
#size cost
SIZE1_COST  = -2.0
SIZE2_COST  = 0.0
SIZE3_COST  = 2.0
SIZE4_COST  = 100.0
 
#toppings name
TOPPING1_NAME  = "no topping"
TOPPING2_NAME  = "cinnamon"
TOPPING3_NAME  = "chocolate"
TOPPING4_NAME  = "coconut"
 
#toppings cost
TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0
 
#function to get what the user wants
def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    """
    (str, str, float, str, float, str, float, str, float) -> str
    Returns the option name corresponding to the number inputed
    
    >>> pose_question_with_costs(Which smoothie would you like?, Pineapple Banana, 4.99, Almond Basil, 6.49, Purple Surprise, 0.99, Onion Toffee, 9.99)
    Your choice (1-4): 1
    You have selected Pineapple Banana
    
    >>> pose_question_with_costs(Which smoothie would you like?, Pineapple Banana, 4.99, Almond Basil, 6.49, Purple Surprise, 0.99, Onion Toffee, 9.99)
    Your choice (1-4): cat
    You have selected 
    
    >>> pose_question_with_costs(Which size would you like?, small, -2.0, medium, 0.0, large, 2.0, galactic, 100.0)
    Your choice (1-4): 1
    You have selected small
    
    >>> pose_question_with_costs(Which topping would you like?, no topping, 0.0, cinnamon, 1.0, chocolate, 1.0, coconut, 1.0)
    Your choice (1-4): 3
    You have selected chocolate
    """
    #print the menu
    print(question)
    print("1)\t", cost1, "\t\t", option1)
    print("2)\t", cost2, "\t\t", option2)
    print("3)\t", cost3, "\t\t", option3)
    print("4)\t", cost4, "\t\t", option4)
    
    #ask user
    x = input("Your choice(1-4): " )
    if not ((x == "1" or x == "2" or x == "3" or x == "4")):
        print("Sorry, that is not a valid option")
        return " "
    
    
    x = int(x)
    
    
    #if the input is a 0 or greater than 4 or a string or is less than zero, we get "Sorry"
    if x == 0 or x > 4 or x < 0 :
        print("Sorry, that is not a valid option")
        return " "
        
        
    #return what the user asked for but in better terms    
    if x == 1:
        print("You have selected",option1)
        return option1
    elif x == 2:
        print("You have selected",option2)
        return option2
    elif x== 3:
        print("You have selected",option3)
        return option3
    else:
        
        print("You have selected",option4)
        return option4
    
    
# function to calaculate subtotal 
def calculate_subtotal(smoothie_type, smoothie_size, topping):
    """
    (str, str, str) -> float
    Returns the price of the smoothie as a floating point
    
    >>> calculate_subtotal(result, final_size, final_topping)
    Smoothie cost: $ 7.99
    
    >>> calculate_subtotal(result, final_size, final_topping)
    Smoothie cost: $ 110.99
    
    >>> calculate_subtotal(result, final_size, final_topping)
    Smoothie cost: $ 12.99
      """
    #conversion of smoothie_type to an actual name and price
    if smoothie_type == SMOOTHIE1_NAME:
        smoothie_price = SMOOTHIE1_COST 
    elif smoothie_type == SMOOTHIE2_NAME :
        smoothie_price = SMOOTHIE2_COST
    elif smoothie_type == SMOOTHIE3_NAME :
        smoothie_price = SMOOTHIE3_COST 
    elif smoothie_type == SMOOTHIE4_NAME:
        smoothie_price = SMOOTHIE4_COST 
       
    #conversion of smoothie_size to an actual name and price
    if smoothie_size == SIZE1_NAME:
        size_price = SIZE1_COST 
    elif smoothie_size == SIZE2_NAME:
        size_price = SIZE2_COST 
    elif smoothie_size == SIZE3_NAME:
        size_price = SIZE3_COST 
    elif smoothie_size == SIZE4_NAME:
        size_price = SIZE4_COST 
    
    #conversion of stoppings to an actual name and price
    if topping == TOPPING1_NAME :
        topping_price = TOPPING1_COST
    elif topping == TOPPING2_NAME :
        topping_price = TOPPING2_COST
    elif topping == TOPPING3_NAME :
        topping_price = TOPPING3_COST
    elif topping == TOPPING4_NAME :
        topping_price = TOPPING4_COST
    
    #subtotal of all the items
    z = float(round((smoothie_price + size_price + topping_price), 2))
    
    return z
    
    
 
def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    """
    (float, str, str, str) -> print (str, float, float)
    Prints order, subtotal, final total
    
    >>>print_receipt(final_subtotal, result, final_size, final_topping)
    You ordered a galactic Onion Toffee smoothie with cinnamon
    Smoothie cost: $ 110.99
    GST: 5.55
    QST: 11.07
    Total: 127.61
    
    >>>print_receipt(final_subtotal, result, final_size, final_topping)
    You ordered a small Onion Toffee smoothie with no topping
    Smoothie cost: $ 7.99
    GST: 0.4
    QST: 0.8
    Total: 9.19
    
    >>>print_receipt(final_subtotal, result, final_size, final_topping)
    You ordered a large Onion Toffee smoothie with chocolate
    Smoothie cost: $ 12.99
    GST: 0.65
    QST: 1.3
    Total: 14.94
    """
    #print order
    print("You ordered a", smoothie_size, smoothie_type, "smoothie with", topping)
    #print subtotal
    print("Smoothie cost: $", subtotal)
    
    #taxes and final total
    #GST and QST // 100
    s = 0.09975
    t = 0.05
    
    #calculations for GST and QST
    GST = round(subtotal * t, 2)
    QST = round(subtotal * s, 2)
    
    #calauclation for Total
    Total = round(subtotal + GST + QST, 2)
    
    #print results
    print("GST:",GST)
    print("QST:", QST)
    print("Total:", Total)
    return GST and QST and Total
    
 
    
def order():
    """
    () -> NoneType
    Prints greetings and gives back functions
    
    >>> order():
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothing?
    Which smoothie would you like
    1)   4.99        Pineapple Banana
    2)   6.49        Almond Basil
    3)   0.99        Purple Surprise
    4)   9.99        Onion Toffee
    Your choice(1-4): 1
    You have selected Pineapple Banana
    Unfortunately, we are out of Pineapple Banana
    You will be served Onion Toffee .
    Which size would you like
    1)   -2.0        small
    2)   0.0         medium
    3)   2.0         large
    4)   100.0       galactic
    Your choice(1-4): 4
    You have selected galactic
    Which topping would you like
    1)   0.0         no topping
    2)   1.0         cinnamon
    3)   1.0         chocolate
    4)   1.0         coconut
    Your choice(1-4): 2
    You have selected cinnamon
    You ordered a galactic Onion Toffee smoothie with cinnamon
    Smoothie cost: $ 110.99
    GST: 5.55
    QST: 11.07
    Total: 127.61
    
    >>> order():
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothing?
    Which smoothie would you like
    1)   4.99        Pineapple Banana
    2)   6.49        Almond Basil
    3)   0.99        Purple Surprise
    4)   9.99        Onion Toffee
    Your choice(1-4): 1
    You have selected Pineapple Banana
    Unfortunately, we are out of Pineapple Banana
    You will be served Onion Toffee .
    Which size would you like
    1)   -2.0        small
    2)   0.0         medium
    3)   2.0         large
    4)   100.0       galactic
    Your choice(1-4): 1
    You have selected galactic
    Which topping would you like
    1)   0.0         no topping
    2)   1.0         cinnamon
    3)   1.0         chocolate
    4)   1.0         coconut
    Your choice(1-4): 1
    You have selected cinnamon
    You ordered a small Onion Toffee smoothie with no topping
    Smoothie cost: $ 7.99
    GST: 0.4
    QST: 0.8
    Total: 9.19
    
    >>> order():
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothing?
    Which smoothie would you like
    1)   4.99        Pineapple Banana
    2)   6.49        Almond Basil
    3)   0.99        Purple Surprise
    4)   9.99        Onion Toffee
    Your choice(1-4): 7
    Sorry that is not a valid option. 
    You will be served Onion Toffee .
    Which size would you like
    1)   -2.0        small
    2)   0.0         medium
    3)   2.0         large
    4)   100.0       galactic
    Your choice(1-4): 4
    You have selected galactic
    Which topping would you like
    1)   0.0         no topping
    2)   1.0         cinnamon
    3)   1.0         chocolate
    4)   1.0         coconut
    Your choice(1-4): 2
    You have selected cinnamon
    You ordered a galactic Onion Toffee smoothie with cinnamon
    Smoothie cost: $ 110.99
    GST: 5.55
    QST: 11.07
    Total: 127.61
 
    """
    #print greetings
    print("Welcome to Smooth Smoothies Smoothie Ordering System")
    print("Have you tried our new Onion Toffee smoothing?")
    
    #ask about smoothie
    result = pose_question_with_costs("Which smoothie would you like",SMOOTHIE1_NAME,SMOOTHIE1_COST ,SMOOTHIE2_NAME , SMOOTHIE2_COST,SMOOTHIE3_NAME ,SMOOTHIE3_COST 
,SMOOTHIE4_NAME,SMOOTHIE4_COST )
    
    if result == " ":
        return
    
    #make any other result into Onion Toffee
    if result == SMOOTHIE1_NAME or result == SMOOTHIE2_NAME  or result == SMOOTHIE3_NAME :
        print("Unfortunately, we are out of", result)
    result = SMOOTHIE4_NAME  
    print("You will be served", result, ".")
    
    #ask about size
    final_size = pose_question_with_costs("Which size would you like",SIZE1_NAME,SIZE1_COST ,SIZE2_NAME, SIZE2_COST ,SIZE3_NAME,SIZE3_COST 
,SIZE4_NAME,SIZE4_COST )
    
    #ask about topping
    final_topping = pose_question_with_costs("Which topping would you like",TOPPING1_NAME ,TOPPING1_COST,TOPPING2_NAME , TOPPING2_COST,TOPPING3_NAME ,TOPPING3_COST
,TOPPING4_NAME ,TOPPING4_COST )
    
    #subtotal
    final_subtotal = calculate_subtotal(result, final_size, final_topping)
    
    #receipt
    print_receipt(final_subtotal, result, final_size, final_topping)
