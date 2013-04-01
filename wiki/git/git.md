Git
===

**Гит (git)** нь төлбөргүй, нээлттэй эхтэй, хурдтай, бүтээмжтэй ажилладаг Хувилбар
Удирдах Тархмал Систем юм. Гитийг Линус Торвалдс Линукс цөмийн хөгжүүлэлтэд
зориулан анх 2005 онд бүтээсэн байна.


Ерөнхий
-------

### Үндсэн онцлогууд
- Хурдтай
- Энгийн загвартай
- Тархмал/Шугаман бус хөгжүүлэлтэд тохиромжтой
- Даацтай (том хэмжээний төслүүдэд хурдаа алдахгүй)

### Гит ашигладаг томоохон төслүүд
- Линукс цөм
- Ruby on Rails
- Перл хэл
- OpenSUSE
- GNOME
- jQuery
- SourceForge
- Digg


Суурин ажиллагаа
----------------

Гит агуулахтай ажиллах үед алсын сервертэй холбогдох шаардлага ерөнхийдөө
байхгүй тул хүлээлт огт байхгүй гэж хэлж болно.


Нэгдмэл байдал
--------------

Гит дээр аливаа зүйлийг хадгалахаас өмнө хэшлэж, цаашид хэш дугаараар нь
хаяглаж, жишиж явдаг. Ингэснээр Гитээс гадуур ямар ч файлыг өөрчлөх боломжгүй
болж байгаа юм. Энэ үйл ажиллагаа Гитийн хамгийн доод түвшинд суусан байдаг
бөгөөд ажиллах зарчмын нэг хэсэг нь юм. Хэрвээ ямар нэг файл дамжуулах явцад
эвдэрсэн эсвэл алдагдсан тохиолдолд Гит мэдэгдэх болно. Гит файлыг нэрээр нь
болон агуулгынх нь SHA-1 хэшээр хадгалж, сандаа хэш хаягийг нь хадгалж явдаг.


Ажлын гурван талбар
-------------------

Гиттэй ажиллахад зайлшгүй ойлгох нэгэн ойлголт бол ажлын 3 талбар юм.
- Ажлын хавтас
- Завсрын орчин
- Агуулах
Аливаа файл амьдралын мөчлөгт энэ гурван талбарыг дайрч өнгөрдөг. Ажлын жирийн
явц (урсгал) дараах байдалтай харагдана: Агуулахаас ажлын хавтас руу файлаа
татна. Ажлын хавтсан дахь файлд өөрчлөлт хийсний дараа завсрын орчин руу
шилжүүлнэ. Өөрчлөлтөө хадгалахын тулд завсрын орчин дахь файлыг агуулахад хийнэ.
Өөрөөр хэлбэл ажлын хавтаснаас шууд агуулах руу орохгүй гэсэн үг.


Тохируулах
----------

### Нэр усаа тохируулах
Агуулахад өөрчлөлтөө хадгалахад бүртгэгдэх нэр, э-шуудангийн хаягийг тохируулах:

```
$ git config --global user.name "blackrock"
$ git config --global user.email blackrock@blah.blah
```

### Засварлагчаа тохируулах
```
$ git config --global core.editor "vi"
```

### Өнгө ялгагчийг тохируулах
```
$ git config --global color.status auto
```

### Тушаал товчлох, өөрөөр нэрлэх
Гитийн зарим түгээмэл хэрэглэгддэг тушаалуудыг товчлоё:
```
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
Алсын агуулах руу түлхэж оруулах (push) тушаалыг товчилсон нь:
```
$ git config --global alias.pom 'push origin master'
```

### .gitignore

Бичвэр засварлагч програмууд файл хадгалахдаа файлын_нэр~ гэх мэтчилэн файлын
нэрийн ардаа долгионтой шинэ файл үүсгэн хадгалдаг. Эдгээр файлууд агуулахад
орох шаардлагагүй, тэгэхээр Гитд бүртгэхгүй байхыг сануулахын тулд ажлын
хавтсандаа .gitignore нэртэй файл үүсгээд түүн дотроо бүртгэлгүй алгасах файлын
нэрийн хэлбэрийг бичиж өгнө.

```
*~     # <- текст засварлагчийн үүсгэсэн түр зуурын файл
*.pyc  # <- пайтон хөрвүүлэг файл
```