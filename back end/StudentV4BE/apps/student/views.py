from student.models import Student  # 学生モデルのインポート
from django.http import JsonResponse  # JsonResponseモジュールのインポート
import json  # jsonモジュールのインポート
from django.db.models import Q  # Qクエリのインポート
import uuid  # uuidモジュールのインポート
import hashlib  # hashlibモジュールのインポート
from django.conf import settings  # settingsのインポート
import os  # osモジュールのインポート
import openpyxl  # openpyxlモジュールのインポート

def get_students(request):
    """すべての学生情報を取得します。"""
    try:
        obj_students = Student.objects.all().values()  # すべての学生情報を取得し、辞書に変換します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code':1, 'data':students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "学生情報の取得中にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def query_students(request):
    """学生情報を検索します。"""
    data = json.loads(request.body.decode('utf-8'))  # リクエストボディからデータを取得します
    try:
        obj_students = Student.objects.filter(Q(sno__icontains=data['inputstr']) | Q(name__icontains=data['inputstr']) |
                                              Q(gender__icontains=data['inputstr']) | Q(mobile__icontains=data['inputstr'])
                                              | Q(email__icontains=data['inputstr']) | Q(address__icontains=data['inputstr'])).values()
        # 条件に一致する学生情報を検索し、辞書に変換します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code': 1, 'data': students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "学生情報の検索中にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def is_exists_sno(request):
    """学籍番号が存在するかどうかを確認します。"""
    data = json.loads(request.body.decode('utf-8'))  # リクエストボディからデータを取得します
    try:
        obj_students = Student.objects.filter(sno=data['sno'])  # 学籍番号を条件に検索します
        if obj_students.count() == 0:  # 結果が0件の場合
            return JsonResponse({'code': 1, 'exists': False})  # JSONレスポンスを返します
        else:  # それ以外の場合
            return JsonResponse({'code': 1, 'exists': True})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "学籍番号の検証中にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def add_student(request):
    """学生情報を追加します。"""
    data = json.loads(request.body.decode("utf-8"))  # リクエストボディからデータを取得します
    try:
        obj_student = Student(sno=data['sno'], name=data['name'], gender=data['gender'],
                              birthday=data['birthday'], mobile=data['mobile'],
                              email= data['email'], address=data['address'], image=data['image'])
        obj_student.save()  # 学生情報を保存します
        obj_students = Student.objects.all().values()  # すべての学生情報を取得します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code': 1, 'data': students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code':0 , 'msg': "データベースに学生情報を追加する際にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def update_student(request):
    """学生情報を更新します。"""
    data = json.loads(request.body.decode("utf-8"))  # リクエストボディからデータを取得します
    try:
        obj_student = Student.objects.get(sno=data['sno'])  # 学籍番号に一致する学生情報を取得します
        obj_student.name = data['name']
        obj_student.gender = data['gender']
        obj_student.birthday = data['birthday']
        obj_student.mobile = data['mobile']
        obj_student.email = data['email']
        obj_student.address = data['address']
        obj_student.image = data['image']
        obj_student.save()  # 学生情報を保存します
        obj_students = Student.objects.all().values()  # すべての学生情報を取得します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code': 1, 'data': students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code':0 , 'msg': "データベースに学生情報を保存する際にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def delete_student(request):
    """学生情報を削除します。"""
    data = json.loads(request.body.decode("utf-8"))  # リクエストボディからデータを取得します
    try:
        obj_student = Student.objects.get(sno=data['sno'])  # 学籍番号に一致する学生情報を取得します
        obj_student.delete()  # 学生情報を削除します
        obj_students = Student.objects.all().values()  # すべての学生情報を取得します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code': 1, 'data': students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "データベースに学生情報を削除する際にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def delete_students(request):
    """学生情報を一括削除します。"""
    data = json.loads(request.body.decode("utf-8"))  # リクエストボディからデータを取得します
    try:
        for one_student in data['student']:
            obj_student = Student.objects.get(sno=one_student['sno'])  # 学籍番号に一致する学生情報を取得します
            obj_student.delete()  # 学生情報を削除します
        obj_students = Student.objects.all().values()  # すべての学生情報を取得します
        students = list(obj_students)  # リストに変換します
        return JsonResponse({'code': 1, 'data': students})  # JSONレスポンスを返します
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "データベースから学生情報を一括削除する際にエラーが発生しました：" + str(e)})  # エラーメッセージを返します

def upload(request):
    """アップロードされたファイルを受け取ります。"""
    rev_file = request.FILES.get('avatar')  # ファイルを取得します
    if not rev_file:  # ファイルが存在しない場合
        return JsonResponse({'code':0, 'msg':'画像がありません！'})  # エラーレスポンスを返します
    new_name = get_random_str()  # ファイル名を生成します
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1] )  # ファイルパスを生成します
    try:
        f = open(file_path,'wb')  # ファイルを書き込みモードで開きます
        for i in rev_file.chunks():  # ファイルを書き込みます
            f.write(i)
        f.close()  # ファイルを閉じます
        return JsonResponse({'code': 1, 'name': new_name + os.path.splitext(rev_file.name)[1]})  # 正常なレスポンスを返します
    except Exception as e:
        return JsonResponse({'code':0, 'msg':str(e)})  # エラーレスポンスを返します

def get_random_str():
    """ランダムな文字列を生成します。"""
    uuid_val = uuid.uuid4()  # UUIDを生成します
    uuid_str = str(uuid_val).encode('utf-8')  # UUIDをUTF-8エンコードします
    md5 = hashlib.md5()  # MD5ハッシュオブジェクトを作成します
    md5.update(uuid_str)  # UUIDをハッシュ化します
    return md5.hexdigest()  # ハッシュ値を返します

def import_students_excel(request):
    """Excelから学生情報を一括インポートします。"""
    rev_file = request.FILES.get('excel')  # アップロードされたExcelファイルを取得します
    if not rev_file:  # ファイルが存在しない場合
        return JsonResponse({'code': 0, 'msg': 'Excelファイルが存在しません！'})  # エラーレスポンスを返します
    new_name = get_random_str()  # ファイル名を生成します
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1])  # ファイルパスを生成します
    try:
        f = open(file_path, 'wb')  # ファイルを書き込みモードで開きます
        for i in rev_file.chunks():  # ファイルを書き込みます
            f.write(i)
        f.close()  # ファイルを閉じます
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})  # エラーレスポンスを返します
    ex_students = read_excel_dict(file_path)  # Excelから学生情報を読み込みます
    success = 0  # 成功数を初期化します
    error = 0  # エラー数を初期化します
    error_snos = []  # エラーが発生した学籍番号を格納するリストを初期化します
    for one_student in ex_students:  # 各学生情報について繰り返します
        try:
            obj_student = Student.objects.create(  # 学生情報を作成します
                sno=one_student['sno'],  # 学籍番号を設定します
                name=one_student['name'],  # 名前を設定します
                gender=one_student['gender'],  # 性別を設定します
                birthday=one_student['birthday'],  # 生年月日を設定します
                mobile=one_student['mobile'],  # 携帯電話番号を設定します
                email=one_student['email'],  # メールアドレスを設定します
                address=one_student['address']  # 住所を設定します
            )
            success += 1  # 成功数をインクリメントします
        except:
            error += 1  # エラー数をインクリメントします
            error_snos.append(one_student['sno'])  # エラーが発生した学籍番号をリストに追加します
    obj_students = Student.objects.all().values()  # すべての学生情報を取得します
    students = list(obj_students)  # 学生情報をリストに変換します
    return JsonResponse({'code': 1, 'success': success, 'error': error, 'errors': error_snos, 'data': students})  # 成功とエラーの情報を含むレスポンスを返します

def export_student_excel(request):
    """学生情報をExcelにエクスポートします。"""
    obj_students = Student.objects.all().values()  # すべての学生情報を取得します
    students = list(obj_students)  # 学生情報をリストに変換します
    excel_name = get_random_str() + ".xlsx"  # Excelファイル名を生成します
    path = os.path.join(settings.MEDIA_ROOT, excel_name)  # ファイルパスを生成します
    write_to_excel(students, path)  # 学生情報をExcelに書き込みます
    return JsonResponse({'code': 1, 'name': excel_name })  # 成功レスポンスを返します

def read_excel_dict(path: str):
    """Excelデータを読み取り、辞書として保存します。"""
    workbook = openpyxl.load_workbook(path)  # Excelファイルをロードします
    sheet = workbook['student']  # 'student'シートを選択します
    students = []  # 学生情報のリストを初期化します
    keys = ['sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address']  # カラムのキーを設定します
    for row in sheet.iter_rows(min_row=2):  # 2行目からデータを取得します
        temp_dict = {}  # 一時的な辞書を初期化します
        for index, cell in enumerate(row):  # 各セルについて繰り返します
            if index < len(keys):  # インデックスがキーの数未満の場合
                temp_dict[keys[index]] = cell.value  # キーと値を辞書に追加します
        students.append(temp_dict)  # 学生情報をリストに追加します
    return students  # 学生情報のリストを返します

def write_to_excel(data:list, path:str):
    """データベースの内容をExcelに書き込みます。"""
    workbook = openpyxl.Workbook()  # 新しいExcelブックを作成します
    sheet = workbook.active  # アクティブなシートを取得します
    sheet.title = 'student'  # シートのタイトルを設定します
    keys = data[0].keys()  # カラムのキーを取得します
    for index, item in enumerate(data):  # 各学生情報について繰り返します
        for k,v in enumerate(keys):  # 各キーと値について繰り返します
            sheet.cell(row=index + 1, column=k+ 1, value=str(item[v]))  # セルに値を書き込みます
    workbook.save(path)  # Excelファイルを保存します
