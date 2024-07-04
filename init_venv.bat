rd /s /q venv
echo 开始创建虚拟环境
py -3.12 -m venv venv
echo 开始安装依赖包
venv\Scripts\python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
venv\Scripts\python -m pip install --upgrade setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
venv\Scripts\python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pause