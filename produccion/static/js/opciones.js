
function actualizarAccion(formId, selectId, tipo) {
  let form = document.getElementById(formId);
  let select = document.getElementById(selectId);
  let selectedId = select.options[select.selectedIndex].value;

  if (select.selectedIndex !== 0) { 
      form.action = `/eliminar_producto/${tipo}/${selectedId}/`;
  } else {
      form.action = '#';
      alert("No puedes eliminar esta opción.");
  }
}

function eliminarOpcion(event, formId) {
  let form = document.getElementById(formId);
  if (form.action !== '#') {
      form.submit();
  } else {
      event.preventDefault();
  }
}