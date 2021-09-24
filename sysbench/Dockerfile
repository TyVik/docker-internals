FROM debian
RUN apt update && apt install -y sysbench
ENTRYPOINT ["/usr/bin/sysbench", "cpu", "run", "--time=30"]
