FROM python:3.8-alpine

LABEL name="Python dnstap receiver" \
      description="Dnstap streams receiver" \
      url="https://github.com/dmachard/dnstap-receiver" \
      maintainer="d.machard@gmail.com"
      
WORKDIR /home/dnstap

COPY . /home/dnstap/

RUN true \
    && adduser -D dnstap \
    && pip install --no-cache-dir dnspython protobuf pyyaml\
    && cd /home/dnstap \
    && chown -R dnstap:dnstap /home/dnstap \
    && true
    
USER dnstap

EXPOSE 6000/tcp

ENTRYPOINT ["python", "-c", "from dnstap_receiver.receiver import start_receiver; start_receiver()"]