FROM debian:buster
RUN apt update && apt install stress
CMD ["/usr/bin/stress", "-c", "2", "--vm", "2", "--vm-bytes", "256M"]
