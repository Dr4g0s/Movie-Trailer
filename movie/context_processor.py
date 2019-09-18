from .models import Movie


def get_slider(request):
    movies = Movie.objects.all().order_by('-created')[:3]
    return {'slider' : movies}


def get_years(request):
    years = []
    temp  = []
    all = Movie.objects.all().order_by('year')
    for y in all:
        temp.append(y.year.year)
    for x in temp:
        if x not in years:
            years.append(x)
    return {'years' : years}

def get_category(request):
    categories = []
    unique_categories = []
    all = Movie.objects.all().order_by('category')
    for c in all:
        category = c.category
        if ',' in str(category):
            for c in category:
                categories.append(c)
        else:
            categories.append(str(category))
    for x in categories:
        if x not in unique_categories:
            unique_categories.append(x)
    return {'categories' : unique_categories}
