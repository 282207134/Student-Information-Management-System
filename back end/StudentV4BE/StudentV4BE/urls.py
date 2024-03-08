from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
path('admin/', admin.site.urls),
path('students/', views.get_students), # 学生情報を取得するAPI
path('students/query/', views.query_students), # 学生情報を検索するAPI
path('sno/check/', views.is_exsits_sno), # 学籍番号の存在を検証するAPI
path('student/add/', views.add_student), # 学生情報を追加するAPI
path('student/update/', views.update_student), # 学生情報を更新するAPI
path('student/delete/', views.delete_student), # 学生情報を削除するAPI
path('students/delete/', views.delete_students), # 学生情報を一括削除するAPI
path('upload/', views.upload), # ファイルをアップロードするAPI
path('excel/import/', views.import_students_excel), # ExcelファイルをインポートするAPI
path('excel/export/', views.export_student_excel), # ExcelファイルをエクスポートするAPI
]
# 以下の行を追加--- すべてのmediaファイルがアクセス可能になるようにする
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







