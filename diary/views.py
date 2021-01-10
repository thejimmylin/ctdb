from django.views.generic.list import ListView
from .models import Diary

class DiaryListView(ListView):

    model = Diary
    paginate_by = 1
