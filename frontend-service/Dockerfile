# 準備一個最簡靜態網站容器
FROM nginx:alpine

# 將 index.html 放到 nginx 的根目錄

COPY index.html /usr/share/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;"]