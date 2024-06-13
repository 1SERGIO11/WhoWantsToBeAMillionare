from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Questions
import random

def home_page_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user, created = User.objects.get_or_create(first_name=first_name, last_name=last_name)
        request.session['user_id'] = user.id  # Сохраняем ID пользователя в сессию
        user.current_level = request.session.get('current_level', 1)
        user.save()
        response = redirect('home')
        response.set_cookie('registration_success', 'true', max_age=900)
        return response
    else:
        current_level = request.GET.get('level', 1)
        request.session['current_level'] = current_level
        questions = list(Questions.objects.filter(level=current_level))
        question = random.choice(questions) if questions else None
        top_winners = User.objects.order_by('-prize_amount', '-max_level_reached')[:10]

        context = {
            'question': question,
            'winner1': top_winners[0] if len(top_winners) > 0 else None,
            'winner2': top_winners[1] if len(top_winners) > 1 else None,
            'winner3': top_winners[2] if len(top_winners) > 2 else None,
            'winner4': top_winners[3] if len(top_winners) > 3 else None,
            'winner5': top_winners[4] if len(top_winners) > 4 else None,
            'winner6': top_winners[5] if len(top_winners) > 5 else None,
            'winner7': top_winners[6] if len(top_winners) > 6 else None,
            'winner8': top_winners[7] if len(top_winners) > 7 else None,
            'winner9': top_winners[8] if len(top_winners) > 8 else None,
            'winner10': top_winners[9] if len(top_winners) > 9 else None,
        }

        return render(request, 'HomePage.html', context)




def submit_answer(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')
        user_id = request.session.get('user_id')  # Получение user_id из сессии

        if not user_id:
            return HttpResponse("User not logged in or session expired", status=401)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse("User not found. Please log in again.", status=404)

        question = Questions.objects.get(id=question_id)

        if int(answer) == question.right_answer:
            next_level = question.level + 1
            user.current_level = next_level
            user.stopped_question = question
            if next_level > user.max_level_reached:
                user.max_level_reached = next_level
        else:
            next_level = 1
            user.current_level = next_level
            user.stopped_question = None
            user.prize_amount = get_prize_amount(user.max_level_reached - 1)  # Сохранение суммы выигрыша

        user.save()
        request.session['current_level'] = next_level

        response_data = {
            'next_level': next_level,
            'correct_answer': question.right_answer
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Invalid request", status=400)

def get_prize_amount(level):
    prize_dict = {
        1: 500,
        2: 1000,
        3: 2000,
        4: 3000,
        5: 5000,
        6: 10000,
        7: 15000,
        8: 25000,
        9: 50000,
        10: 100000,
        11: 200000,
        12: 400000,
        13: 800000,
        14: 1500000,
        15: 3000000
    }
    return prize_dict.get(level, 0)



def get_question(request, level):
    questions = list(Questions.objects.filter(level=level))
    if questions:
        question = random.choice(questions)
        data = {
            'question_text': question.question,
            'right_answer': question.right_answer,
            'answers': [question.answer1, question.answer2, question.answer3, question.answer4],
            'question_id': question.id
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'No questions available'}, status=404)
