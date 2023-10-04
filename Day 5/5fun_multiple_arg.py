def person(name,**data):  #Here the dubble star means you are passing the multiple arguments with the keywords & the first one is mendotory
    print(name)
    print(data)
    for i,j in data.items(): # i is for the index & the j is for the value
        print(i,j)

person("Nihir",age="23",workplace="Rajkot",hometown="Rajkot",phone="123456789",homenu="4567891123",image="c://downloads/user.png",twiiter="htps://twi.com")