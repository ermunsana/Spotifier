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

  fetch("http://localhost:8000/following-artists")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("artists");
    data.forEach(artist => {
    const li = document.createElement("li");
    const img = document.createElement("img");
    li.textContent += `${artist.name}`;
    list.appendChild(li);
        });
  });

  fetch("http://localhost:8000/following-artists")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("artists-images");
    data.forEach(artist => {
    const li = document.createElement("li");
    const img = document.createElement("img");
    img.src = artist.images[0]?.url || "";
    img.alt = artist.name;
    img.width = 100;
    li.appendChild(img);
    list.appendChild(li);
        });
  });

  




