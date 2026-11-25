window.addEventListener("DOMContentLoaded", () => {
  // Tombol tema dipasang lebih dulu agar tetap berfungsi bila KaTeX gagal dimuat.
  const root = document.documentElement;
  const tema = document.getElementById("tema");
  const label = () => {
    tema.textContent = root.dataset.theme === "dark" ? "☀️ Mode terang" : "🌙 Mode gelap";
  };
  tema.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem("tema", root.dataset.theme); } catch (e) {}
    label();
  });
  label();
  tema.hidden = false;

  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
    ],
    throwOnError: false,
  });

  const cards = [...document.querySelectorAll(".soal")];
  const q = document.getElementById("q");
  if (!q) return;
  const topik = document.getElementById("topik");
  const jenis = document.getElementById("jenis");
  const hitung = document.getElementById("hitung");
  const text = new Map(cards.map((c) => [c, c.textContent.toLowerCase()]));

  function filter() {
    const term = q.value.trim().toLowerCase();
    let n = 0;
    for (const c of cards) {
      const ok = (!term || text.get(c).includes(term)) &&
        (!topik.value || c.dataset.topic === topik.value) &&
        (!jenis.value || c.dataset.kind === jenis.value);
      c.hidden = !ok;
      if (ok) n++;
    }
    for (const s of document.querySelectorAll("main section:not(.catatan)")) {
      s.hidden = !s.querySelector(".soal:not([hidden])");
    }
    hitung.textContent = n + " soal";
  }
  q.addEventListener("input", filter);
  topik.addEventListener("change", filter);
  jenis.addEventListener("change", filter);
  const setAll = (open) => cards.forEach((c) => { if (!c.hidden) c.querySelector("details").open = open; });
  document.getElementById("buka").addEventListener("click", () => setAll(true));
  document.getElementById("tutup").addEventListener("click", () => setAll(false));
  filter();
});
