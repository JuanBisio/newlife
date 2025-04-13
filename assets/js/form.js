const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevent HTML refresh
  const formData = new FormData(form); // Converts to array of arrays
  const obj = Object.fromEntries(formData); // Array of arrays to object
  window.location.href = `https://api.whatsapp.com/send?phone=+5493584299645&text=Nombre: ${obj.nombre}, Apellido: ${obj.Apellido}, Clase: ${obj.options}, Consulta: ${obj.Consulta}`;
});
