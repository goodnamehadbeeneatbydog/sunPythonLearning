# 举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
# 现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，
# 避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
# mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，
# abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
# 也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，
# 自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块

# 2.内置函数¶
# Python解释器内置了许多始终可用的函数和类型。它们按字母顺序列在此处。
#
# 内置功能
# abs()	delattr()	hash()	memoryview()	set()
# all()	dict()	help()	min()	setattr()
# any()	dir()	hex()	next()	slice()
# ascii()	divmod()	id()	object()	sorted()
# bin()	enumerate()	input()	oct()	staticmethod()
# bool()	eval()	int()	open()	str()
# breakpoint()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()