from django.urls import path
from .views import AvaliacoesAPIView, CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliaca_pk>',
        AvaliacoesAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avalicao'),

]