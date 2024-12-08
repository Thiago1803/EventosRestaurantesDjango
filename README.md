
# 🍽️ **Sistema de Reserva de Mesas**  

Um sistema simples e eficiente para reservas de mesas em restaurantes!  
O cliente pode selecionar:  
-  **Cidade**  
-  **Tipo de comida**  
-  **Data da reserva**  

Além disso, é possível filtrar por tipos de estabelecimentos, como:  
-  Pubs  
-  Restaurantes familiares  
-  Outros tipos de locais!  

---

## 🛠️ **Como rodar a aplicação**  

### Pré-requisitos  
Certifique-se de ter o **Python** instalado na sua máquina.  

### Passo a passo  

1. **Clone o repositório**  
   ```bash  
   git clone https://github.com/seu-usuario/seu-repositorio.git  
   cd seu-repositorio  
   ```  

2. **Inicie a venv (Linux)**  
   ```bash  
   source venv/bin/activate  
   ```  

3. **Instale as dependências**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Rode as migrações do banco de dados**  
   ```bash  
   python manage.py migrate  
   ```  

5. **Inicie o servidor**  
   ```bash  
   python manage.py runserver  
   ```  

Pronto! 🚀 Acesse o sistema em: **http://127.0.0.1:8000**  

---

## 📚 **Arquitetura da aplicação**  

[![](https://mermaid.ink/img/pako:eNqlVEuP2jAQ_ivWXAsICOTha6uVem3VSxUJTePZYCmxI3vcliL-e52wQoHswlb1IZn55vXNZJwjVFYRSKga9P6TxtphWxoRz4CIb56cOJ6R_nwQWkmhDY-hEJ0MtiSFZzc2UIu6maBdTPzLOjUynEozrvoRmWrrDg8r31S9SfNkrfrPFF_IMwaHhv2_ZjqDqJQj76dD2Fvz3oFVmg8TUJGvnO5YWzOxsWVsdrEuuZ_Ye_gJWduR0abese5J98-rio31d6yO4gdSO2QpVJRu7brFOoZ97l9Pmhr11mgv9B7PNrQ_yN1vqacy9nid3NvkL_yGpS9hVYKYz6NgonDFVsYWNBl-CRwvyf0wpva1EDMOGbZWis56H7RoyYSHIZf7MlQQ1VnV6GEGLbm4VCre8WHGJfCeYscgo6joGUPDJZTmFF0xsP16MBVIdoFm4Gyo9yCfsfFRC10_rpd_xAXt0Hy39koHeYTfIOebIlmkxXKdJ_ky32bLdTqDA8jVJlkUaZovk3WeZXmxTU8z-DPkWC22WbFJsyRbFUmaF8X69BeSzWD-?type=png)](https://mermaid.live/edit#pako:eNqlVEuP2jAQ_ivWXAsICOTha6uVem3VSxUJTePZYCmxI3vcliL-e52wQoHswlb1IZn55vXNZJwjVFYRSKga9P6TxtphWxoRz4CIb56cOJ6R_nwQWkmhDY-hEJ0MtiSFZzc2UIu6maBdTPzLOjUynEozrvoRmWrrDg8r31S9SfNkrfrPFF_IMwaHhv2_ZjqDqJQj76dD2Fvz3oFVmg8TUJGvnO5YWzOxsWVsdrEuuZ_Ye_gJWduR0abese5J98-rio31d6yO4gdSO2QpVJRu7brFOoZ97l9Pmhr11mgv9B7PNrQ_yN1vqacy9nid3NvkL_yGpS9hVYKYz6NgonDFVsYWNBl-CRwvyf0wpva1EDMOGbZWis56H7RoyYSHIZf7MlQQ1VnV6GEGLbm4VCre8WHGJfCeYscgo6joGUPDJZTmFF0xsP16MBVIdoFm4Gyo9yCfsfFRC10_rpd_xAXt0Hy39koHeYTfIOebIlmkxXKdJ_ky32bLdTqDA8jVJlkUaZovk3WeZXmxTU8z-DPkWC22WbFJsyRbFUmaF8X69BeSzWD-)

---

## 📌 **Funcionalidades principais**  

- **Cadastro e gerenciamento de reservas**  
- **Filtro por localização, tipo de comida e estabelecimentos**  
- **Interface simples e intuitiva para os clientes**  
