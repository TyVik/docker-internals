FROM ubuntu
RUN apt update && apt install stress
ENTRYPOINT ["/usr/bin/stress", "-c", "2", "--vm", "2", "--vm-bytes", "256M"]
