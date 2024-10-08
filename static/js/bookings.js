const editButtons = document.getElementsByClassName("btn-edit");
const bookingText = document.getElementById("id_body");
const bookingForm = document.getElementById("bookingForm");

const cancelModal = new bootstrap.Modal(document.getElementById("cancelModal"));
const cancelButtons = document.getElementsByClassName("btn-cancel");
const cancelConfirm = document.getElementById("cancelConfirm");

/**
* Initializes edit booking functionality 
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
    let bookingContent = document.getElementById(`booking${bookingId}`).innerText;
    bookingText.value = bookingContent;
    submitButton.innerText = "Update";
    bookingForm.setAttribute("action", `edit_booking/${bookingId}`);
  });
}

/**
Initializes the booking cancellation function
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("booking_id");
      cancelConfirm.href = `cancel_booking/${bookingId}`;
      cancelModal.show();
    });
  }