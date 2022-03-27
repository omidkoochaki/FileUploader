FROM minio/minio
RUN mkdir -p /var/www/html/data
CMD ["minio", "server", "/var/www/html/data --console-address :9001"]

#RUN #minio server /Users/omid/minio/ --console-address ":9001" -d
#WORKDIR -p ~/minio/data
