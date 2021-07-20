FROM python:3.9.6-alpine3.14

# Update native packages
RUN apk update

# Set environment
WORKDIR /usr/src/app
RUN python -m venv venv
ENV PATH /usr/src/app/venv/bin:$PATH
RUN source venv/bin/activate
COPY settings_sample.toml ./settings.toml

# Get and install dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Get and run application
COPY . .
EXPOSE 5000
CMD [ "waitress-serve" , "--call", "--listen=0.0.0.0:5000", "app:create_app" ]
