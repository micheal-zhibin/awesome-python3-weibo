# awesome-python3-weibo
awesome-python3-weibo

使用gunicorn一步搞定后端代码热处理

pip3 install gunicorn
gunicorn -b 127.0.0.1:8800 -k aiohttp.worker.GunicornWebWorker -w 1 -t 60 --reload app:app
