// Detecta cuando se abre una nueva pestaña
document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'visible') {
      // Recarga la página cuando la pestaña se vuelve visible
      window.location.reload();
    }
  });
  
  