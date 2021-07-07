FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip uninstall -y pandas
RUN pip uninstall -y numpy
RUN pip install tld --ignore-installed sklearn
RUN pip install tld --ignore-installed six
RUN pip install tld --ignore-installed itsdangerous
RUN pip install tld --ignore-installed tornado
RUN pip install tld --ignore-installed ipykernel
RUN pip install tld --ignore-installed ipywidgets
RUN pip install -r requirements.txt
CMD python WebAPISwagger.py