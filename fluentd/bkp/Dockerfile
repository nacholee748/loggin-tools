# https://docs.fluentd.org/v/0.12/container-deployment/docker-compose

# Fluent Alpine version
FROM fluent/fluentd:v1.15-1

# Use root account to use apk
# USER root

# below RUN includes plugin as examples elasticsearch is not required
# you may customize including plugins as you wish
# RUN apk add --no-cache --update --virtual .build-deps \
#         sudo build-base ruby-dev \
#  && sudo gem install fluent-plugin-elasticsearch \
#  && sudo gem sources --clear-all \
#  && apk del .build-deps \
#  && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

COPY fluent.conf /fluentd/etc/fluent.conf
# COPY entrypoint.sh /bin/

# USER fluent

# COPY fluent.conf /fluentd/etc/fluent.conf

# # RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.2"]
# RUN ["gem", "install", "fluent-plugin-s3", "--no-rdoc", "--no-ri", "--version", "1.1.0"]



# # docker run -p 24224:24224 -d --rm -v ${PWD}/data:/fluentd/log -v ${PWD}/fluent.conf:/fluentd/etc/fluent.conf fluentd-alpine
# # docker run -p 24224:24224 -d --rm -v ${PWD}/data:/fluentd/log -v ${PWD}:/fluentd/etc/ -v ~/.aws/credentials:~/.aws/credentials fluentd