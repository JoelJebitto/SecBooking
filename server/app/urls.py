from django.urls import path
from . import views

urlpatterns = [
    path('book_exam/<int:exam_id>/', views.book_exam, name='book_exam'),
    path('book_class/<int:class_id>/', views.book_class, name='book_class'),
    path('view_answer_sheet/<int:answer_sheet_id>/', views.view_answer_sheet, name='view_answer_sheet'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('view_all_classes/', views.view_all_classes, name='view_all_classes'),
    path('view_all_exams/', views.view_all_exams, name='view_all_exams'),
    path('view_all_answer_sheets/', views.view_all_answer_sheets, name='view_all_answer_sheets'),
    
]