fetch("http://localhost:8000/saved-tracks")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("tracks");
    data.forEach(track => {
    const li = document.createElement("li");
    li.textContent += `${track.artist} – ${track.name}`;
    list.appendChild(li);
        });
  });

  fetch("http://localhost:8000/about-user")
  .then(res => res.json())
  .then(user => {
    const header = document.querySelector("h1");
    header.textContent += ` for ${user.display_name} `;

  });



