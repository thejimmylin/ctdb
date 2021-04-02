from django.contrib.auth.decorators import login_required
from django.http.response import Http404, JsonResponse

from core.decorators import permission_required
from diary.views import get_diary_queryset

from .serializers import DiaryModelSerializer


@login_required
@permission_required('diary.view_diary', raise_exception=True, exception=Http404)
def api_diary_list(request):
    queryset = get_diary_queryset(request)
    serializer = DiaryModelSerializer(queryset, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)
