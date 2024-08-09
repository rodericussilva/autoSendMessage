# WhatsApp Automation with Selenium

Este projeto utiliza a biblioteca Selenium para automatizar o envio de mensagens via WhatsApp Web. As URLs inseridas nas mensagens podem ser automaticamente encurtadas usando a API Bitly.

## Funcionalidades

- **Automação do WhatsApp Web**: Envio automático de mensagens para contatos predefinidos.
- **Encurtamento de URLs**: URLs nas mensagens são encurtadas usando a API Bitly.
- **Agendamento**: Envio de mensagens em horários pré-determinados ao longo do dia.

## Requisitos

- Python 3.7 ou superior
- [Selenium](https://www.selenium.dev/)
- [webdriver_manager](https://pypi.org/project/webdriver-manager/)
- [pandas](https://pandas.pydata.org/)
- [requests](https://pypi.org/project/requests/)

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/rodericussilva/autoSendMessage.git
    cd autoSendMessage
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install selenium webdriver-manager pandas requests
    ```

4. Configure o token de acesso da API Bitly no código:

    Substitua `'YOUR TOKEN'` pelo seu token de acesso na variável `BITLY_ACCESS_TOKEN`:

    ```python
    BITLY_ACCESS_TOKEN = 'YOUR TOKEN'
    ```

## Uso

1. **Prepare os contatos e mensagens**:

   No código, edite o DataFrame `contact_df` com os nomes, números de telefone e mensagens que deseja enviar.
   Também é possível utilizar um arquivo externo, com excel, criando uma coluna para name, number e text.

3. **Execute o script**:

    Execute o script para iniciar a automação:

    ```bash
    python your_script_name.py
    ```

4. **Login no WhatsApp Web**:

    Quando o navegador abrir, escaneie o código QR com o aplicativo do WhatsApp para fazer login.

5. **Aguarde o envio das mensagens**:

    O script enviará as mensagens de acordo com os horários especificados em `restart_times`.

## Configuração do Agendamento

Você pode configurar os horários em que as mensagens serão enviadas alterando a lista `restart_times` no código, como no exemplo abaixo:

```python
restart_times = ['07:30', '09:30', '12:30', '16:30', '22:00']
```

## Considerações finais

  Este projeto foi desenvolvido para fins profissionais para automatizar o envio de mensagens via WhatsApp Web utilizando Python e Selenium. As informações sensíveis foram ocultadas.

  Antes de implementar em um ambiente de produção ou em larga escala, é recomendável revisar e adaptar o código conforme necessário, especialmente no que diz respeito ao gerenciamento de autenticação, segurança e privacidade dos dados dos usuários.

## Autor

### Rodrigo Silva
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo em rodericus@alu.ufc.br
