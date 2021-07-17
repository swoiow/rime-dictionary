FROM mcr.microsoft.com/dotnet/runtime:3.1

LABEL App=ImeWlConverter
LABEL Github=https://github.com/studyzy/imewlconverter
ARG BIN_LINK=https://github.com/studyzy/imewlconverter/releases/download/v2.9.0/imewlconverter_Linux_Mac.tar.gz

WORKDIR /wordbook

RUN apt-get update && \
    apt-get install -y wget && \
    wget -qO- ${BIN_LINK} | tar -xvz -C /usr/local/bin && \
    rm -rf /root/.cache /tmp/* /var/lib/apt/* /var/cache/* /var/log/*

ENTRYPOINT ["/usr/local/bin/ImeWlConverterCmd"]
