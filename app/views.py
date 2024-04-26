from django.shortcuts import render
from django.views.generic import View
from .forms import FeedbackForm
# Create your views here.


class FeedbackView(View):

    def post(self, request):
        data = None
        gender = {
            '1': 'Мужчина',
            '2': 'Женщина'
        }
        internet = {
            '1': 'Каждый день',
            '2': 'Несколько раз в день',
            '3': 'Несколько раз в неделю',
            '4': 'Несколько раз в месяц'
        }
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'city': form.cleaned_data['city'],
                'job': form.cleaned_data['job'],
                'gender': gender[form.cleaned_data['gender']],
                'internet': internet[form.cleaned_data['internet']],
                'notice': 'Да' if form.cleaned_data['notice'] else 'Нет',
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            form = None
        return render(request, 'pool.html', {'form': form, 'data': data})

    def get(self, request):
        form = FeedbackForm()
        return render(self.request, 'pool.html', {'form': form})
