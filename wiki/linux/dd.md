# dd #

dd тушаал ашиглан хаард диск, партишн нөөцлөх, сэргээх
боломжтой.

**Юу хийж байгаагаа мэдэхгүй бол ашиглаад хэрэггүй,
["нүдээ сохлоно"](http://www.youtube.com/watch?v=YleZvTSDC6s)!**

Үндсэн бичиглэл:

    dd if=/dev/sda1 of=/dev/sdb bs=512k

`if` гэж оролтын файл, `of` гэж гаралтын файлыг заана.

**Үндсэн партишнаа гаралтын файл болгож заагаад балруузай!**

## Хаард нөөцлөх ##

    dd if=/dev/sda of=/dev/sdb bs=512k

## Хаард зураг файлд нөөцлөх ##

    dd if=/dev/sda of=/media/thx/hard.img bs=512k

## Хаард зураг файлаас сэргээх ##

    dd if=/media/thx/hard.img of=/dev/sda bs=512k

## ISO-оос USB бүүт бэлдэх ##

Unetbootin зэргийг ашиглахын оронд зүгээр л dd тушаал
өгчихнө:

    dd if=~/Downloads/knoppix.iso of=/dev/sdb bs=512k
