flatpickr("#fecha", { 
  dateFormat: "d-m-Y",

  locale: "es" // Configuración de idioma español
});

flatpickr("#hora", { 
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i", //formato de hora
  locale: "es",
  altInput: false // colocar pm/am
});