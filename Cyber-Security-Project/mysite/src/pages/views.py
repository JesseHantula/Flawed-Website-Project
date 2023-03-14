import sqlite3
from django.shortcuts import render, redirect
from .forms import CreateListForm, CreateItemForm
from .models import List, Item
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from pathlib import Path
#to fix flaw 4, we import csrf_protect to protect against cross-site request forgery
'''
from django.views.decorators.csrf import csrf_protect
'''

#to fix flaw 5, we import logging to log errors
'''
import logging
logger = logging.getLogger(__name__)
'''

#we add the csrf_protect decorator to protect against cross-site request forgery (flaw 4)
'''
@csrf_protect
'''
def home(request):
    lists = List.objects.all()   
    return render(request, 'pages/home.html', {'lists': lists})

#we add the csrf_protect decorator to protect against cross-site request forgery (flaw 4)
'''
@csrf_protect
'''
def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect('view_list', list.id)
        #log the error to the console (flaw 5)
        '''
        else:       
            logger.error('Form is invalid')
        '''
    else:
        form = CreateListForm()
    return render(request, 'pages/create_list.html', {'form': form})
    


def verify_password(request, list_id):
    list = List.objects.get(pk=list_id)
    if request.method == 'POST':
        password = request.POST['password']
        if password == list.password:
            #to fix flaw 2, we create a session variable to store the password verification specific to the list id
            '''
            request.session['list_verified_%d' % list_id] = True
            '''
            
            return redirect('view_list', list_id)
        else:
            #log the error to the console (flaw 5)
            '''
            logger.error('Incorrect password')
            '''

            return HttpResponse('Incorrect password')
    else:
        return render(request, 'pages/verify_password.html', {'list': list})
        #we would change the return statement to the following to fix flaw 4
        '''
        return render(request, 'pages/verify_password.html', {'list': list}, context_instance=RequestContext(request))
        '''


#we add the csrf_protect decorator to protect against cross-site request forgery (flaw 4)
'''
@csrf_protect
'''
def view_list(request, list_id):
    list = List.objects.get(pk=list_id)
    items = Item.objects.filter(list=list) 
    #we then check to see if the password has been verified, if it hasn't, we redirect to the verify password page (flaw 2)
    '''
    if not request.session.get('list_verified_%d' % list_id):
        return redirect('verify_password', list_id)
    '''
      
    return render(request, 'pages/view_list.html', {
            'list': list,
            'items': items,
            'form': CreateItemForm()
        })
    
 #we add the csrf_protect decorator to protect against cross-site request forgery (flaw 4)
'''
@csrf_protect
'''   
def create_item(request, list_id):
    list = List.objects.get(id=list_id)
    if request.method == 'POST':
        form = CreateItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list = list
            item.save()
            return redirect('view_list', list_id)
        #log the error to the console (flaw 5)
        '''
        else:
            logger.error('Form is invalid')
        '''

    else:
        form = CreateItemForm()
    return render(request, 'pages/create_item.html', {'form': form, 'list': list})

def complete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.completed = True
    item.save()
    return redirect('view_list', item.list.id)

def delete_list(request, list_id):
    #this is the original code, which is vulnerable to SQL injection (flaw 3)
    connection = sqlite3.connect(Path(__file__).resolve().parent.parent / 'db.sqlite3')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM pages_list WHERE id = %s;" % (list_id,))
    connection.commit()
    connection.close()
    return redirect('home')

#to fix flaw 3, we use Djano's ORM to delete the list instead of deleting it using SQL injection
'''
def delete_list(request, list_id):
    todo_list = get_object_or_404(List, pk=list_id)
    todo_list.delete()
    return redirect('home')
'''
