from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='course_list'),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name='course_detail'),

    path('faculty', FacultyViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='faculty_list'),
    path('faculty/<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='faculty_detail'),

    path('teacher', TeacherViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='teacher_detail'),

    path('student', StudentViewSet.as_view({'get': 'list',
                                          'post': 'create'}), name='student_list'),
    path('student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update', 'delete': 'destroy'}), name='student_list'),

    path('room', RoomViewSet.as_view({'get': 'list',
                                      'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve',
                                                'put': 'update', 'delete': 'destroy'}), name='room_detail'),

    path('table', TimetableViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='table_list'),
    path('table/<int:pk>/', TimetableViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='table_detail'),

    path('Enrollment', EnrollmentViewSet.as_view({'get': 'list',
                                                  'post': 'create'}), name='enrollment_list'),
    path('Enrollment/<int:pk>/', EnrollmentViewSet.as_view({'get': 'retrieve',
                                                            'put': 'update', 'delete': 'destroy'}), name='enrollment_detail'),
]