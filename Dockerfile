FROM python:3.11-slim

WORKDIR /app

# Copie apenas o requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Atualize o pip antes de instalar as dependências
RUN pip install --upgrade pip

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do código
COPY . .

EXPOSE 8000

CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]