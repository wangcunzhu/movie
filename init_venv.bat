rd /s /q venv
echo ��ʼ�������⻷��
py -3.12 -m venv venv
echo ��ʼ��װ������
venv\Scripts\python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
venv\Scripts\python -m pip install --upgrade setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
venv\Scripts\python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pause