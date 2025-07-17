document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".fav-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      const juegoId = this.dataset.id;
      const icon = this.querySelector("i");

      fetch(`/games/toggleFavs/${juegoId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.favorito) {
            icon.classList.remove("text-muted");
            icon.classList.add("text-danger");
          } else {
            icon.classList.remove("text-danger");
            icon.classList.add("text-muted");
          }
        })
        .catch((error) => {
          console.error("Error al marcar favorito:", error);
        });
    });
  });
});
