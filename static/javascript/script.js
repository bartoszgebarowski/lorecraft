document.addEventListener("DOMContentLoaded", function () {
  initiateModalImages();
  removeElementAfterTime(removeSuccessDiv, 3000);
});

function createModal() {
  let modal = new bootstrap.Modal(document.querySelector("#img-modal"), {
    keyboard: false,
    backdrop: true,
  });
  modal.show();
}

function imageSrcReplacer(imageCandidate) {
  let imageCandidateSrc = imageCandidate.getAttribute("src");
  let imgModal = document.querySelector("#modal-img");
  imgModal.src = imageCandidateSrc;
  createModal();
}

function initiateModalImages() {
  let images = document.querySelectorAll(".gallery-image");
  for (let image of images) {
    image.addEventListener("click", function () {
      imageSrcReplacer(image);
    });
  }
}

function removeElementAfterTime(functionToExecute, time) {
  setTimeout(functionToExecute, time);
}

function removeSuccessDiv() {
  let targetedDiv = document.getElementById("success_message");
  if (targetedDiv) {
    targetedDiv.remove();
  }
}
