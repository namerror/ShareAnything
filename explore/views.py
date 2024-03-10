from django.shortcuts import render, get_object_or_404
from explore.models import WebPage, Category
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

def list(request, category_slug=None):
    category = None # default none
    
    webpages = WebPage.objects.all()

    url_parameter = request.GET.get("q")

    '''
    Filtering the categories by search
    '''
    if url_parameter:
        categories = Category.objects.filter(name__icontains=url_parameter)
    else:
        categories = Category.objects.all()
    

    '''
    Getting webpages based on the category selected
    '''
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        webpages = WebPage.objects.filter(category=category)

    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(
            template_name="explore/categories-results-partial.html",
            context={"categories":categories}
        )

        data_dict = {"html_from_view": html} # the html block containing the categories based on user search in string

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'explore/list.html', {'category' : category,
                                                 'categories' : categories,
                                                 'webpages' : webpages})

