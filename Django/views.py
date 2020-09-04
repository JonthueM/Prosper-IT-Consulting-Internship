from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Games_UpComing
from .forms import  GamesUpComingForm
from bs4 import BeautifulSoup as BS
import string
from .api_service import  *


# Create your views here.
def home(request):
    return render(request, 'GameApp/Game_App_Home.html')

def index(request):
    get_event = Games_UpComing.eventModel.all()
    context = {'games': get_event} #Games is the variable you will use to refernce the table, for games is the key to this data
    return render(request, 'GameApp/Game_App_Index.html', context)

def addEvent(request):
    form = GamesUpComingForm(request.POST or None) # gets the pasted form, if one exists
    if form.is_valid(): #checks the form for errors, ensuring it's filled in
        form.save() #saves the valid form to the database
        return redirect('game')
    else:
        print(form.errors) #prints any errors for the posted form to the form to the terminal
        form = GamesUpComingForm() #Creates a new black form
    return render(request,'GameApp/Game_App_Create.html', {'form': form})

def details_Event(request, pk):
    pk = int(pk)                                    #Casts value of pk to an int so it's in the proper form
    event = get_object_or_404(Games_UpComing, pk=pk)      #Gets single instance of the food from the database
    context = {'game':event}                           #Creates dictionary object to pass the food object
    return render(request,'GameApp/Game_App_Details.html', context)

def edit_Event(request, pk):
    pk = int(pk)
    event = get_object_or_404(Games_UpComing, pk=pk)
    if request.method == 'POST':
        form = GamesUpComingForm(request.POST, instance=event)
        if form.is_valid():
            events = form.save()
            events.save()
            return redirect('eventDetails', pk=events.pk)
        else:
            print(form.errors)
            form = GamesUpComingForm(instance=event)
    else:
        form = GamesUpComingForm(instance=event)
        context = {'form': form, 'pk': pk}
        return render(request, 'GameApp/Game_App_Edit.html', context)


def delete_Event(request, pk):
    pk = int(pk)
    form = get_object_or_404(Games_UpComing, pk=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('listEvent')
    context = {'form': form, 'pk': pk}
    return render(request, 'GameApp/Game_App_Delete.html', context)

#def game_API(request,pk):
 #   return render(request,'GameApp/Game_App_API.html')

def game_News(request):
    print('Hello World')
    source = requests.get('https://www.gameinformer.com/news')
    print(source.status_code)
    soup = BS(source.content, 'html.parser')
    nodes = soup.find_all(class_="views-row")
    articles = []
    for node in nodes:
        title = node.find(class_="field field--name-title field--type-string field--label-hidden").get_text()
        img = node.find('img').get("src")
        summary = node.find(class_="field field--name-field-promo-summary field--type-string field--label-hidden field__item").get_text()
        author = node.find(class_="username").get_text()
        #type = node.find("h2").find("a").get_text()
        time = node.find(class_="field field--name-created field--type-created field--label-hidden").get_text()
        link = node.find('a').get('href')  # Sets link equal to the href of the a tag
        url = "https://www.gameinformer.com/" + link  # Modifies the link to a full url, since the links were relative
        article = { 'img':img,'title': title, 'summary':summary, 'author':author, 'url': url, 'time':time}
        articles.append(article)
        context = {'articles': articles}
    return render(request, 'GameApp/Video_Games_News.html', context)




