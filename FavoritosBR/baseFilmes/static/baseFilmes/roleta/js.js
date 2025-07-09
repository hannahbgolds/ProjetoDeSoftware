let globalObjects = {};

function girarRoleta() {
    globalObjects = {
        btJogar: document.getElementById("btJogar"),
        roleta: document.getElementById("roleta"),
        btParar: document.getElementById("btParar"),
        tempoInicial: new Date()
    };

    document.getElementById("imgModal").src = "";
    globalObjects.btJogar.style.visibility = "hidden";
    globalObjects.btParar.style.visibility = "visible";
    globalObjects.roleta.style.animation = "roleta 1s linear infinite";
}

function calcularBox() {
    const tempoFinal = new Date();
    const tempo = Math.abs(tempoFinal - globalObjects.tempoInicial);
    let box = parseInt(tempo / 125);
    box = box % 8;
    return box;
}

function pararRoleta() {
  globalObjects.roleta.style["animation-play-state"] = "paused";
  globalObjects.btJogar.style.visibility = "visible";
  globalObjects.btParar.style.visibility = "hidden";

  const box = calcularBox();
  const nomesGeneros = [
      "Ação",     // 0
      "Aventura", // 1
      "Diverso",  // 2
      "Suspense", // 3
      "Faroeste", // 4
      "Fantasia", // 5
      "Drama",    // 6
      "Comédia"   // 7
  ];

  const GENRE_MAP = {
      "Ação": 28,
      "Aventura": 12,
      "Comédia": 35,
      "Drama": 18,
      "Fantasia": 14,
      "Faroeste": 37,
      "Suspense": 53,
      "Diverso": null  // pega todos
  };

  const genero = nomesGeneros[box];
  const generoId = GENRE_MAP[genero];

  const url = new URL("https://api.themoviedb.org/3/discover/movie");
  url.searchParams.set("with_origin_country", "BR");
  url.searchParams.set("sort_by", "popularity.desc");
  url.searchParams.set("language", "pt-BR");
  if (generoId) {
      url.searchParams.set("with_genres", generoId);
  }

  fetch(url.toString(), {
      headers: {
          accept: "application/json",
          Authorization: "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMWQ1MDExZGNkYWI3ZjU0OGRhNDM4ZmRhMjRjN2ViZCIsIm5iZiI6MTc1MDk5MTcxMC44NTY5OTk5LCJzdWIiOiI2ODVlMDM1ZWMwNjZhNDk0YzEzNGYyZDEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.bc5-4RE8_UXxp5d617Cw2LJfowA3x70_z_rVrU3hsa8"
      }
  })
  .then(res => res.json())
  .then(data => {
      const filmes = data.results;
      if (!filmes || filmes.length === 0) {
          alert("Nenhum filme encontrado.");
          return;
      }

      const filme = filmes[Math.floor(Math.random() * filmes.length)];
      document.getElementById("imgModal").src = filme.poster_path ? `https://image.tmdb.org/t/p/w300${filme.poster_path}` : "";
      document.getElementById("tituloModal").innerText = filme.title || "Sem título";
      document.getElementById("sinopseModal").innerText = filme.overview || "Sem sinopse";
      document.getElementById("diretorModal").innerText = ""; // TMDB não traz direto aqui
      document.getElementById("lancamentoModal").innerText = "Ano: " + (filme.release_date?.substring(0, 4) || "Desconhecido");

      abrirModal();
  })
  .catch(err => {
      console.error("Erro ao buscar filme:", err);
      alert("Erro ao buscar filme da API.");
  });
}

function abrirModal() {
  $("#ex1").modal("show");
}

