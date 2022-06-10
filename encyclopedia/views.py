from django.shortcuts import redirect, render
from django import forms

from . import util
import markdown
import secrets

#class SearchForm(forms.Form):
#   search = forms.CharField(label= "Search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getpage(request, title):
    try:
        mdpage = util.get_entry(title)
        htmlpage = markdown.markdown(mdpage)
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": htmlpage
    })

    except:    
        return render(request, "encyclopedia/error.html", {
            "title": "404 Error: Page Not Found",
            "error": "Page not found"
    })
    

def search (request):
    query = request.GET.get("q")
    entry_list = util.list_entries()


    if util.get_entry(query):
        mdpage = util.get_entry(query)
        htmlpage = markdown.markdown(mdpage)
        
        return render(request, "encyclopedia/entry.html", {
        "title": query,
        "content": htmlpage
        })

    else: 
        results = [entry for entry in entry_list if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {
        "title": "Search Result",
        "entries": results
        })      

def new (request):
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")

            if util.get_entry(title):
                return render(request, "encyclopedia/new_page_error.html", {
                "title": "400 Error: Page Already Exists",
                "error": "Page already exists"
                })
            
            else:
                util.save_entry(title, content)
                mdpage = util.get_entry(title)
                htmlpage = markdown.markdown(mdpage)
                return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": htmlpage
                })
        elif request.method =="GET":
            return render(request, "encyclopedia/new.html")

def edit (request):

    if request.method =="GET":
        title = request.GET.get("title")
        #content = request.GET.get("content")

        
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": util.get_entry(title)

            })
    elif request.method =="POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            print(title)

            util.save_entry(title, content)
            mdpage = util.get_entry(title)
            htmlpage = markdown.markdown(mdpage)
            return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": htmlpage
            })

def random(request):
    entry = secrets.choice(util.list_entries())
    print(util.list_entries())
    print(entry)
    mdpage = util.get_entry(entry)
    htmlpage = markdown.markdown(mdpage)
        
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "content": htmlpage
        })

