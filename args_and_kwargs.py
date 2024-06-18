

def using_ags_and_kwargs(normal_aguements,*args_arguements,**kwargs_arguments):
    print(normal_aguements,args_arguements,kwargs_arguments)
    print(args_arguements[0])
    print(kwargs_arguments["ram"])

    for i in args_arguements[0]:
        print([i])

    for i ,j in kwargs_arguments.items():
        print(i,j)

    print("hii this is the me one of the best developer in the world")


list1 =("hello ","rohan","sohan","ram","mohan")
val = {"ram":"god","shiv":"destroyer","mohan":"krishna"}

using_ags_and_kwargs("sohan",list1,**val)