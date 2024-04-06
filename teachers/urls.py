from rest_framework import routers

from teachers.views import CategoryView, TeacherView

router = routers.SimpleRouter()
router.register('category', CategoryView)
router.register('teacher', TeacherView)

urlpatterns = [] + router.urls
