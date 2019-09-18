from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks, Contact
from django.db.models import Q
from .forms import ContactForm
# Create your views here.



class MovieHomeView(ListView):
    model = Movie
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(MovieHomeView, self).get_context_data(**kwargs)
        context['recent_movies'] = Movie.objects.all().order_by('-created')[:16]
        context['most_movies']   = Movie.objects.all().order_by('-views')[:16]
        context['top_movies']    = Movie.objects.all().order_by('-year')[:16]
        return context

class MovieListView(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'list.html'

class MovieListByCategory(ListView):
    model = Movie
    template_name = 'list.html'

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category__icontains=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieListByCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context

class MovieListByLanguage(ListView):
    model = Movie
    template_name = 'list.html'

    def get_queryset(self):
        self.language = self.kwargs['language']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieListByLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context

class MovieListByYear(ListView):
    model = Movie
    template_name = 'list.html'

    def get_queryset(self):
        self.year = self.kwargs['year']
        return Movie.objects.filter(year__year=self.year)

    def get_context_data(self, **kwargs):
        context = super(MovieListByYear, self).get_context_data(**kwargs)
        context['movie_year'] = self.year
        return context

class MovieListByCast(ListView):
    model = Movie
    template_name = 'list.html'

    def get_queryset(self):
        self.cast = self.kwargs['cast']
        return Movie.objects.filter(cast__name=self.cast)

    def get_context_data(self, **kwargs):
        context = super(MovieListByCast, self).get_context_data(**kwargs)
        context['movie_cast'] = self.cast
        return context

def related_movies(movie):
    q = Q()
    for category in movie.category:
        q |= Q(category__icontains=category)
    all = Movie.objects.filter(q).exclude(id=movie.id).order_by('category')[:6]
    return all

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'detail.html'

    def get_object(self):
        return super(MovieDetailView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['links'] = MovieLinks.objects.filter(movie=obj)
        context['related_movies'] = related_movies(obj)
        print(context)
        obj.views += 1
        obj.save()
        return context

class MovieSearch(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'list.html'

    def get_queryset(self):
        query  = self.request.GET.get('s')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list = Movie.objects.none()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(MovieSearch, self).get_context_data(**kwargs)
        if not self.get_queryset():
            context['result'] = 'none'
        context['search_result'] = self.get_queryset()
        return context

def MovieContactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form':form, 'message':'success'})
        else:
            return render(request, 'contact.html', {'form':form, 'message':'error'})
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def MovieTerms(request):
    return render(request, "terms.html")
