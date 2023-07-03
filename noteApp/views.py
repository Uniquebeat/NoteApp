from django.shortcuts import render, redirect
from .models import NoteModel
from .forms import NoteForm

# Create your views here.

def NoteListView(request):
    notes = NoteModel.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'noteList.html', context)

def NoteDetailView(request, pk):
    note = NoteModel.objects.get(id=pk)

    if request.method == 'GET':
        form = NoteForm(instance=note)
    elif request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'note': note,
        'form': form
    }
    
    return render(request, 'noteDetail.html',context)

def NoteCreateView(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form': form
    }

    return render(request, 'noteCreate.html', context)

def NoteDeleteView(request, pk):
    note = NoteModel.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    
    context = {
        'note': note
    }

    return render(request, 'noteDelete.html', context)
