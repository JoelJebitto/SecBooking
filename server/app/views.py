from django.shortcuts import render
from .models import Exam, Class, AnswerSheet
from django.shortcuts import get_object_or_404, redirect
from .models import Exam, Class, AnswerSheet, Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


@login_required
def book_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    exam.students.add(request.user)
    return HttpResponse("Exam booked successfully")


@login_required
def book_class(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)
    _class.students.add(request.user)
    return HttpResponse("Class booked successfully")


@login_required
def view_answer_sheet(request, answer_sheet_id):
    answer_sheet = get_object_or_404(
        AnswerSheet, pk=answer_sheet_id, student=request.user)
    # Here you would normally render a template with the answer sheet data.
    # For simplicity, we're just returning the answers as plain text.
    # return HttpResponse(answer_sheet.answers)
    return JsonResponse({'pdf': answer_sheet.pdf.url})


@login_required
def view_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    # Here you would normally render a template with the profile data.
    # For simplicity, we're just returning some of the data as plain text.
    return JsonResponse({
        'user_id': profile.user.id,
        'username': profile.user.username,
        'email': profile.user.email,
        # add other fields as needed
    })


@login_required
def view_all_classes(request):
    classes = Class.objects.filter(students=request.user)
    # Here you would normally render a template with the classes data.
    # For simplicity, we're just returning the class names as plain text.
    return HttpResponse(", ".join(str(c.name) for c in classes))


@login_required
def view_all_exams(request):
    exams = Exam.objects.filter(students=request.user)
    # Here you would normally render a template with the exams data.
    # For simplicity, we're just returning the exam names as plain text.
    return HttpResponse(", ".join(str(e.name) for e in exams))


@login_required
def view_all_answer_sheets(request):
    answer_sheets = AnswerSheet.objects.filter(student=request.user)
    # Here you would normally render a template with the answer sheets data.
    # For simplicity, we're just returning the answer sheet IDs as plain text.
    return HttpResponse(", ".join(str(asheet.id) for asheet in answer_sheets))


@login_required
def book_class(request, class_id):
    # Get the Class object with the given id
    class_to_book = get_object_or_404(Class, id=class_id)

    # Add the current user to the students of the class
    class_to_book.students.add(request.user)
    class_to_book.save()

    messages.success(request, 'Class booked successfully')
    return redirect('view_all_classes')


@login_required
def book_exam(request, exam_id):
    # Get the Exam object with the given id
    exam_to_book = get_object_or_404(Exam, id=exam_id)

    # Add the current user to the students of the exam
    exam_to_book.students.add(request.user)
    exam_to_book.save()

    messages.success(request, 'Exam booked successfully')
    return redirect('view_all_exams')
