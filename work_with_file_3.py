def cook_book_creation(f):
    cook_book={}
    the_flag = 0
    number_of_ingredients = 0
    dish_name = ''
    list_of_ing = []
    for line in f:
        if the_flag == 0:
            dish_name = line
            list_of_ing = []
            the_flag = 1
        elif the_flag == 1:
            number_of_ingredients = int(line)
            the_flag = 2
        elif number_of_ingredients > 0:
            dic_of_ing={}
            ingredient_name, quantity, measure = line.strip().split('|')
            dic_of_ing['ingredient_name']=ingredient_name
            dic_of_ing['quantity'] = quantity
            dic_of_ing['measure'] = measure
            list_of_ing.append(dic_of_ing)
            number_of_ingredients -= 1
        else:
            the_flag = 0
        cook_book[dish_name.strip()] = list_of_ing
    print(cook_book)
    return (cook_book)

def get_shop_list_by_dishes(cook_book):
    person_count = input('please, input quantity of person')
    dishes = input('please, input names of dishes').split(',')
    for dish in dishes:
        if dish not in cook_book.keys():
            print(f'dish {dish} is not in cook_book')
            pass
        dic_of_ing = {}
        for key in cook_book:
            if key==dish:
                for value in cook_book[key]:
                    value['quantity']=int(value['quantity'])*int(person_count)
                    dic_of_ing[value.pop('ingredient_name')]=value
                print(dic_of_ing)


with open('recipes.txt', encoding='utf-8') as file:
    get_shop_list_by_dishes(cook_book_creation(file))

