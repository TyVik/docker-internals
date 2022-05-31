FROM debian
COPY . .
RUN apt update && apt install -y ./libmysqlclient21.deb ./sysbench_1.0.18.deb
CMD ["/usr/bin/sysbench", "cpu", "run", "--time=30"]
