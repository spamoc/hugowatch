## abount

watching [hugo](https://gohugo.io/) project directory and copy repository directory automation.

## usage

hugowatcher.py C:\\path\\from\\diary C:\\path\\to\\diary

## prerequisites

* install hugo and adding PATH
* python(test by 3.5)
* watchdog

## attention

* 中身のコピーの際にすでにあるディレクトリを削除してからディレクトリごとコピーするとかやってるのでgitのルートがそこにあった場合都度ロストする可能性があります
* エディタによってはmodifyの検知が2回立て続けに発生することがあります