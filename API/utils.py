import random
import string


#function to generate random numbers.
def random_sku_generator(size=6,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_sku_generator(instance):
    new_random_sku = random_sku_generator()
    #instance of item class
    Kclass= instance.__class__
    #check if that sku already exists
    query_exists= Kclass.objects.filter(sku= new_random_sku).exists()
    #if exist call the function again
    if query_exists:
        return unique_sku_generator(instance)
    
    return new_random_sku
