# login_automation

Esse código aqui foi feito pra automatizar a abertura de abas e processos de login no navegador chrome.
As credenciais de login podem ser salvas no arquivo config.json.

Para rodar o código será necessário ter o Python instalado no seu computador. Instale a dependência Selenium do Python.
Em seguida instale o ChromeDriver (pode ser baixado no link https://chromedriver.chromium.org/). Dê unzip no arquivo no caminho "C:\WebDriver\". Se não tiver o caminho, apenas crie um...

Após isso, o programa está praticamente pronto para rodar. Você só precisa configurar suas credencias de login.
Caso precise logar em algum outro site, você terá que inspecionar os elementos html do site para poder preencher o campo de usuário e senha. (Quase tudo pode ser resolvido copiando "full xpath").
O  template de credenciais e login estão representados no código para facilitar a automação.

OBS: O código pode depender um pouco da sua internet. Animações do site podem causar problemas na hora de realizar o login. Então utilize a função time.sleep(2) para tudo que utilizar alguma transição/animação antes de aparecer a tela de login.

OBS2: O navegador chromium que é usado por esse código não abre no youtube. Alguma coisa a ver com a política de segurança da google.
