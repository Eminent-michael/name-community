from .models import Category


def categorySplit(request, category):
    cat_obj=[]
    
    cat_list = list(category.replace(" ", "").split(","))
    
    for cat in cat_list:
        c, cat = Category.objects.get_or_create(title=cat)
        cat_obj.append(c)
        
    return cat_obj