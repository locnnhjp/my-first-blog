from django.shortcuts import render


# Create your views here.
def post_list(request):
    # テンプレートに渡すデータ
    data = {}
    return render(request, 'blog/post_list.html', data)