# awesome-python3-weibo
awesome-python3-weibo

使用gunicorn一步搞定后端代码热处理

pip3 install gunicorn
gunicorn -b 127.0.0.1:8800 -k aiohttp.worker.GunicornWebWorker -w 1 -t 30 --reload app:app

-w 表示worker数，工作进程数，默认1，推荐为cpu*2+1
-c 配置文件路径
-b gunicorn服务器套接字
--backlog 未决连接最大数，必定正整数64~2048，一般为2048超过会导致client连接时错误
-k 工作模式：sync(default), eventlet(need eventlet>=0.9.7), gevent(need eventlet>=0.13), tornado(need tornado>=0.2), gthead, gaiohttp(need     aiohttp>=0.9.7 && python3.4)
--threads 处理请求工作线程数
--worker-connections 最大客户端并发数量
--max-requests 重启之前工作处理最大请求数
-t 超过多少秒后工作杀掉重启，一般30s
--max-requests-jitter 添加到max_requests最大抖动
--graceful_timeout 优雅的人工超时
--keep-alive keep-alive连接上等待请求的描述，默认2，一般1-5
