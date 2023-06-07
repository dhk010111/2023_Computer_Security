from distutils.core import setup
import py2exe

options = {                                       #(1)
	"bundle_files" : 1, #번들링 여부 결정: 1-파이썬 인터프리터까지 번들링
	"compressed" : 1, #라이브러리 아카이브를 압축할 것인지 결정: 1-압축
	"optimize"     : 2, #코드 최적화: 2-추가최적화
}

setup (                                           #(2)
	console = ["backdoorClient.py"],
	options = {"py2exe" : options},
	zipfile = None
)
