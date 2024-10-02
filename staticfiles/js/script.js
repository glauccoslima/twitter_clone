// Carrega os dados do usuário do localStorage
const loadUserData = () => {
  return (
    JSON.parse(localStorage.getItem("data")) || {
      loggedInUser: "null", // Valor padrão para usuário não logado
      loggedInName: "null", // Valor padrão para nome não logado
    }
  );
};

// Estado da aplicação contendo os dados do usuário
const appState = loadUserData();

// Função para exibir os dados do usuário na sidebar
const getData = () => {
  const displayHandle = document.getElementById("displayHandle"); // Elemento para exibir o handle do usuário
  const displayName = document.getElementById("displayName"); // Elemento para exibir o nome do usuário

  if (displayHandle && displayName) {
    // Verifica se os elementos existem
    if (appState.loggedInUser !== "null" && appState.loggedInName !== "null") {
      // Se o usuário estiver logado, exibe os dados do usuário
      displayHandle.innerText = `@${appState.loggedInUser}`;
      displayName.innerText = `${appState.loggedInName}`;
    } else {
      // Se o usuário não estiver logado, exibe valores padrão
      displayHandle.innerText = "@Desconhecido";
      displayName.innerText = "Usuário Desconhecido";
    }
  }
};

// Inicializa o getData após o DOM ser carregado
document.addEventListener("DOMContentLoaded", () => {
  getData();
});

// Função para adicionar um novo tweet
const addTweet = () => {
  const textArea = document.getElementById("id_content"); // Campo de texto para o conteúdo do tweet

  if (textArea) {
    const tweetContent = textArea.value.trim(); // Obtém o conteúdo do tweet e remove espaços em branco

    if (tweetContent.length === 0) {
      // Se o conteúdo do tweet estiver vazio, exibe uma mensagem de erro
      showFeedback("Tweet inválido. O conteúdo não pode estar vazio.");
      return;
    }

    const tweetCards = document.getElementById("tweetCards"); // Contêiner para os tweets

    if (tweetCards) {
      // Formata a data para o formato do Brasil (dia/mês)
      const dataFormatada = new Date().toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
      });

      // HTML do novo tweet
      const tweetHTML = `
        <div class="tweet-wrap p-3 mb-3" style="background-color: #ffffff; border-radius: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
          <div class="tweet-header d-flex">
            <img
              src="${
                appState.loggedInUser !== "null"
                  ? appState.loggedInUser.profile.image.url
                  : '{% static "img/avatar-placeholder.png" %}'
              }"
              alt="Avatar"
              class="avatar rounded-circle"
              style="width: 50px; height: 50px;"
            />
            <div class="tweet-header-info ml-3">
              <span class="username font-weight-bold">@${
                appState.loggedInUser !== "null"
                  ? appState.loggedInUser
                  : "Desconhecido"
              }</span>
              <span class="text-muted"> · ${dataFormatada}</span>
              <p class="mt-2">${tweetContent}</p>
            </div>
          </div>
        </div>
      `;

      // Insere o novo tweet no início do contêiner de tweets
      tweetCards.insertAdjacentHTML("afterbegin", tweetHTML);
      textArea.value = ""; // Limpa o campo de input após o tweet ser adicionado
    }
  }
};

// Função para exibir feedback visual
function showFeedback(message) {
  const feedbackElement = document.createElement("div"); // Cria um novo elemento div para a mensagem de feedback
  feedbackElement.className = "feedback-message"; // Define a classe CSS para estilização
  feedbackElement.innerText = message; // Define o texto da mensagem

  document.body.appendChild(feedbackElement); // Adiciona a mensagem ao corpo do documento

  setTimeout(() => {
    feedbackElement.remove(); // Remove a mensagem após 3 segundos
  }, 3000);
}

// Adiciona o evento de submit no formulário para adicionar um tweet
const tweetForm = document.querySelector("#tweetForm");
if (tweetForm) {
  tweetForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Previne o comportamento padrão do formulário
    addTweet(); // Chama a função para adicionar um tweet
  });
}

// Adiciona o evento de clique no botão de tweet, caso exista
const tweetButton = document.getElementById("tweetButton");
if (tweetButton) {
  tweetButton.addEventListener("click", (e) => {
    e.preventDefault(); // Previne o comportamento padrão do botão
    addTweet(); // Chama a função para adicionar um tweet
  });
}
