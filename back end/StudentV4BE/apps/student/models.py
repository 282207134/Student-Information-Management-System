from django.db import models
# ここでモデルを定義します。
# Student: 学籍番号、名前、性別、生年月日、携帯番号、メールアドレス、住所、写真
class Student(models.Model):
    gender_choices = (('男性', '男性'), ('女性', '女性'))
    sno = models.IntegerField(db_column="SNo", primary_key=True, null=False)  # 学籍番号、空でない、主キー
    name = models.CharField(db_column="SName", max_length=100, null=False)  # 名前、最大100文字、空でない
    gender = models.CharField(db_column="Gender", max_length=100, choices=gender_choices)  # 性別、選択肢あり
    birthday = models.DateField(db_column="Birthday", null=False)  # 生年月日、空でない
    mobile = models.CharField(db_column="Mobile", max_length=100)  # 携帯番号
    email = models.CharField(db_column="Email", max_length=100)  # メールアドレス
    address = models.CharField(db_column="Address", max_length=200)  # 住所
    image = models.CharField(db_column="Image", max_length=200, null=True)  # 写真
    # デフォルトでは、生成されたテーブル名：アプリ名_クラス名、カスタマイズする場合はClass Metaを使用してカスタマイズする
    class Meta:
        managed = True
        db_table = "Student"
    # __str__ メソッド
    def __str__(self):
        return "学籍番号：%s\t名前：%s\t性別：%s" % (self.sno, self.name, self.gender)
