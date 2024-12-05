

def creer_event(request):
    if request.method == 'POST':
        try:
            titre = request.POST.get('titre')    