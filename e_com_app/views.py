from django.shortcuts import render

def e_com_app(request):
    name = "Yevhenii"
    current_date = "24.06.2019"
    return render(request, 'e_com_app/e_com_app.html', locals())
