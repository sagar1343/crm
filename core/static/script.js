const statusForm = document.getElementById("change-status-form");
const selectbox = document.getElementById("select-status");

selectbox.addEventListener("change", () => {
  statusForm.submit();
});
