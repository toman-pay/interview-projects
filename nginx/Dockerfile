FROM nginx:latest

#RUN mkdir -p /etc/nginx/sites-enabled/
#RUN cp /confs/nginx.conf /etc/nginx/
#RUN ln -s /confs/django.conf /etc/nginx/sites-enabled/

COPY nginx.conf /etc/nginx/nginx.conf
COPY django.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
