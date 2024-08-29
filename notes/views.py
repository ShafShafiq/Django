from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView, ListView , DetailView , UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Notes
from .form import NotesForm



class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'
    context_object_name = "note"
    login_url = '/admin'


class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/note_form.html'
    success_url = '/smart/notes'
    login_url = '/admin'


class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/note_form.html'
    success_url = '/smart/notes'
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        # return super().form_valid(form)

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'all_notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

# def notes_list (request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'all_notes': all_notes})


class NoteDetailsView(LoginRequiredMixin,DetailView):
    model = Notes
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'
    login_url = '/admin'



# def notes_detail (request ,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except note.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/note_detail.html', {'note': note})